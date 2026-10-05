import numpy as np

array = np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                 [['I','J','K'],['L','M','N'],['O','P','Q']],
                 [['R','S','T'],['U','V','W'],['X','Y','Z']]])

a = array[2,0,1] + array[2,0,1] + array[0,1,1]
print(a)