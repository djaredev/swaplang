from swaplang.utils.logger import logger
from swaplang.database import init_db


def prestart():
    logger.info("Running prestart script...")
    init_db()
    logger.info("Prestart script completed.")


if __name__ == "__main__":
    prestart()
