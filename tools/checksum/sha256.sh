#!/usr/bin/env sh
set -eu

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 <file>" >&2
  exit 1
fi

sha256sum "$1"
