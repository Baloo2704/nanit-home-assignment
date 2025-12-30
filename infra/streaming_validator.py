import requests
from pydantic import ValidationError
from infra.schemas import PerformanceMetrics, HealthCheck


class StreamingValidator:
    def __init__(self, base_url):
        self.base_url = base_url
        
    def get_metrics(self):
        """Fetches the /metrics endpoint and returns the json response."""
        response = requests.get(f"{self.base_url}/metrics")
        response.raise_for_status()
        return response.json()
    
    def get_health_metrics(self):
        """Fetches raw JSON from /health."""
        response = requests.get(f"{self.base_url}/health")
        response.raise_for_status()
        return response.json()
    
    def set_network_condition(self, condition):
        """
        Sets network conditoin.
        Valid values: 'normal', 'poor', 'terrible'
        """
        url = f"{self.base_url}/control/network/{condition}"
        response = requests.put(url)
        response.raise_for_status()

    def validate_streaming_performance(self):
        """Validates structure using the PerformanceMetrics Pydantic model."""
        metrics = self.get_metrics()
        
        if 'performance' not in metrics:
            raise ValueError("Validation Failed: 'performance' key missing")
            
        try:
            # MAGIC HAPPENS HERE: 
            # 1. Checks all keys exist
            # 2. Checks types (e.g., latency is a number, not a string)
            # 3. Strips out unknown extra fields (optional)
            validated_metrics = PerformanceMetrics(**metrics['performance'])
            
            # Return the validated object (or dict if you prefer)
            return validated_metrics.model_dump()
            
        except ValidationError as e:
            # Returns a very detailed error about exactly which key failed
            raise ValueError(f"Schema Validation Failed: {e}")

    def validate_health_check(self):
        """
        Stage 3 Validation:
        Strictly validates the schema of the /health response against the HealthCheck model.
        Does NOT enforce specific status values (logic moved to test).
        
        Returns:
            HealthCheck: The validated Pydantic model object.
        """
        # 1. Fetch
        data = self.get_health_metrics()
        
        # 2. Schema Validation (Pydantic)
        # This guarantees 'status', 'viewers', 'timestamp' etc. exist and have correct types.
        return HealthCheck(**data)