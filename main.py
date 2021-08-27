numpy is faster than lists.
computers sees any number in binary fromat
it stores the int in 4 bytes ex : 5--> 00000000 00000000 00000000 00000101
list is an built in int type for python it consists of 1) size -- 4 bytes
                                                       2) reference count -- 8 bytes
                                                       3) object typye -- 8 bytes
                                                       4) object value -- 8 bytes
since numpy uses less bytes of memory it is faster than lists.

Another reason for numpy is faster than list is it uses contiguous memory. contiguous memory -- continues memory.
benefits :
->SIMD Vector processing
SIMD-Single Instruction Multiple Data.
->Effective cache utilization


lists                   |                     numpy
                        |
-> List can perform     |-> Numpy can perforn insertion  Deletion
insertion,delection     |    , appending , concatenation etc. we can perform lot more actions here.
appending,concatenation |
ex :                    | ex :
	a=[1,3,5]       |       import numpy as np
	b=[1,2,3]       |       a=np.array([1,3,5])
  	a*b = ERROR     |       b=np.array([1,2,3])
                        |       c=a*b
                        |       print(c)
                        |
                        |   o/p : [1,6,15]

Applications of Numpy?
-> we can do maths with numpy. (MATLAB Replacement)
-> Plotting (Matplotlib)
-> Backend ( Pandas , Connect4 , Digital Photography)
-> Machine Learing.



Codes.
1) input

import numpy as np

a=np.array([1,2,3])
print(a)

1) o/p

[1 2 3]  (one dimentional array)

2) input

b=np.array([[9.0,3.9,4],[6.0,5.0,4.0]])
print(b)

2) 0/p
[[9.  3.9 4. ]              ( both the array inside must be equal or else it will give error )
 [6.  5.  4. ]]  --> Two dimentional array.

3) input

#To get dimension.

->print(a.ndim)

n-number,dim-dimention

3) o/p

1

4) input

# To get shape.

print(b.shape)
print(a.shape)

4) o/p

(2, 3) # { 2 rows and 3 columns }
(3,)   # { 1 row and 3 columns }

5) input

# to get type.

print(a.dtype)
d-data,type

5) o/p

int32

6) input

to get size.
print(a.itemsize)

6) o/p

4  ( because 4 * 8 = 32 ) 8 - bytes

7) input

note :
we can specify the dtype in the beginning itself ex:

a=np.array([2,3,4],dtype='int16')
print(a.itemsize)

7) o/p

2 (because 2 * 8 = 16 ) 8 - bytes

8) input

# to get total size.


a=np.array([[2,5,4],[3,5,4]])

print(a.nbytes) # gets total size.
print(a.size * a.itemsize)  # gets the total size.

8) o/p

24
24

9) input

#to get specific element [row,column]

print(a)
print(a[1,2])  or print(a[-1,-1])  '-' Refers to reverse indexing.

o/p

[[2 5 4]
 [3 5 4]]
                   ( indexing strats from 0 so a[1,2] means 2st row and 3rd column which is 4. )
4

input

#to get specific row only.

print(a[0:1])

o/p

[2 5 4]

input

#to get specific column.

print(a[:,2])

o/p

[4 4]