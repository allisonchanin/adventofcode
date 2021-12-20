# Allison Chanin
# advent of code day #1

def main ():
	with open ("oceandepth.txt") as file:
		measurements = file.readlines()
		sums = summing(measurements)
		print (measuring(sums))

def summing (measurements):
	sums = []
	for i in range (len(measurements)-2):
		summed = int(measurements[i])+int(measurements[i+1])+int(measurements[i+2])
		sums.append(summed)
	return sums

def measuring (values):
	previous_measurement = int(values[0])
	amount_larger_than_previous = 0
	for value in values:
		if int(value) > previous_measurement:
			amount_larger_than_previous +=1
		previous_measurement = int(value)
	return amount_larger_than_previous

main()