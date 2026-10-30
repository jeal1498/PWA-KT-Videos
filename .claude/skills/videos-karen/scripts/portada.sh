#!/bin/bash
# Uso: portada.sh <trabajo> [portada.html] — saca portada.png (1080x1920) del HTML con Playwright.
# Para v2 sin cara. Las portadas con foto de Karen siguen con portada.py.
set -e
W="$(realpath "$1")"; H="$(realpath "${2:-$W/portada.html}")"
node -e "const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:1080,height:1920}});await p.goto('file://'+process.argv[1]);await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(300);await p.screenshot({path:process.argv[2]});await b.close();})()" "$H" "$W/portada.png"
echo "portada → $W/portada.png"
