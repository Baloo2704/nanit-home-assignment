import pytest

@pytest.mark.api
@pytest.mark.parametrize("initial_condition,final_condition", [
    ("normal", "poor"),
    ("poor", "terrible"),
    ("normal", "terrible")
])
def test_stream_performance_degradation(streaming_validator, initial_condition, final_condition):
    # 1. Initial Condition
    streaming_validator.set_network_condition(initial_condition)
    perf_initial = streaming_validator.validate_streaming_performance()
    initial_latency = perf_initial['average_latency_ms']

    # 2. Switch to Final Condition
    streaming_validator.set_network_condition(final_condition)
    perf_final = streaming_validator.validate_streaming_performance()
    final_latency = perf_final['average_latency_ms']

    # 3. Assert degradation of latency
    assert final_latency > initial_latency, (
        f"Expected higher latency under {final_condition} conditions. "
        f"{initial_condition.capitalize()}: {initial_latency} ms, "
        f"{final_condition.capitalize()}: {final_latency} ms"
    )