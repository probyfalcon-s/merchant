#!/bin/bash
set -e  # Exit on first fail
export PYTHONUNBUFFERED=0

case "$1" in
    test)
        source /app/venv/bin/activate
        #flake8 --max-line-length 120 --max-cognitive-complexity=110 src
        pytest -sv tests
    ;;
    *)
        $@
    ;;
esac
