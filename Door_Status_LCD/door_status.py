import I2C_LCD_driver
import board
import busio
import adafruit_ahtx0
from time import sleep, strftime
from datetime import datetime

#  Setup LCDs
mylcd1 = I2C_LCD_driver.lcd(0x27)
mylcd2 = I2C_LCD_driver.lcd(0x26)

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_ahtx0.AHTx0(i2c)

def get_cpu_temp():     # get CPU temperature and store it into file "/sys/class/thermal/thermal_zone0/temp"
    tmp = open('/sys/class/thermal/thermal_zone0/temp')
    cpu = tmp.read()
    tmp.close()
    return '{:.2f}'.format( float(cpu)/1000 ) + ' C'
 
def get_time_now():     # get system time
    return datetime.now().strftime('%H:%M')

mylcd1.backlight(0)
mylcd2.backlight(0)
sleep(1)
mylcd1.backlight(1)
mylcd2.backlight(1)
sleep(1)
mylcd1.backlight(0)
mylcd2.backlight(0)
sleep(1)
mylcd1.backlight(1)
mylcd2.backlight(1)

mylcd1.lcd_clear()
mylcd2.lcd_clear()
mylcd1.lcd_display_string("Naresh's Status:", 1)
mylcd1.lcd_display_string("Working", 2)
mylcd2.lcd_display_string("Naresh's Status:", 1)
mylcd2.lcd_display_string("Working", 2)

i = 0

while True:
    
    # dd/mm/YY H:M:S
    t_string = datetime.now().strftime("%H:%M")
    
    if i == 0:
        # Read Temperature and Humidity
        tmp = "Tmp %0.1f C" % sensor.temperature
        hmd = "Hmd %0.1f %%" % sensor.relative_humidity
        cpu_tmp = get_cpu_temp()
        
        # Display info
        mylcd1.lcd_display_string(tmp, 3)
        mylcd1.lcd_display_string(hmd, 4)
        mylcd1.lcd_display_string(cpu_tmp, 3, 13)
    
    mylcd1.lcd_display_string(t_string, 4, 15)
    
    i += 1
    
    if i == 59:
        i = 0
        
    sleep(1)

