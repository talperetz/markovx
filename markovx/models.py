#!/usr/bin/env python

"""
:Date: 12/4/17
:TL;DR: Markov model implementation
"""

from collections import defaultdict, Counter
from itertools import chain
from abc import ABC, abstractclassmethod
import numpy as np
import random


class BaseMarkov(ABC):
    _chain_start = '__begin__'
    _chain_end = '__end__'

    @abstractclassmethod
    def add_one(self, iterable):
        pass

    def add_many(self, iterable):
        for it in iterable:
            self.add_one(it)

    @abstractclassmethod
    def generate(self, n, **kwargs):
        pass

    def _choose_random_token(self, possible_tokens):
        if self._chain_start in possible_tokens:
            possible_tokens.remove(self._chain_start)
        assert len(possible_tokens) > 0, 'Not enough samples to learn from'
        return random.choice(possible_tokens)

    @staticmethod
    def _generate_next_token(token_to_occurrences):
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


class MarkovModel(BaseMarkov):
    _token_to_tokens_occurrences = defaultdict(Counter)

    def add_one(self, iterable):
        iterable = iter(iterable)
        peek = next(iterable)
        self._token_to_tokens_occurrences[self._chain_start][peek] += 1
        iterable = chain([peek], iterable)
        for p, q in MarkovModel._pair(iterable):
            self._token_to_tokens_occurrences[p][q] += 1
        self._token_to_tokens_occurrences[q][self._chain_end] += 1

    def generate(self, n, random_init=False, smart_ending=False):
        res = list()
        current_token = random.choice(list(self._token_to_tokens_occurrences)) if random_init else self._chain_start

        for _ in range(n):
            current_token = self._generate_next_token(self._token_to_tokens_occurrences[current_token])
            if current_token == self._chain_end:
                if smart_ending:
                    break
                else:
                    current_token = self._choose_random_token(list(self._token_to_tokens_occurrences))
            res.append(current_token)
        return res


class OrdinalMarkovModel(BaseMarkov):
    _ordinal_tokens_occurrences = [defaultdict(Counter)]

    def add_one(self, iterable):
        iterable = iter(iterable)
        peek = next(iterable)
        idx = 0
        self._ordinal_tokens_occurrences[idx][self._chain_start][peek] += 1
        iterable = chain([peek], iterable)
        for p, q in OrdinalMarkovModel._pair(iterable):
            idx += 1
            if len(self._ordinal_tokens_occurrences) < idx + 1:
                self._ordinal_tokens_occurrences.append(defaultdict(Counter))
            self._ordinal_tokens_occurrences[idx][p][q] += 1
        self._ordinal_tokens_occurrences.append(defaultdict(Counter))
        self._ordinal_tokens_occurrences[idx+1][q][self._chain_end] += 1

    def generate(self, n, smart_ending=True):
        res = list()
        current_token = self._chain_start

        for idx in range(n):
            current_token = self._generate_next_token(self._ordinal_tokens_occurrences[idx][current_token])
            if current_token == self._chain_end:
                if smart_ending:
                    break
                else:
                    random_idx = random.randint(0, len(self._ordinal_tokens_occurrences))
                    current_token = self._choose_random_token(list(self._ordinal_tokens_occurrences[random_idx]))
            res.append(current_token)
        return res
