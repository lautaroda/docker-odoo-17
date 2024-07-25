#!/bin/bash

set -e

python3 wait-for-psql.py

exec "$@"
