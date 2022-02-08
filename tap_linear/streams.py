"""Stream type classes for tap-linear."""
from tap_linear.client import LinearStream
from tap_linear.schemas.issues import issuesSchema
from tap_linear.queries.issues import issuesQuery


class IssuesStream(LinearStream):

    """Define custom stream."""

    name = "Issues"
    schema = issuesSchema
    primary_keys = ["id"]
    replication_key = "updatedAt"
<<<<<<< HEAD
    query = issuesQuery
=======
    query = issuesQuery
>>>>>>> a1b3ebce19e334cd85884ffe813daa0a0084fa80
