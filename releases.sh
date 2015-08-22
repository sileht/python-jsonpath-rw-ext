#!/bin/bash

version=$1

git checkout master
git tag -s $version -m "Release version ${version}"
git checkout $version
git clean -fd
rm -rf jsonpath_rw_ext.egg-info build dist
tox -epep8,py27,py34
tox -r -evenv python setup.py sdist bdist_wheel

echo "release: jsonpath-rw-ext ${version}"
echo
echo "SHA1sum: "
sha1sum dist/*
echo "MD5sum: "
md5sum dist/*

echo 
echo "To publish:"
echo
echo "* git push --tags"
echo "* twine upload -r pypi -s dist/jsonpath-rw-ext-${version}.tar.gz dist/jsonpath_rw_ext-${version}-py2.py3-none-any.whl"
