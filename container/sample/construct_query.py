import sys


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
        query = query.format(fields=fields, table=table,
                             extra=extra_order.format(grouped_fields=group))
    else:
        query = query.format(fields=fields, table=table, extra="")

    return query
