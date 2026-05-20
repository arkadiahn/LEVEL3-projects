from dagster import Definitions, definitions

from bike_rental.defs.assets.hello import hello


@definitions
def defs() -> Definitions:
    return Definitions(
        assets=[
            hello,
        ]
    )
