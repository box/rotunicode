#!/bin/bash

# Originally from
# <https://github.com/pyca/cryptography/blob/d93aa99636b06d5d403130425098b2f0cc1b516e/.travis/install.sh>.

set -e
set -x
set -o pipefail

export PYENV_ROOT="$PWD/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"

if [[ "$(uname -s)" == "Darwin" ]]; then
    eval "$(pyenv init -)"
else
    if [[ "${TOX_ENV}" == "pypy" ]]; then
        eval "$(pyenv init -)"
        pyenv global pypy-2.6.0
    fi
fi
source $PWD/.venv/bin/activate
tox -e $TOX_ENV -- $TOX_FLAGS
