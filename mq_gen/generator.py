import json
import secrets
from pathlib import Path
from typing import Any

from . import data
from .pkg_resources import data_location_as_path
from .quote_types import MQuote


class MQGenerator:

    def __init__(self, quote_data: str | Path | dict = None):
        if quote_data is None:
            quote_data = data_location_as_path(data, data.DEFAULT_QUOTES_JSON)
        if not isinstance(quote_data, dict):
            quote_data = json.load(open(quote_data))
        self._media_title = quote_data["meta"]["media_title"]
        self._media_type = quote_data["meta"]["media_type"]
        self._year = quote_data["meta"]["year"]
        self._description = quote_data["meta"]["description"]
        self._quotes = []
        quote_dicts = quote_data["quotes"]
        self.populate_quotes(quote_dicts)

    def populate_quotes(self, quote_dicts: dict[str, Any]):
        for quote_dict in quote_dicts:
            quote_obj = MQuote(quote_dict, self._media_title,
                               self._media_type, self._year)
            self._quotes.append(quote_obj)

    def random_quote(self):
        idx = secrets.choice(range(0, len(self._quotes)))
        quote = self._quotes[idx]
        return quote
