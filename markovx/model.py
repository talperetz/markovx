#!/usr/bin/env python

"""
:Date: 12/4/17
:TL;DR: Markov model implementation
"""

from collections import defaultdict, Counter
from itertools import chain
import numpy as np
import random


class MarkovModel:
    _chain_start = '__begin__'
    _chain_end = '__end__'
    _with_repetitions = True
    _token_to_tokens_occurrences = defaultdict(Counter)

    def add_one(self, iterable):
        iterable = iter(iterable)
        peek = next(iterable)
        self._token_to_tokens_occurrences[self._chain_start][peek] += 1
        iterable = chain([peek], iterable)
        for p, q in MarkovModel._pair(iterable):
            self._token_to_tokens_occurrences[p][q] += 1
        self._token_to_tokens_occurrences[q][self._chain_end] += 1

    def add_many(self, iterable):
        for it in iterable:
            self.add_one(it)

    def generate(self, n, random_init=False, smart_ending=True):
        res = []
        current_token = random.choice(list(self._token_to_tokens_occurrences)) if random_init else self._chain_start

        for _ in range(n):
            current_token = self._generate_next_token(current_token)
            if current_token == self._chain_end:
                if smart_ending:
                    break
                else:
                    current_token = random.choice(list(self._token_to_tokens_occurrences))
            res.append(current_token)
        return res

    def _generate_next_token(self, current_token):
        token_to_occurrences = self._token_to_tokens_occurrences[current_token]
        token_total_occurrences = sum(token_to_occurrences.values())
        probs = list(map(lambda o: o / token_total_occurrences, token_to_occurrences.values()))
        next_token = np.random.choice(list(token_to_occurrences.keys()), 1, p=probs)[0]
        current_token = next_token
        return current_token

    @staticmethod
    def _pair(iterable):
        iterator = iter(iterable)
        last = next(iterator)
        for curr in iterator:
            yield last, curr
            last = curr
