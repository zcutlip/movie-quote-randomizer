mgquote_type_registry = {}


def register_quote_type(quote_class):
    """
    Decorator to register quote classes
    """
    quote_type = quote_class.QUOTE_TYPE
    mgquote_type_registry[quote_type] = quote_class
    return quote_class


@register_quote_type
class MQuoteSingle(dict):
    QUOTE_TYPE = "single"

    def __init__(self, quote_dict: dict, media_title: str, media_type: str, year: int):
        super().__init__()
        if quote_dict["quote_type"] != self.QUOTE_TYPE:
            raise ValueError(f"Invalid quote type: {quote_dict["quote_type"]}")
        self.update(quote_dict)
        self["media_title"] = media_title
        self["media_type"] = media_type
        self["year"] = year

    @property
    def characters(self) -> list[str]:
        return self["characters"]

    @property
    def lines(self) -> list[dict[str, str]]:
        line = {self._character(): self._line()}
        return [line]

    @property
    def media_title(self) -> str:
        return self["media_title"]

    @property
    def media_type(self) -> str:
        return self["media_type"]

    @property
    def year(self) -> int:
        return self["year"]

    def _line(self) -> str:
        return self["line"]

    def _character(self) -> str:
        return self.characters[0]


@register_quote_type
class MQuoteDialogue(MQuoteSingle):
    QUOTE_TYPE = "dialogue"

    @property
    def lines(self) -> list[dict[str, str]]:
        lines = self["lines"]
        return lines
