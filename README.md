## Project-Maximus
> Get the live feed of a USB camera and interact with GPIO pins with a Dash UI.

### Installation
```
# USB Camera
# Raspberry Pi 4
# Raspberry Pi OS

pip3 install RPi
pip3 install dash
pip3 install dash_daq
sudo apt-get -y install python3-rpi.gpio

cd
git clone https://github.com/lxRbckl/Project-Maximus.git

# Run the following command if you haven't
# used at-desktop loaded commands before:
cp -r /etc/xdg/lxsession ~/.config

cd /home/pi/.config/lxsession/LDXE-pi
nano autostart

@bash ~/Project-Maximus/Maximus.sh

crontab -e
@reboot ~/Project-Maximus/Maximus.py
```
