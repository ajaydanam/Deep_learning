list_heights = []
heights_in_cm = []
while True:
    height1 = input("Enter heights of customers(inches) (press x to quit):")
    if height1 == 'x':
        break
    else:
        list_heights.append(height1)
    
print("L1: ",list_heights)
heights_in_cm = [int(height) * 2.54 for height in list_heights]
print("Output: ", heights_in_cm)


