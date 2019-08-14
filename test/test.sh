#!/bin/bash
export PYTHONPATH=$PYTHONPATH:/opt/:/opt/container/
pwd
rm -Rf .htmlcov
coverage run -m py.test test/tests/
SUCCESS=$?
echo ""
coverage report -m
coverage html -d .htmlcov
echo ""
exit $SUCCESS
