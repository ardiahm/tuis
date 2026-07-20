import psutil

percent = psutil.disk_usage("/Users/ahmed.1196").percent

print(percent)