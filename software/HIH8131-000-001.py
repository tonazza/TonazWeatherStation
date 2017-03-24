import spidev
import time


spi = spidev.SpiDev() # create spi object
spi.open(0, 0) # open spi port 0, device (CS) 0

try:
    while True:
        risposta= spi.readbytes(1)
        time.sleep(0.2)
        risposta= spi.readbytes(4)
        if (risposta[0]<64) :
            lettura_rh=risposta[1]+256*risposta[0]
            lettura_T=int(risposta[3]/4)+risposta[2]*64
        else:
            lettura_rh=0
            lettura_T=0
         #end if   
        rh= round(lettura_rh*100/16382, 1)
        T= round(-40+lettura_T*165/16382, 1)
        print ("{}% {}°C".format(rh, T))
        time.sleep(0.8) # sleep 
    #end while
except KeyboardInterrupt: # Ctrl+C pressed, so…
    spi.close() # … close the port before exit
#end try

