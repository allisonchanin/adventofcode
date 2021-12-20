# Allison Chanin
# advent of code day #1

def main ():
	with open ("oceandepth.txt") as file:
		measurements = file.readlines()
		print (measuring(measurements))

def measuring (measurements):
	previous_measurement = int(measurements[0])
	amount_larger_than_previous = 0
	for measurement in measurements:
		if int(measurement) > previous_measurement:
			amount_larger_than_previous +=1
		previous_measurement = int(measurement)
	return amount_larger_than_previous

main()