import logging

class LoggingHandler:
    """
    Responsible for fetching the correct logger.
    Refactored to rely on the root logger configuration (pytest.ini) 
    to avoid duplicate log entries.
    """
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        # We REMOVED the StreamHandler setup. 
        # Pytest (or the main app config) now handles the output format.
        
        # Ensure we don't accidentally filter out INFO logs before they reach Pytest
        self.logger.setLevel(logging.INFO)

    def log_info(self, message):
        self.logger.info(message)

    def log_error(self, message):
        self.logger.error(message)