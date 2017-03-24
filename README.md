# TonazWeatherStation
Indoor weather station based on Raspberry Pi 2 model B

**2017/3/23**
Initial upload of the files.
Still NOT working, just a work in progress.


PROJECT DESCRIPTION
This is a Weather Station, conceived for measuring air properties in an indoor environment.

The main components are:

**Raspberry Pi 2 Model B** Single board computer
https://www.raspberrypi.org/products/raspberry-pi-2-model-b/

**MIDAS MC21605G12W-VNMLWI** LCD 16x2 chars I2C module, white on black
http://it.farnell.com/midas/mc21605g12w-vnmlwi/lcd-alpha-num-16-x-2-white/dp/2425704

**HONEYWELL HIH8131-000-001** humidity and temperature sensor
http://www.mouser.it/Search/ProductDetail.aspx?R=HIH8131-000-001virtualkey67850000virtualkey785-HIH8131-000-001

**MEASUREMENT SPECIALTIES MS580502BA01-50** barometric pressure sensor
http://www.mouser.it/Search/ProductDetail.aspx?R=MS580502BA01-50virtualkey53710000virtualkey824-MS580502BA01-50

The hardware project(Pi HAT + connection boards) was made using EAGLE CAD 6.5.

The software was made in Python 3, to be run on the Raspberry Pi equipped with Raspbian minimal on a 4GB uSD card.