import import_file

# raspberrypi function not in use

#grovepi.set_ubs("RPI_1")

def set_button(port):
    grovepi.pinMode(port, "INTPUT")

def check_button_port():
    port = 0
    return grovepi.digitalRead(port)