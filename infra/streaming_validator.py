import requests
from infra.base_session import BaseSession
from infra.schemas import PerformanceMetrics, HealthCheck

class StreamingValidator(BaseSession):
    """
    Validates the Streaming Server API.
    Inherits retry logic from BaseSession to handle network flakiness.
    """
    def __init__(self, base_url):
        super().__init__(name="API")
        self.base_url = base_url

    def _get_request(self, endpoint):
        """
        Internal helper.
        This function is passed to self.retry_operation, so it doesn't need
        its own error handling logic here.
        """
        self._logger.info(f"Making GET request to: {self.base_url}{endpoint}")
        response = requests.get(f"{self.base_url}{endpoint}", timeout=5)
        response.raise_for_status()
        self._logger.info(f"GET {endpoint} response: {response.text}")
        return response.json()

    def get_metrics(self):
        # Executes _get_request with automatic retries (default 3 attempts)
        return self.retry_operation(self._get_request, endpoint="/metrics")

    def get_health_metrics(self):
        return self.retry_operation(self._get_request, endpoint="/health")

    def set_network_condition(self, condition):
        url = f"{self.base_url}/control/network/{condition}"
        self._logger.info(f"Setting network condition to: {condition}")
        
        # We can also wrap PUT requests in retry logic if desired
        def _put():
            self._logger.info(f"Making PUT request to: {url}")
            resp = requests.put(url)
            resp.raise_for_status()
            self._logger.info(f"Network condition set response: {resp.json()}")
            return resp
            
        self.retry_operation(_put)

    def validate_streaming_performance(self):
        """
        Validates structure using PerformanceMetrics schema.
        """
        self._logger.info("Validating streaming performance metrics")
        data = self.get_metrics()
        
        if 'performance' not in data:
            self._logger.error("'performance' key missing in metrics response")
            raise ValueError("Validation Failed: 'performance' key missing")
            
        validated_metrics = PerformanceMetrics(**data['performance'])
        self._logger.info(f"Validated performance metrics: {validated_metrics.model_dump()}")
        return validated_metrics.model_dump()

    def validate_health_check(self):
        """
        Validates structure using HealthCheck schema.
        """
        self._logger.info("Validating health check metrics")
        data = self.get_health_metrics()
        # Returns the validated Pydantic model
        self._logger.info(f"Validated health check metrics: {data}")
        return HealthCheck(**data)