import time
from requests.exceptions import RequestException

class RetryHandler:
    """
    Responsible solely for executing functions with retry logic.
    """
    def __init__(self, logger_handler):
        # Inject dependency: Logger
        self.logger = logger_handler

    def retry(self, func, retries=3, delay=1, **kwargs):
        """
        Executes 'func' and retries on specific exceptions.
        """
        last_exception = None
        for attempt in range(retries):
            try:
                return func(**kwargs)
            except (RequestException, ValueError, KeyError) as e:
                last_exception = e
                self.logger.info(f"Operation failed (Attempt {attempt+1}/{retries}). Retrying in {delay}s...")
                time.sleep(delay)

        self.logger.error(f"Operation failed permanently after {retries} attempts.")

        if last_exception:
            raise last_exception
        
        # Fallback for edge case (e.g retires=0)
        raise RuntimeError(f"Operation failed: Max retries ({retries}) exceeded or invalid configuration.")