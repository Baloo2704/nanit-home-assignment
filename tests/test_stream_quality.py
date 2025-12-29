def test_stream_performance_degradation(streaming_validator):
    # 1. Normal Condition
    streaming_validator.set_network_condition("normal")

    # Validate normal performance structure, types and get latency
    perf_normal = streaming_validator.validate_streaming_performance()
    normal_latency = perf_normal['average_latency_ms']

    # 2. Switch Poor Condition
    streaming_validator.set_network_condition("poor")

    # Validate poor performance structure, types and get latency
    perf_poor = streaming_validator.validate_streaming_performance()
    poor_latency = perf_poor['average_latency_ms']

    # 3. Assert degradation of latency
    assert poor_latency > normal_latency, (
        f"Expected higher latency under poor conditions. "
        f"Normal: {normal_latency} ms, Poor: {poor_latency} ms"
    )