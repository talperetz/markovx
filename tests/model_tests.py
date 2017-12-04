#!/usr/bin/env python

"""
:Date: 12/4/17
:TL;DR: tests for markovx.model module
"""

import unittest
from markovx.model import MarkovModel


class MarkovModelTestCase(unittest.TestCase):
    _inputs = [(1, 2, 3), ('q', 'w', 'a', 's', 'd'), 'qwerty123456', 'qwerty', '!@#$RDAs',
               '123456787654', 'asdafhqwjke', '123\nas\v\b\dq\wer']
    _input = _inputs[-1]

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

    def test_add_one(self):
        mx = MarkovModel()
        mx.add_one(self._input)

    def test_add_many(self):
        mx = MarkovModel()
        mx.add_many(self._inputs)

    def test_generate(self):
        mx = MarkovModel()
        mx.add_many(self._inputs)
        self.assertEqual(len(mx.generate(5)), 5)


if __name__ == '__main__':
    unittest.main()
