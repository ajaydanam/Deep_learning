import numpy as np

x = np.random.uniform(1, 20, 20)
print("Original Array: ", x)

newarr = x.reshape(4, 5)
print("\nReshaped Array: ", newarr)

max_values = np.amax(newarr, axis=1).reshape(-1, 1)
newarr1 = np.where(newarr == max_values, 0, newarr)
print("\nArray after replacing the maximum in each row by 0:", newarr1)


