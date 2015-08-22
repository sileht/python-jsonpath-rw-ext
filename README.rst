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

This extensions will be proposed `upstream <https://github.com/kennknowles/python-jsonpath-rw>`__
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


Extensions
----------

+--------------+----------------------------------------------+
| name         | Example                                      |
+==============+==============================================+
| len          | - $.objects.`len`                            |
+--------------+----------------------------------------------+
| sorted       | - $.objects.`sorted`                         |
|              | - $.objects[\\some_field]                    |
|              | - $.objects[\\some_field,/other_field]       |
+--------------+----------------------------------------------+
| filter       | - $.objects[?(@some_field > 5)]              |
|              | - $.objects[?some_field = "foobar")]         |
|              | - $.objects[?some_field > 5 & other < 2)]    |
+--------------+----------------------------------------------+
| arithmetic   | - $.foo + "_" + $.bar                        |
| (-+*/)       | - $.foo * 12                                 |
|              | - $.objects[*].cow + $.objects[*].cat        |
+--------------+----------------------------------------------+

About arithmetic and string
---------------------------

Operations are done with python operators and allows types that python
allows, and return None if the operation can be done due to imcompatible types.

When operators are used, a jsonpath must be be fully defined otherwise
if jsonpath-rw-ext can't known if expression is a string or a jsonpath field,
it will choice string.

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

Arithmetic can be used against two list if they have the same size.

Example with data::

    {'objects': [
        {'cow': 2, 'cat': 3},
        {'cow': 4, 'cat': 6}
    ]}

| **$.objects[\*].cow + $.objects[\*].cat** returns **[6, 9]**

