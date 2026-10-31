#!/usr/bin/env bash
# 使い方: ./deploy.sh <元のhakozume.html> "コミットメッセージ"
set -euo pipefail
cd "$(dirname "$0")"
[ -n "${1:-}" ] && python3 build.py "$1"
git add -A
git diff --cached --quiet && { echo "変更なし"; exit 0; }
git commit -q -m "${2:-更新}"
git push -q origin HEAD:main
echo "push完了: $(git rev-parse --short HEAD)"
