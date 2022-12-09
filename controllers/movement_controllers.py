# import RPi.GPIO as GPIO

# GPIO.setwarnings(False)
# GPIO.setmode(GPIO.BCM)
# GPIO.setup(4, GPIO.OUT)
# GPIO.setup(5, GPIO.OUT)


async def left():

        # GPIO.output(4,true)
        return f'left Donzo!'


async def right():

        # GPIO.output(5,true)
        return f'right Donzo!'

async def forward():

        # GPIO.output(5,True)
        return f'forward Donzo!'


        

async def stop():
        # GPIO.output(5,True)
        return f"stop Donzo!"


        



