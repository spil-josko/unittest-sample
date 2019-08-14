import logging

def construct_query(*args, **kwargs):
    """Simple query construction. Purpose is to unit test it for demonstration purposes"""
    query = "SELECT {fields} FROM {table} {extra}"
    extra_order = "GROUP BY {grouped_fields}"


    fields = kwargs.get("fields")
    table = kwargs.get("table")
    group = kwargs.get("group")

    # This function is a bit more assertive than we usually do. Again, demonstration purposes
    assert isinstance(fields, list)
    assert isinstance(table, str)
    assert isinstance(group, list) or group is None

    fields = ",".join(fields)  

    if group:
        group = ",".join(group) 
        query = query.format(fields = fields, table = table, extra = extra_order.format(grouped_fields = group))
    else:
        query = query.format(fields = fields, table = table, extra="")

    return query

if __name__ == "__main__":

    logger = logging.getLogger()
    consoleHandler = logging.StreamHandler()
    logFormatter = logging.Formatter(
        "[%(levelname)s] %(message)s")
    consoleHandler.setFormatter(logFormatter)
    logger.addHandler(consoleHandler)
    logger.setLevel(logging.INFO)

    logging.info("This is the unittest sample. It has a few functions for the purpose of demonstrating unittests.")

    logging.info("Will no demonstrate a simple query construction. It is called correctly in the sample.")
    query = construct_query(
        fields = ["level", "COUNT(1) AS number"],
        table = "fake_users",
        group = ["level"]
    ) 
    logging.info(query)