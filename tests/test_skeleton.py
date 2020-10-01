# -*- coding: utf-8 -*-

import pytest
from fred_md.skeleton import fib

__author__ = "NoFishLikeIan"
__copyright__ = "NoFishLikeIan"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
