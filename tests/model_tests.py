#!/usr/bin/env python

"""
:Date: 12/4/17
:TL;DR: tests for markovx.model module
"""

import unittest
from markovx.models import MarkovModel, OrdinalMarkovModel


class BaseTestCase(unittest.TestCase):
    _inputs = [(1, 2, 3), ('q', 'w', 'a', 's', 'd'), 'qwerty123456', 'qwerty', '!@#$RDAs',
               '123456787654', 'asdafhqwjke', '123\nas\v\b\dq\wer']
    _input = _inputs[-1]


class BaseMarkovTestCase(BaseTestCase):
    def test_pair(self):
        pairs_curr_tokens, pairs_next_tokens = list(), list()
        pairs = MarkovModel._pair(self._input)
        pairs_res = next(pairs, None)
        while pairs_res is not None:
            pairs_curr_tokens.append(pairs_res[0])
            pairs_next_tokens.append(pairs_res[1])
            pairs_res = next(pairs, None)
        self.assertEqual(pairs_curr_tokens, list(self._input[0:-1]))
        self.assertEqual(pairs_next_tokens, list(self._input[1:]))


class MarkovModelTestCase(BaseTestCase):
    def test_add_one(self):
        mx = MarkovModel()
        mx.add_one(self._input)

    def test_add_many(self):
        mx = MarkovModel()
        mx.add_many(self._inputs)

    def test_generate(self):
        mx = MarkovModel()
        mx.add_many(self._inputs)
        self.assertEqual(len(mx.generate(5, smart_ending=False)), 5)


class OrdinalMarkovModelTestCase(BaseTestCase):
    def test_add_one(self):
        mx = OrdinalMarkovModel()
        mx.add_one(self._input)

    def test_add_many(self):
        mx = OrdinalMarkovModel()
        mx.add_many(self._inputs)

    def test_generate(self):
        mx = OrdinalMarkovModel()
        mx.add_many(self._inputs)
        self.assertEqual(len(mx.generate(5, smart_ending=False)), 5)

    def check(self):
        mx = OrdinalMarkovModel()
        mx.add_many(self._inputs)
        print(mx.generate(5, smart_ending=False))


if __name__ == '__main__':
    unittest.main()
