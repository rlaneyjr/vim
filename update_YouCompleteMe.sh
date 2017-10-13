#!/bin/sh

# YouCompleteMe Update
git submodule update --init --recursive
# Re-compile YCM
plugged/YouCompleteMe/install.py --clang-completer --go-completer --js-completer
