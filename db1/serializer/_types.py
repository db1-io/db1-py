"""Types used in the serializer package."""

from typing import Any, Dict, Union

import numpy as np
import pandas as pd

PY_TYPES_ = Union[
    int, float, str, bool, bytes, list, Dict[str, Any], np.ndarray, pd.DataFrame
]
"""Python serialization types for type hints."""


PY_TYPES = [int, float, str, bool, bytes, list, dict, np.ndarray, pd.DataFrame]
"""Python serialization types."""
