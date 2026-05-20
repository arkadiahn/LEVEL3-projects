import dagster as dg


@dg.asset
def hello() -> str:
    return "Hello world!"
