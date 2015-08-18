# -*- coding: utf-8 -*-

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

"""
test_jsonpath_rw_ext
----------------------------------

Tests for `jsonpath_rw_ext` module.
"""

from jsonpath_rw import jsonpath  # For setting the global auto_id_field flag
from oslotest import base
import testscenarios

from jsonpath_rw_ext import parser


class TestJsonpath_rw_ext(testscenarios.WithScenarios,
                          base.BaseTestCase):
    scenarios = [
        ('sorted_list', dict(string='objects.`sorted`',
                             data={'objects': ['alpha', 'gamma', 'beta']},
                             target=['alpha', 'beta', 'gamma'])),
        ('sorted_dict', dict(string='objects.`sorted`',
                             data={'objects': {'cow': 'moo', 'horse': 'neigh',
                                               'cat': 'meow'}},
                             target=['cat', 'cow', 'horse'])),
        ('len_list', dict(string='objects.`len`',
                          data={'objects': ['alpha', 'gamma', 'beta']},
                          target=3)),
        ('len_dict', dict(string='objects.`len`',
                          data={'objects': {'cow': 'moo', 'cat': 'neigh'}},
                          target=2)),
        ('len_str', dict(string='objects[0].`len`',
                         data={'objects': ['alpha', 'gamma']},
                         target=5)),
        ('filter_exists_syntax1', dict(string='objects[?cow]',
                                       data={'objects': [{'cow': 'moo'},
                                                         {'cat': 'neigh'}]},
                                       target=[{'cow': 'moo'}])),
        ('filter_exists_syntax2', dict(string='objects[?@.cow]',
                                       data={'objects': [{'cow': 'moo'},
                                                         {'cat': 'neigh'}]},
                                       target=[{'cow': 'moo'}])),
        ('filter_exists_syntax3', dict(string='objects[?(@.cow)]',
                                       data={'objects': [{'cow': 'moo'},
                                                         {'cat': 'neigh'}]},
                                       target=[{'cow': 'moo'}])),
        ('filter_eq1', dict(string='objects[?cow="moo"]',
                            data={'objects': [{'cow': 'moo'},
                                              {'cow': 'neigh'},
                                              {'cat': 'neigh'}]},
                            target=[{'cow': 'moo'}])),
        ('filter_eq2', dict(string='objects[?(@.["cow"]="moo")]',
                            data={'objects': [{'cow': 'moo'},
                                              {'cow': 'neigh'},
                                              {'cat': 'neigh'}]},
                            target=[{'cow': 'moo'}])),
        ('filter_gt', dict(string='objects[?cow>5]',
                           data={'objects': [{'cow': 8},
                                             {'cow': 7},
                                             {'cow': 5},
                                             {'cow': 'neigh'}]},
                           target=[{'cow': 8}, {'cow': 7}])),
        ('filter_and', dict(string='objects[?cow>5&cat=2]',
                            data={'objects': [{'cow': 8, 'cat': 2},
                                              {'cow': 7, 'cat': 2},
                                              {'cow': 5, 'cat': 3},
                                              {'cow': 8, 'cat': 3}]},
                            target=[{'cow': 8, 'cat': 2},
                                    {'cow': 7, 'cat': 2}])),

    ]

    def test_fields_value(self):
        jsonpath.auto_id_field = None
        result = parser.parse(self.string, debug=True).find(self.data)
        if isinstance(self.target, list):
            self.assertEqual(self.target, [r.value for r in result])
        elif isinstance(self.target, set):
            self.assertEqual(self.target, set([r.value for r in result]))
        elif isinstance(self.target, (int, float)):
            self.assertEqual(self.target, result[0].value)
        else:
            self.assertEqual(self.target, result.value)
