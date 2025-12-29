import pytest
from infra.streaming_validator import StreamingValidator


@pytest.fixture(scope="session")
def streaming_validator():
    return StreamingValidator()