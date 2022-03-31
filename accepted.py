'''init string array'''
inputString = "150-177-154-156-149-223-157-144-197-223-214"

strint_array = inputString.split("-")
''' list of strings to int array'''
int_array = list(map(int, strint_array))

print(int_array)
'''subtract a number of each element in the array'''
for i in range(len(int_array)):
    int_array[i] = 255 - int_array[i]

print(int_array)
'''convert int array to ascii representation'''
ascii_array = list(map(chr, int_array))

print(ascii_array)
'''swap every item in ascii_array with the next item'''
for i in range(0, len(ascii_array) - 1, 2):
    ascii_array[i], ascii_array[i + 1] = ascii_array[i + 1], ascii_array[i]

print(ascii_array)
'''convert ascii array to string'''
outputString = ''.join(ascii_array)

print(outputString)
