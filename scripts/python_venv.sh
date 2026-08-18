#!/bin/sh

# Runs a command within the local venv.
#
# Arguments: [pass-through]

set -o errexit -o nounset

SCRIPTS_PATH="$(dirname "$(realpath -e "$0")")/"
VENV_PATH="$SCRIPTS_PATH/../.venv/"

# shellcheck disable=SC1090
. "$VENV_PATH/bin/activate"

"$@"
