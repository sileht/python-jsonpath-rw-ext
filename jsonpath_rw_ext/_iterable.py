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


class SortedThis(jsonpath_rw.This):
    """The JSONPath referring to the sorted version of the current object.

    Concrete syntax is '`sorted`'.
    """

    def find(self, datum):
        """Return sorted value of This if list or dict."""
        if isinstance(datum.value, dict) or isinstance(datum.value, list):
            return [jsonpath_rw.DatumInContext.wrap(value)
                    for value in sorted(datum.value)]
        return datum


class Len(jsonpath_rw.JSONPath):
    """The JSONPath referring to the len of the current object.

    Concrete syntax is '`len`'.
    """

    def find(self, datum):
        datum = jsonpath_rw.DatumInContext.wrap(datum)
        try:
            value = len(datum.value)
        except TypeError:
            return []
        else:
            return [jsonpath_rw.DatumInContext(value,
                                               context=None,
                                               path=Len())]

    def __eq__(self, other):
        return isinstance(other, Len)

    def __str__(self):
        return '`len`'

    def __repr__(self):
        return 'Len()'
