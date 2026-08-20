#!/bin/sh

# `yt-dlp` helper wrappers.
# https://github.com/yt-dlp/yt-dlp
#
# Arguments: [command to run [arguments...]]

# /// script
# dependencies = [
#   # https://github.com/yt-dlp/yt-dlp/blob/master/Changelog.md
#   "yt-dlp==2026.8.19",
# ]
# ///

# TODO refactor
# TODO error handling
# TODO test (+ shellcheck)
# TODO document (+ dependencies + setup)
# TODO logging (+ syslog)
# TODO check https://github.com/TheFrenchGhosty/TheFrenchGhostys-Ultimate-YouTube-DL-Scripts-Collection

set -o errexit -o nounset

yt() {
    yt-dlp "$@"
}

yt_defaults() {
    yt \
        --mtime \
        --no-part \
        --windows-filenames \
        --embed-subs \
        --embed-metadata \
        --embed-thumbnail \
        --format 'bestvideo[height<=?720]+bestaudio/best' \
        "$@"
}

yt_non_live() {
    yt_defaults \
        --output-na-placeholder not_live \
        --match-filter live_status=not_live \
        "$@"
}

# Arguments: URL
# Exit: 0 if live, 1 otherwise
# TODO merge into `yt_defaults` using post-processing filters?
#  - Plugins: https://github.com/yt-dlp/yt-dlp#plugins
#  - `--exec` / post-processing: https://github.com/yt-dlp/yt-dlp#post-processing-options
yt_is_livestream() {
    # Some upcoming livestreams don't have a video format available yet,
    # so ignore related warnings and errors.
    # https://github.com/jmbannon/ytdl-sub/issues/1323
    yt \
        --no-warnings \
        --ignore-no-formats-error \
        --output-na-placeholder not_live \
        --print live_status \
        "$1" \
    | grep --quiet --invert-match --ignore-case --fixed-strings not_live
}

if [ $# -gt 0 ]; then
    "$@"
fi
