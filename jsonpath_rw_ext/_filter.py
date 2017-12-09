#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import jsonpath_rw
import operator
import re
from six import moves


OPERATOR_MAP = {
    '!=': operator.ne,
    '==': operator.eq,
    '=': operator.eq,
    '<=': operator.le,
    '<': operator.lt,
    '>=': operator.ge,
    '>': operator.gt,
    '~': lambda s, pat: re.match(pat, s)
}


class Filter(jsonpath_rw.JSONPath):
    """The JSONQuery filter"""

    def __init__(self, expressions):
        self.expressions = expressions

    def find(self, datum):
        if not self.expressions:
            return datum

        datum = jsonpath_rw.DatumInContext.wrap(datum)
        if not isinstance(datum.value, list):
            return []

        return [jsonpath_rw.DatumInContext(datum.value[i],
                                           path=jsonpath_rw.Index(i),
                                           context=datum)
                for i in moves.range(0, len(datum.value))
                if (len(self.expressions) ==
                    len(list(filter(lambda x: x.find(datum.value[i]),
                                    self.expressions))))]

    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.expressions)

    def __str__(self):
        return '[?%s]' % self.expressions


class Expression(jsonpath_rw.JSONPath):
    """The JSONQuery expression"""

    def __init__(self, target, op, value):
        self.target = target
        self.op = op
        self.value = value

    def find(self, datum):
        datum = self.target.find(jsonpath_rw.DatumInContext.wrap(datum))

        if not datum:
            return []
        if self.op is None:
            return datum

        found = []
        for data in datum:
            value = data.value
            if isinstance(self.value, int):
                try:
                    value = int(value)
                except ValueError:
                    continue
            elif isinstance(self.value, bool):
                try:
                    value = bool(value)
                except ValueError:
                    continue

            if OPERATOR_MAP[self.op](value, self.value):
                found.append(data)

        return found

    def __eq__(self, other):
        return (isinstance(other, Filter) and
                self.target == other.target and
                self.op == other.op and
                self.value == other.value)

    def __repr__(self):
        if self.op is None:
            return '%s(%r)' % (self.__class__.__name__, self.target)
        else:
            return '%s(%r %s %r)' % (self.__class__.__name__,
                                     self.target, self.op, self.value)

    def __str__(self):
        if self.op is None:
            return '%s' % self.target
        else:
            return '%s %s %s' % (self.target, self.op, self.value)
