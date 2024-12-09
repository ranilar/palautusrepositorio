from matchers import *


class QueryBuilder:
    def __init__(self, matchers=None):
        if matchers:
            self._matchers = matchers
        else: self._matchers = []

    def build(self):
        if not self._matchers:
            return All()
        else: return And(*self._matchers)

    def has_at_least(self, value, attr):
        return QueryBuilder(self._matchers + [HasAtLeast(value, attr)])

    def has_fewer_than(self, value, attr):
        return QueryBuilder(self._matchers + [HasFewerThan(value, attr)])

    def plays_in(self, team):
        return QueryBuilder(self._matchers + [PlaysIn(team)])

    def one_of(self, *matchers):
        return QueryBuilder(self._matchers + [Or(*matchers)])
            