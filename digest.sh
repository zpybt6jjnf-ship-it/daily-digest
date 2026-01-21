#!/bin/bash
# Daily Digest helper script
#
# WORKFLOW:
#   1. ./digest.sh copy     - Copy content prompt, open Claude.ai
#   2. Paste prompt, get structured content back
#   3. Save content to a .txt file (e.g., content.txt)
#   4. ./digest.sh build content.txt  - Generate branded HTML
#   5. ./digest.sh view     - Preview in browser
#
# Commands:
#   copy   - Copy content prompt to clipboard, open Claude.ai
#   build  - Convert content file to branded HTML
#   view   - View latest digest in browser
#   send   - Build, commit, push (triggers email)
#   auto   - Full automation: research, build, send (via Claude Code)
#   help   - Show this help

cd "$(dirname "$0")"

case "${1:-help}" in
  copy)
    cat prompts-and-instructions/content-prompt.md | pbcopy
    echo "Content prompt copied to clipboard!"
    echo ""
    echo "Opening Claude.ai..."
    open "https://claude.ai/new"
    echo ""
    echo "WORKFLOW:"
    echo "  1. Paste the prompt (Cmd+V) in Claude.ai"
    echo "  2. Copy the structured content output"
    echo "  3. Save to a file: pbpaste > content.txt"
    echo "  4. Build HTML: ./digest.sh build content.txt"
    echo "  5. Preview: ./digest.sh view"
    ;;

  build)
    if [ -z "$2" ]; then
      echo "Usage: ./digest.sh build <content-file>"
      echo ""
      echo "Example: ./digest.sh build content.txt"
      echo ""
      echo "The content file should contain the structured output from Claude.ai"
      exit 1
    fi

    if [ ! -f "$2" ]; then
      echo "Error: File not found: $2"
      exit 1
    fi

    python3 build_digest.py "$2"
    echo ""
    echo "Run './digest.sh view' to preview"
    ;;

  view)
    FILE=$(ls -t digests/energy-digest-*.html 2>/dev/null | head -1)
    if [ -n "$FILE" ]; then
      open "$FILE"
      echo "Opened: $FILE"
    else
      echo "No HTML digest found in digests/"
      echo "Run './digest.sh build <content-file>' first"
    fi
    ;;

  send)
    # Build if content file provided
    if [ -n "$2" ]; then
      if [ ! -f "$2" ]; then
        echo "Error: File not found: $2"
        exit 1
      fi
      echo "Building digest..."
      python3 build_digest.py "$2"
    fi

    # Get latest digest
    FILE=$(ls -t digests/energy-digest-*.html 2>/dev/null | head -1)
    if [ -z "$FILE" ]; then
      echo "Error: No digest found. Run './digest.sh build <content-file>' first"
      exit 1
    fi

    echo "Sending: $FILE"
    git add "$FILE"
    git commit -m "Add $(basename "$FILE" .html | sed 's/energy-digest-//' ) digest"
    git push

    echo ""
    echo "Pushed! Email will arrive shortly."
    echo "Check: https://github.com/zpybt6jjnf-ship-it/daily-digest/actions"
    ;;

  auto)
    echo "🚀 Starting automated digest generation..."
    echo ""

    # Run content prompt via Claude Code
    echo "Step 1/3: Running content prompt via Claude Code..."
    claude --print "Run the content prompt in prompts-and-instructions/content-prompt.md in full. Save the structured output to content.txt. Do not ask questions, just execute." > /dev/null 2>&1

    if [ ! -f "content.txt" ]; then
      echo "Error: content.txt was not created"
      exit 1
    fi

    echo "Step 2/3: Building HTML digest..."
    python3 build_digest.py content.txt

    echo "Step 3/3: Pushing to GitHub..."
    FILE=$(ls -t digests/energy-digest-*.html 2>/dev/null | head -1)
    git add "$FILE"
    git commit -m "Add $(basename "$FILE" .html | sed 's/energy-digest-//') digest"
    git push

    echo ""
    echo "✅ Done! Email will arrive shortly."
    echo "Check: https://github.com/zpybt6jjnf-ship-it/daily-digest/actions"
    ;;

  help|--help|-h|"")
    echo "Daily Digest Helper"
    echo ""
    echo "WORKFLOW:"
    echo "  1. ./digest.sh copy          Copy prompt, open Claude.ai"
    echo "  2. Paste prompt, get content back"
    echo "  3. Save content: pbpaste > content.txt"
    echo "  4. ./digest.sh build content.txt   Generate HTML"
    echo "  5. ./digest.sh view          Preview in browser"
    echo ""
    echo "COMMANDS:"
    echo "  auto              Full automation (Claude Code → build → email)"
    echo "  copy              Copy content prompt to clipboard"
    echo "  build <file>      Convert content file to branded HTML"
    echo "  view              Open latest digest in browser"
    echo "  send [file]       Build (optional), commit, push, email"
    echo "  help              Show this help"
    ;;

  *)
    echo "Unknown command: $1"
    echo "Run './digest.sh help' for usage"
    exit 1
    ;;
esac
