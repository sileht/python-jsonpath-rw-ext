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

    $ pip install python-jsonpath-rw-ext

Or, if you have virtualenvwrapper installed::

    $ mkvirtualenv python-jsonpath-rw-ext
    $ pip install python-jsonpath-rw-ext


Extensions
----------

+--------------+-------------------------------+
| name         | Example                       |
+==============+===============================+
| len          | $.objects.`len`               |
+--------------+-------------------------------+
| sorted       | $.objects.`sorted`            |
+--------------+-------------------------------+
| filter       | $.objects[?(@some_field > 5)] |
+--------------+-------------------------------+


