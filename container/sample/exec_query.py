
from sample.construct_query import construct_query
from sample.bq_helpers import get_bq_client, get_query_as_array_dict


def exec_query(secret, query):
    """Executes query using client made from secret, returns result"""
    assert isinstance(secret, str)
    assert isinstance(query, str)

    client = get_bq_client(secret)

    return get_query_as_array_dict(client, query)
