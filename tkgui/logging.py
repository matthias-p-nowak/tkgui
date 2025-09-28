import logging
import datetime

def configureLogging():
    # Configure logging
    now = datetime.datetime.now()
    logging.basicConfig(
        level=logging.DEBUG,  # Minimum level to log
        format="%(asctime)s [%(levelname)s] %(message)s",  # Log format
        datefmt="%Y-%m-%d %H:%M:%S",  # Timestamp format
        filename=now.strftime("%Y-%m-%d %H.log"),  # Save to a file
        filemode="w",  # Overwrite the log file each run; use "a" to append
    )
    logging.debug("Logging configured")
