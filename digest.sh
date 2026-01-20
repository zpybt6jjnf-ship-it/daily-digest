#!/bin/bash
# Daily Digest helper script
# Usage: ./digest.sh [command]
#   copy   - Copy prompt to clipboard, open Gemini
#   view   - View latest digest in browser
#   new    - Create today's digest file and open for editing

cd "$(dirname "$0")"

case "${1:-copy}" in
  copy)
    cat prompts-and-instructions/external_use-html-prompt.md | pbcopy
    echo "Prompt copied to clipboard!"
    echo "Opening Gemini..."
    open "https://gemini.google.com/app"
    echo ""
    echo "Next steps:"
    echo "  1. Paste prompt (Cmd+V) in Gemini"
    echo "  2. Copy the HTML output"
    echo "  3. Run: ./digest.sh new"
    ;;
  new)
    FILE="digests/energy-digest-$(date +%Y-%m-%d).html"
    mkdir -p digests
    if [ ! -f "$FILE" ]; then
      touch "$FILE"
    fi
    open "$FILE"
    echo "Opened: $FILE"
    echo "Paste the HTML, save, then run: ./digest.sh view"
    ;;
  view)
    FILE=$(ls -t digests/energy-digest-*.html 2>/dev/null | head -1)
    if [ -n "$FILE" ]; then
      open "$FILE"
      echo "Opened: $FILE"
    else
      echo "No HTML digest found in digests/"
    fi
    ;;
  *)
    echo "Usage: ./digest.sh [copy|new|view]"
    ;;
esac
