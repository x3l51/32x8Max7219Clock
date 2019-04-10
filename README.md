# 32x8Max7219Clock
Script that is intended to be run in an endless loop to run a clock.

Apply this via `sudo crontab -e`:

`@reboot sleep 20; cd /PATH/TO/SCRIPT && python3 clockMatrix.py`

You can uncomment everything for displaying the devices' IP on boot, for showing the weather and dimming the display automatically.

The max7219 has to be connected as documented [here](https://luma-led-matrix.readthedocs.io/en/latest/install.html#gpio-pin-outs).

The light sensor should be connected as documented [here](https://pimylifeup.com/raspberry-pi-light-sensor/).

For the weather api key, you have to create an account [here](https://home.openweathermap.org/users/sign_up).
