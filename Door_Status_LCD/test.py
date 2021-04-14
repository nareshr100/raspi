import I2C_LCD_driver

mylcd1 = I2C_LCD_driver.lcd(0x27)
mylcd1.lcd_display_string("Naresh's Status:", 1)