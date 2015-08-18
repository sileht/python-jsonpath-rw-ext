#!/bin/bash

version=$1

git checkout master
git tag -s $version -m "Release version ${version}"
git checkout $version
git clean -fd
rm -rf python_jsonpath_rw_ext.egg-info build dist
tox -evenv python setup.py sdist bdist_wheel


echo "git push --tags"
echo "twine upload -r pypi dist/python-jsonpath-rw-ext-${version}.tar.gz"
