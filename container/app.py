import logging
from sample.construct_query import construct_query
from sample.exec_query import exec_query

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
        fields=["applicationId", "COUNT(1) AS number"],
        table="presentation.AGG__game_performance",
        group=["applicationId"]
    )
    logging.info(query)
    logging.info(
        "Let us execute that query. This function will require mocking when tested")

    result = exec_query("/opt/container/secret.json", query)
    for i in range(10):
        row = result[i]
        logging.info(row)
