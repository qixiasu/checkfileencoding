#!/usr/bin/env python

"""Tests for `checkfileencoding` package."""


import unittest

from checkfileencoding.filefunc import get_encoding


class TestCheckfileencoding(unittest.TestCase):
    """Tests for `checkfileencoding` package."""

    def setUp(self):
        """Set up test fixtures, if any."""

    def tearDown(self):
        """Tear down test fixtures, if any."""

    def test_000_something(self):
        """Test something."""

    def test_get_encoding(self):
        assert get_encoding.get_encoding('/home/travis/build/qinxian1989/checkfileencoding/tests/test.csv')['encoding'] == 'gb18030'
