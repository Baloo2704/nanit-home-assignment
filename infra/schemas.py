from pydantic import BaseModel, Field, ValidationError

class PerformanceMetrics(BaseModel):
    # We define the keys and their expected types here.
    # If the server adds 50 new keys, you just add them here.
    average_latency_ms: float = Field(..., description="Network latency in milliseconds")
    jitter_ms: float
    packet_loss_rate: float
    
    # Example of scalability: You can make fields optional if needed
    # buffer_health: Optional[float] = None