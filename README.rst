===============================
python-jsonpath-rw-ext
===============================

.. image:: https://travis-ci.org/sileht/python-jsonpath-rw-ext.png?branch=master
   :target: https://travis-ci.org/sileht/python-jsonpath-rw-ext

.. image:: https://img.shields.io/pypi/v/jsonpath-rw-ext.svg
   :target: https://pypi.python.org/pypi/jsonpath-rw-ext/
   :alt: Latest Version

.. image:: https://img.shields.io/pypi/dm/jsonpath-rw-ext.svg
   :target: https://pypi.python.org/pypi/jsonpath-rw-ext/
   :alt: Downloads

Extensions for JSONPath RW

jsonpath-rw-ext extends json-path-rw capabilities by adding multiple extensions.
'len' that allows one to get the length of a list. 'sorted' that returns a sorted version
of a list, 'arithmetic' that permits one to make math operation between elements and
'filter' to select only certain elements of a list.

Each extensions will be proposed `upstream <https://github.com/kennknowles/python-jsonpath-rw>`__
and will stay here only if they are refused.

* Free software: Apache license
* Documentation: https://python-jsonpath-rw-ext.readthedocs.org/en/latest/
* Source: http://github.com/sileht/python-jsonpath-rw-ext


Quick Start
-----------

At the command line::

    $ pip install jsonpath-rw-ext

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv jsonpath-rw-ext
    $ pip install jsonpath-rw-ext


To replace the jsonpath_rw parser by this one with::

    import jsonpath_rw_ext
    jsonpath_rw_ext.parse("$.foo").find(...)

Or::

    from jsonpath_rw_ext import parser
    parser.ExtentedJsonPathParser().parse("$.foo").find(...)


Shortcut functions for getting only the matched values::

    import jsonpath_rw_ext as jp
    print jp.match('$.cow[*]', {'cow': ['foo', 'bar'], 'fish': 'foobar'})
    # prints ['foo', 'bar']

    print jp.match1('$.cow[*]', {'cow': ['foo', 'bar'], 'fish': 'foobar'})
    # prints 'foo'

The jsonpath classes are not part of the public API, because the name/structure
can change when they will be implemented upstream. Only the syntax *shouldn't*
change.

Extensions
----------

+--------------+----------------------------------------------+
| name         | Example                                      |
+==============+==============================================+
| len          | - $.objects.`len`                            |
+--------------+----------------------------------------------+
| sub          | - $.field.`sub(/foo\\\\+(.*)/, \\\\1)`       |
+--------------+----------------------------------------------+
| split        | - $.field.`split(+, 2, -1)`                  |
|              | - $.field.`split(sep, segement, maxsplit)`   |
+--------------+----------------------------------------------+
| sorted       | - $.objects.`sorted`                         |
|              | - $.objects[\\some_field]                    |
|              | - $.objects[\\some_field,/other_field]       |
+--------------+----------------------------------------------+
| filter       | - $.objects[?(@some_field > 5)]              |
|              | - $.objects[?some_field = "foobar")]         |
|              | - $.objects[?some_field ~ "regexp")]         |
|              | - $.objects[?some_field > 5 & other < 2)]    |
+--------------+----------------------------------------------+
| arithmetic   | - $.foo + "_" + $.bar                        |
| (-+*/)       | - $.foo * 12                                 |
|              | - $.objects[*].cow + $.objects[*].cat        |
+--------------+----------------------------------------------+

About arithmetic and string
---------------------------

Operations are done with python operators and allows types that python
allows, and return [] if the operation can be done due to incompatible types.

When operators are used, a jsonpath must be be fully defined otherwise
jsonpath-rw-ext can't known if the expression is a string or a jsonpath field,
in this case it will choice string as type.

Example with data::

    {
        'cow': 'foo',
        'fish': 'bar'
    }

| **cow + fish** returns **cowfish**
| **$.cow + $.fish** returns **foobar**
| **$.cow + "_" + $.fish** returns **foo_bar**
| **$.cow + "_" + fish** returns **foo_fish**

About arithmetic and list
-------------------------

Arithmetic can be used against two lists if they have the same size.

Example with data::

    {'objects': [
        {'cow': 2, 'cat': 3},
        {'cow': 4, 'cat': 6}
    ]}

| **$.objects[\*].cow + $.objects[\*].cat** returns **[6, 9]**

