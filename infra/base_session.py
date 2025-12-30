from abc import ABC
# UPDATED IMPORTS
from infra.handlers import LoggingHandler, RetryHandler

class BaseSession(ABC):
    """
    Abstract Base Class that delegates functionality to specialized handlers.
    """
    def __init__(self, name="BaseSession"):
        # 1. Compose the Logger
        self._logger = LoggingHandler(name)
        
        # 2. Compose the Retrier
        self._retrier = RetryHandler(self._logger)

    def log_info(self, message):
        self._logger.log_info(message)

    def log_error(self, message):
        self._logger.log_error(message)

    def retry_operation(self, func, retries=3, delay=1, **kwargs):
        return self._retrier.retry(func, retries, delay, **kwargs)