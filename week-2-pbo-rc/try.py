# class AbsString:
# 	def __init__(self, value):
# 		self.value = value 

# 	def __abs__(self):
# 		absolute = self.value.replace("negative", "")
# 		return absolute

# string = AbsString("negative ten")
# print(abs(string))

import random

# List contoh
data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Memilih dua data acak dari list
random_data = random.sample(data_list, 2)

print("Data acak yang dipilih:", random_data)