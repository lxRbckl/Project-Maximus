python3 Maximus.py

chromium-browser "http://127.0.0.1:8050"
wmctrl -r Chromium -e 0,1045,-100,0,1080,1080
wmctrl -a Chromium

guvcview
wmctrl -r Guvcview -e 0,-10,-90,1053,900
wmctrl -a guvcview

sleep 10

wmctrl -r Chromium -e 0,1045,-100,0,1080,1080
wmctrl -a Chromium

wmctrl -r Guvcview -e 0,-10,-90,1053,900
wmctrl -a guvcview
