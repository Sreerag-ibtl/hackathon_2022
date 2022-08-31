"""Assert equality of objects

This module implement test_equality that
asserts equality of two objects.

    Typical example:
        pytest test/test_equality.py
"""

from typing import Any, List

import pytest

from hackathon.inspection import get_nu_contours

# Expect, returned number of contours
expected_nu_contours: List[int] = [2, 2, 2, 2, 2]
returned_nu_contours: List[int] = list(
    map(
        get_nu_contours,
        [
            "test/good.png",
            "test/defect1.png",
            "test/defect2.png",
            "test/defect3.png",
            "test/defect4.png",
        ],
    )
)

# Expected, returned co-ordinates


@pytest.mark.parametrize(
    "expected, returned", [(expected_nu_contours, returned_nu_contours)]
)
def test_equality(expected: Any, returned: Any) -> None:

    """Assert equality of objects

    This function assert equality of two objects.

    Args:
        expected: Expected object.
        returned: Returned object.

    Returns:
        This function returns None.

    Raises:
        Raises AssertionError if returned != expected.
    """

    assert returned == expected
