#!/bin/bash

index="/home/george/public_html/isjameswearingashirttoday/public/index.html"

case "$1" in
  yes)
    sed -i '' s/NO/YES/g $index
  ;;

  no)
    sed -i '' s/YES/NO/g $index
  ;;

  *)
    echo "Usage: ./change.sh {yes|no}" >&2
  ;;
esac

