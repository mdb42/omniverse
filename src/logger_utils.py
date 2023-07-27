import logging
import sys

def create_logger(logger_name, log_file, level=logging.INFO):
    # Create a custom logger
    logger = logging.getLogger(logger_name)
    logger.setLevel(level)

    # Create handlers
    file_handler = logging.FileHandler(log_file)
    file_handler.setLevel(level)

    std_handler = logging.StreamHandler(sys.stdout)
    std_handler.setLevel(logging.ERROR)

    # Create formatters and add it to handlers
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)

    # Add the handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(std_handler)

    return logger

def encrypt_log(log_file):
    # Implement your log file encryption logic here
    pass

def anonymize_log(log_file):
    # Implement your log anonymization logic here
    pass

# Usage:
# logger = create_logger('my_logger', 'log.txt')
# logger.info('This is an info message')
