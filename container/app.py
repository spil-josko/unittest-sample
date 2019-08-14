import logging
from sample.construct_query import construct_query

if __name__ == "__main__":

    logger = logging.getLogger()
    consoleHandler = logging.StreamHandler()
    logFormatter = logging.Formatter(
        "[%(levelname)s] %(message)s")
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)
    logger.setLevel(logging.INFO)

    logging.info(
        "This is the unittest sample. It has a few functions for the purpose of demonstrating unittests.")

    logging.info(
        "Will no demonstrate a simple query construction. It is called correctly in the sample.")
    query = construct_query(
        fields=["level", "COUNT(1) AS number"],
        table="fake_users",
        group=["level"]
    )
    logging.info(query)
