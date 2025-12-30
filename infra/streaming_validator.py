import requests
from infra.base_session import BaseSession
from infra.schemas import PerformanceMetrics, HealthCheck

class StreamingValidator(BaseSession):
    """
    Validates the Streaming Server API.
    Inherits retry logic from BaseSession to handle network flakiness.
    """
    def __init__(self, base_url):
        super().__init__(name="API_VALIDATOR")
        self.base_url = base_url

    def _get_request(self, endpoint):
        """
        Internal helper.
        This function is passed to self.retry_operation, so it doesn't need
        its own error handling logic here.
        """
        response = requests.get(f"{self.base_url}{endpoint}")
        response.raise_for_status()
        return response.json()

    def get_metrics(self):
        # Executes _get_request with automatic retries (default 3 attempts)
        return self.retry_operation(self._get_request, endpoint="/metrics")

    def get_health_metrics(self):
        return self.retry_operation(self._get_request, endpoint="/health")

    def set_network_condition(self, condition):
        url = f"{self.base_url}/control/network/{condition}"
        self.log_info(f"Setting network condition to: {condition}")
        
        # We can also wrap PUT requests in retry logic if desired
        def _put():
            resp = requests.put(url)
            resp.raise_for_status()
            return resp
            
        self.retry_operation(_put)

    def validate_streaming_performance(self):
        """
        Validates structure using PerformanceMetrics schema.
        """
        data = self.get_metrics()
        
        if 'performance' not in data:
            self.log_error("'performance' key missing in metrics response")
            raise ValueError("Validation Failed: 'performance' key missing")
            
        validated_metrics = PerformanceMetrics(**data['performance'])
        return validated_metrics.model_dump()

    def validate_health_check(self):
        """
        Validates structure using HealthCheck schema.
        """
        data = self.get_health_metrics()
        # Returns the validated Pydantic model
        return HealthCheck(**data)