class MQuote(dict):

    def __init__(self, quote_dict: dict, media_title: str, media_type: str, year: int):
        super().__init__()
        self.update(quote_dict)
        self["media_title"] = media_title
        self["media_type"] = media_type
        self["year"] = year

    @property
    def characters(self) -> list[str]:
        return self["characters"]

    @property
    def lines(self) -> list[dict[str, str]]:
        lines = self["lines"]
        return lines

    @property
    def media_title(self) -> str:
        return self["media_title"]

    @property
    def media_type(self) -> str:
        return self["media_type"]

    @property
    def year(self) -> int:
        return self["year"]

    def __str__(self):
        lines = [
            f"{list(q.keys())[0]}: {list(q.values())[0]}" for q in self.lines]
        _str = "\n".join(lines)
        return _str
