import json
import secrets
from pathlib import Path
from typing import Any

from . import data
from .json_validation import validate_quotes_json
from .pkg_resources import data_location_as_path
from .quote_types import MQuote


class MQRandomizer:
    """
    A random quote generator for movie, TV show, or video game quotes.

    Parameters
    ----------
    quote_data_src : str | Path | dict[str, Any], optional
        The source of quote data. Can be a file path, directory path, or pre-loaded dictionary.
        If None, defaults to the package's default quotes.
    """

    def __init__(self, quote_data_src: str | Path | dict[str, Any] = None):

        if quote_data_src is None:
            # if we wern't given a quote data object,
            # use the default
            quote_data = self._default_quote_data()
        elif not isinstance(quote_data_src, dict):
            # quote_data_src, either default or caller-provided
            # is not a dict and should represent a path to the data
            quote_data = json.load(open(quote_data_src))
        else:
            # quote_data_src is a dict, and doesn't need to be
            # loaded from disk via json
            quote_data = quote_data_src

        # if validation is enabled and is successful, this returns True
        # if validation is disabled, this returns False
        # and exception is raised if validation fails
        self._validated = validate_quotes_json(quote_data)

        self._media_title = quote_data["meta"]["media_title"]
        self._media_type = quote_data["meta"]["media_type"]
        self._year = quote_data["meta"]["year"]
        self._description = quote_data["meta"]["description"]
        self._quotes: list[MQuote] = []
        quote_dicts = quote_data["quotes"]
        self._quotes = self._populate_quotes(quote_dicts)

    def _default_quote_data(self):
        # for easier monkeypatching during tests
        quote_data_src = data_location_as_path(
            data, data.DEFAULT_QUOTES_JSON)
        quote_data = json.load(open(quote_data_src))
        return quote_data

    def _populate_quotes(self, quote_dicts: list[dict[str, Any]]) -> list[MQuote]:
        quotes = []
        for quote_dict in quote_dicts:
            quote_obj = MQuote(quote_dict, self._media_title,
                               self._media_type, self._year)
            quotes.append(quote_obj)
        return quotes

    def quote_at_index(self, index: int):
        quote = self._quotes[index]
        return quote

    def random_quote(self):
        """
        Randomly select and return a quote from the collection.

        Returns
        -------
        MQuote
            A randomly selected quote object.
        """
        idx = secrets.choice(range(0, len(self._quotes)))
        return self.quote_at_index(idx)
