import psutil

batt = psutil.sensors_battery()



print(batt.percent)
print(batt.power_plugged)