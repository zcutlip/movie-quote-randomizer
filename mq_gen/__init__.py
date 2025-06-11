try:
    # register colored_traceback hook if in a dev environment (dev-reqs.txt)
    import colored_traceback.auto
except ImportError:  # pragma: no coverage
    # otherwise just stick to the basics
    pass

from .__about__ import __summary__, __title__, __version__
# this causes the quote class decorators to fire and register them
from .quote_types import MQuoteDialogue, MQuoteSingle
