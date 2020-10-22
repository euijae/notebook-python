
'''
import sys
sys.path.append('../')

from utility import divider
'''

for i in range(1, 11):
    if i % 2 == 0:
        print(i, " is even")
    else:
        print(i, " is odd")

for i in range(1, 11, 3):
    print(i)

float_list = [2.5, 16.42, 10.77, 8.3, 34.21]
print(float_list)

for i in range(0, len(float_list)):
    float_list[i] *= 2

print(float_list)
