import logging
from abc import ABC
from infra.handlers import RetryHandler

class BaseSession(ABC):
    """
    Abstract Base Class that delegates functionality to specialized handlers.
    """
    def __init__(self, name="BaseSession"):
        # 1. Compose the Logger
        self._logger = logging.getLogger(name)
        
        # 2. Compose the Retrier
        self._retrier = RetryHandler(self._logger)

    def retry_operation(self, func, retries=3, delay=1, **kwargs):
        return self._retrier.retry(func, retries, delay, **kwargs)