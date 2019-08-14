
from google.cloud import bigquery as bq


def get_query_as_array_dict(client, query): 
    results = [parse_bq_result(row) for row in client.query(query)]

    return results

def parse_bq_result(row):
    parsed_result = {}

    for key, val in row.items():
        parsed_result[key] = val

    return parsed_result

def get_bq_client(secret):
    """ returns bq client """ 
    client = bq.Client.from_service_account_json(
        secret
    )

    projects = [project.project_id for project in client.list_projects()]
    # Force the project
    return bq.Client.from_service_account_json(
        secret,
        project=projects[0]
    ) 