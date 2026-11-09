#!/bin/sh
R=/Users/kk/Documents/VLProjects/Matrix-Video-Recording
export PW_DIR=/Users/kk/Documents/VL-Release-Worktrees/core177-codehub/core-source/workbenches/build/VLCode-2.0/node_modules/playwright
cd $R/rec
for CB in "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" "/Users/kk/Library/Caches/ms-playwright/chromium-1194/chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing" "/Users/kk/Library/Caches/ms-playwright/chromium_headless_shell-1194/chrome-mac-arm64/headless_shell"; do
  [ -x "$CB" ] || { echo "skip $CB"; continue; }
  echo "=== try $CB"
  CHROME_BIN="$CB" node record-huzhou.cjs && { echo "=== ok with $CB"; exit 0; }
  echo "=== failed with $CB"
done
echo "=== all failed"; exit 1
