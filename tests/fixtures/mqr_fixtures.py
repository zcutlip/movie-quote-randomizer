import json
from pathlib import Path

import pytest

from .support.paths import VALID_INPUT_DATA_PATH


@pytest.fixture
def external_data():
    zero_wing_path = Path(VALID_INPUT_DATA_PATH, "zero-wing.json")
    zero_wing_data = json.load(open(zero_wing_path))

    return zero_wing_data
