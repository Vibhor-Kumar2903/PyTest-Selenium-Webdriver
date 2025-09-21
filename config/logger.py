import logging

def get_logger():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(massage)s",
        handlers=[
            logging.FileHandler("app.log", mode='w'),
            logging.StreamHandler()
        ]
    )
    return logging.getLogger()

