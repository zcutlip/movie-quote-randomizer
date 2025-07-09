import json

try:
    from jsonschema import validate as jsonschema_validate
except ImportError:
    def jsonschema_validate(*args, **kwargs) -> None:
        pass

from . import data
from .pkg_resources import data_location_as_path


def validate_quotes_json(obj: object):
    schema_src = data_location_as_path(data, data.QUOTES_SCHEMA_JSON)
    schema = json.load(open(schema_src))
    return jsonschema_validate(obj, schema)
