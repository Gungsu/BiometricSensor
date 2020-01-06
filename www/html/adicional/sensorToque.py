import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 13

#while True: # Run forever
#    if GPIO.input(13) == GPIO.HIGH:
#        print("Button was pushed!")

count = 0

def button_callback(channel):
	global count
	print("Button was pushed!",str(count))
	count += 1

GPIO.add_event_detect(13,GPIO.RISING,callback=button_callback)

message = input("Press enter to quit\n\n") # Run until someone presses enter
GPIO.cleanup() # Clean up
