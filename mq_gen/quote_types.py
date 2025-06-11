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

    def __init__(self, quote_dict: dict):
        super().__init__()
        if quote_dict["quote_type"] != self.QUOTE_TYPE:
            raise ValueError(f"Invalid quote type: {quote_dict["quote_type"]}")
        self.update(quote_dict)

    def characters(self) -> list[str]:
        return self["characters"]

    def lines(self) -> list[dict[str, str]]:
        line = {self._character(): self._line()}
        return [line]

    def _line(self) -> str:
        return self["line"]

    def _character(self) -> str:
        return self.characters()[0]


@register_quote_type
class MQuoteDialogue(MQuoteSingle):
    QUOTE_TYPE = "dialogue"

    def __init__(self, quote_dict: dict):
        super().__init__(quote_dict)

    def lines(self) -> list[dict[str, str]]:
        lines = self["lines"]
        return lines
