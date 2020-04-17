#!/bin/zsh
while inotifywait -e close_write scripts simulador.py; do clear && mypy --ignore-missing-imports scripts simulador.py && flake8 --ignore=E501 scripts simulador.py; done
