import numpy as R
n=R.array([[1,2,3,4,],[6,7,9,8],[1,2,9,0]])
v=R.array([[[1,2,3,4,],[6,7,9,8],[1,2,9,0]],[[1,2,3,4,],[6,7,9,8],[1,2,9,0]]])
print(v[1,2,0])
print(n.ndim)
print(n[2,3])
print(v[1,1,1:3])
