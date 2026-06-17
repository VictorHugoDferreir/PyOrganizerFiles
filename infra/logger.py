import logging

class LoggerFactory:
    @staticmethod
    def create_logger() -> logging.Logger:
        logger = logging.getLogger("OrganizerLogger")
        logger.setLevel(logging.INFO)

        if not logger.hasHandlers():

            file_handler = logging.FileHandler(
                "organizer.log",
                encoding="utf-8"
            )

        # Create formatter and add it to the handlers
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            file_handler.setFormatter(formatter)

        # Add the handlers to the logger
            logger.addHandler(file_handler)

        return logger