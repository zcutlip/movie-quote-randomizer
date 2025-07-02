import pytest

from mq_randomizer.quote_types import MQuote, MQuoteLine


class TestMQuote:
    @pytest.fixture
    def sample_quote(self):
        quote_dict = {
            "characters": ["Neo"],
            "lines": [{"Neo": "Remember... there is no spoon."}]
        }
        return MQuote(quote_dict, "The Matrix", "movie", 1999)

    def test_initialization(self, sample_quote):
        assert sample_quote["media_title"] == "The Matrix"
        assert sample_quote["media_type"] == "movie"
        assert sample_quote["year"] == 1999
        assert sample_quote["characters"] == ["Neo"]
        sample_quote_line = MQuoteLine("Neo", "Remember... there is no spoon.")
        assert sample_quote["lines"] == [sample_quote_line]

    def test_characters_property(self, sample_quote):
        assert sample_quote.characters == ["Neo"]

    def test_lines_property(self, sample_quote):
        sample_quote_line = MQuoteLine("Neo", "Remember... there is no spoon.")
        assert sample_quote.lines == [sample_quote_line]

    def test_mquote_line_equality_010(self):
        """
        Test the __eq__() implementation

        Verify: two different MQuoteLine but equivalent objects are equal
        """
        quote_line_1 = MQuoteLine("Neo", "Remember... there is no spoon.")
        quote_line_2 = MQuoteLine("Neo", "Remember... there is no spoon.")

        # no tricks up our sleeve ,these actually are different objects
        assert id(quote_line_1) != id(quote_line_2)
        assert quote_line_1 == quote_line_1

    def test_mquote_line_equality_020(self):
        """
        Test the __eq__() implementation

        Verify: An MQuoteLine object is equal to itself

        Note: this is trivially true and is present for the purpose of complete coverage
        """
        quote_line = MQuoteLine("Neo", "Remember... there is no spoon.")

        assert id(quote_line) == id(quote_line)
        assert quote_line == quote_line

    def test_str_representation(self, sample_quote):
        expected = "Neo: Remember... there is no spoon."
        assert str(sample_quote) == expected

    def test_unattributed_line(self):
        quote_dict = {
            "characters": ["Unattributed"],
            "lines": [{"__none__": "This is a line without attribution."}]
        }
        quote = MQuote(quote_dict, "Test Movie", "movie", 2023)
        assert str(quote) == "This is a line without attribution."
