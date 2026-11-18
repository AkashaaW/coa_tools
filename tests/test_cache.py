import unittest

from coa_tools.cache import split_address, access_cache


class CacheTests(unittest.TestCase):
    def test_address_split(self):
        self.assertEqual(split_address(19), (1, 0, 3))

    def test_first_access_is_miss(self):
        cache_lines = [None] * 4
        self.assertEqual(access_cache(16, cache_lines), "MISS")

    def test_same_block_is_hit(self):
        cache_lines = [None] * 4
        access_cache(16, cache_lines)
        self.assertEqual(access_cache(19, cache_lines), "HIT")

    def test_replacement_causes_miss(self):
        cache_lines = [None] * 4
        access_cache(16, cache_lines)
        access_cache(0, cache_lines)
        self.assertEqual(access_cache(16, cache_lines), "MISS")