import os

def read_temp():
	filepath = "/sys/class/thermal/thermal_zone0/temp"
	with open(filepath, "r") as f:
		temp = int(f.read())/1000
		return temp

print(read_temp(), "C")
