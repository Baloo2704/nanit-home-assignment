import logging
import os

class LoggingHandler:
    @staticmethod
    def setup_file_logging(test_name: str) -> logging.FileHandler:
        """
        Attaches a FileHandler to the Root Logger for the specific test.
        Returns the handler object so it can be removed later.
        """
        logger = logging.getLogger()
        
        # Ensure the logs directory exists
        log_dir = "logs"
        os.makedirs(log_dir, exist_ok=True)
        
        # Create the File Handler
        file_path = f"{log_dir}/{test_name}.log"
        file_handler = logging.FileHandler(file_path, mode='w')
        
        # Define a detailed format for the file (can be different from console!)
        formatter = logging.Formatter(
            '%(asctime)s [%(levelname)s] [%(name)s]: %(message)s',
            datefmt='%d-%m-%Y %H:%M:%S'
        )
        file_handler.setFormatter(formatter)
        
        # Add to Root Logger
        logger.addHandler(file_handler)
        
        return file_handler