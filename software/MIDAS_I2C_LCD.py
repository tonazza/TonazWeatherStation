# -*- coding: utf-8 -*-
#!/usr/bin/python
"""
#created by Tonazza for display MIDAS MC21605G12W-VNMLWI
# 2017-03-08
"""

# i2c bus (0 -- original Pi, 1 -- Rev 2 Pi)
I2CBUS = 1

# LCD Address
#ADDRESS = 0x78
ADDRESS = 0x3C

#delay between commands
CMD_DELAY=0.0002

""""
# COMANDI COMPLETI

LCD_CLEARDISPLAY = 0x01

LCD_RETURNHOME = 0x02

LCD_ENTRYMODESET = 0x04
# flags for display entry mode
LCD_ENTRY_INCREMENT_SHIFT_L = 0x02
LCD_ENTRY_DECREMENT_SHIFT_R = 0x00
LCD_ENTRY_SHIFT = 0x01
LCD_ENTRY_NOSHIFT = 0x00

LCD_DISPLAYCONTROL = 0x08
# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

LCD_CURSORSHIFT = 0x10
# flags for display/cursor shift
LCD_DISPLAYSHIFT = 0x08
LCD_CURSORSHIFT = 0x00
LCD_SHIFTRIGHT = 0x04
LCD_SHIFTLEFT = 0x00

LCD_FUNCTIONSET = 0x20
# flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x11DOTS = 0x04
LCD_5x8DOTS = 0x00

LCD_SETCGRAMADDR = 0x40

LCD_SETDDRAMADDR = 0x80

"""

# comandi rapidi
CMD_CLEAR_DISPLAY = 0x01
CMD_RETURNHOME = 0x02
CMD_FUNCTION_SET_INIZIALE = 0x38
CMD_CURSOR_SHIFT_RIGHT = 0x14
CMD_DISPLAY_ON = 0x0C

REGMODE1 = 0x00 #preambolo per i comandi
CHARMODE = 0x40 #preambolo per i caratteri

import smbus
from time import sleep

bus = smbus.SMBus(I2CBUS)    # 0 = /dev/i2c-0 (port I2C0), 1 = /dev/i2c-1 (port I2C1)

def LCD_DDRAM_ADDRESS(line=1, pos=0):
    if line == 1:
      pos_new = pos
    elif line == 2:
      pos_new = 0x40 + pos
    return (0x80 + pos_new)

def scrivi_comando(comando):
    bus.write_byte_data(ADDRESS, REGMODE1, comando)
    sleep(CMD_DELAY)

def scrivi_carattere(carattere):
    bus.write_byte_data(ADDRESS, CHARMODE, carattere)
    sleep(CMD_DELAY)

def posiziona_cursore(riga, colonna):
    scrivi_comando(LCD_DDRAM_ADDRESS(riga, colonna-1))
    
def scrivi_stringa(stringa):
    for char in stringa:
      scrivi_carattere(ord(char))
      
def inizializza():
    scrivi_comando(CMD_FUNCTION_SET_INIZIALE)
    scrivi_comando(CMD_CURSOR_SHIFT_RIGHT)
    scrivi_comando(CMD_DISPLAY_ON)
    scrivi_comando(CMD_CLEAR_DISPLAY)
    posiziona_cursore(1, 1)

#test del display

inizializza()
scrivi_stringa("...finalmente...")
posiziona_cursore(2, 1)
scrivi_stringa("...FUNZIONA!!!!!")
