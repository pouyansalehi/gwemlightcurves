import numpy as np

# dicvar = {}
# dicvar['hello'] = {}
# dicvar['goodbye'] = {}
# dicvar['hello']['hi'] = 3
# dicvar['goodbye']['bye'] = 4
# print(list(dicvar.keys()))

# x = numpy.array([1,0,2,0,3,0,4,5,6,7,8])
# y = numpy.where(x == 0)[2]
# print (y)

lines = [line.rstrip('\n') for line in open('Micheal Homeworks/08/data/GW170817.dat')]
print (lines )

p = np.append([[1, 2, 3], [4, 5, 6]], [[7, 8, 9]],axis=2)
print (p)