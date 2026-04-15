import numpy as np
from numpy.testing.print_coercion_tables import print_new_cast_table

# print(np.__version__)

# a=np.array([1,2,3,4])
# print(a)
# print(a.ndim)   #one dimension array
# a=np.array(10)  #Zero dimension array
# print(a)
# print(a.ndim)
# a=np.array([[1,2,3],[4,5,6]])  #two dimension array
# print(a)
# print(a.ndim)

# a=np.array([1,2,3,4])
# print(a.shape)
# a=np.array([[1,2,3,4],[5,6,7,8]])
# print(a.shape)

# a=np.array([1,2,3,4])
# print(a.dtype)

# a=np.array([1,2,3,4])
# b=a.reshape(1,4)
# print(b)
# x=np.array([[1,2,3],[4,5,6]])
# print(x)
# y=x.reshape(3,2)
# print(y)

# Note:--->
# If we want flatten or convert
# multidimensional array to uni-dimensional
# then we will use syntax:->
# array_var.reshape(-1)
# x=np.array([[1,2,3],[4,5,6]])
# print(x)
# y=x.reshape(-1)
# print(y)
# y1=x.flatten()
# print(y1)
# y2=x.flatten(order="C")  #C-->rows
# print(y2)
# y3=x.flatten(order="F") #F-->column
# print(y3)

# Note2:-
# To convert uni-dimensional array to n
# dimension array we will make use of ndmin
# x=np.array([1,2,3,4,5],ndmin=3)
# print(x)

# x=np.arange(1,10,2)
# print(x)
# x1=np.arange(0,20,2)
# print(x1)

# x=np.linspace(1,10,5,retstep=True)
# print(x)

# x=np.random.randint(1,5)
# print(x)
# x1=np.random.randint(5,10,3)
# print(x1)
# y=np.random.randn()
# print(y)
# y1=np.random.randn(2)
# print(y1)
# z=np.random.rand()
# print(z)
# a=np.random.choice([1,2,3,3+4j,4,5,"Hello"])
# print(a)
# arr=np.array([1,2,7.8,'hii',False,(1,2,3)],dtype=object)
# np.random.shuffle(arr)
# print(arr)
# a=[1,2,3,4,5]
# np.random.shuffle(a)
# print(a)

# a=np.array([1,2,3,4])
# print(a)
# b=np.append(a,99)
# print(b)
# b=np.array([[1,2],[3,4]])
# print(b)
# c=np.append(b,100)
# print(c)
# c=np.array([[1,2,3],[4,5,6]])
# print(c)
# x=np.append(c,(99,90))
# print(x)

# p=np.array([1,2,3,4])
# print(p)
# x=np.insert(p,4,5)
# print(x)
# x1=np.insert(p,(0,3),5)
# print(x1)

# a=np.array([1,2,3,4,5])
# d=np.delete(a,3)
# print(a)
# print(d)

# b=np.array([11,12,13,14,15,12,16,12,15])
# print(b)
# y=np.where(b==12)
# print(y)
# y1=np.where(b==200)
# print(y1)
# y2=np.where(b==15)
# print(y2)

# c=np.array([11,12,13,14,15,12,16,12])
# y3=np.array_split(c,10)
# y4=np.array_split(c,4)
# print(y3)
# print(y4)
# a=np.array_split(c,12)
# print(a)


# z=np.asarray([1,2,3,4,5],dtype=complex)
# print(z)
# x=np.asarray([1,2,3],dtype=float)
# print(x)
# x1=np.asarray([4,5,6],dtype=str)
# print(x1)

# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a)
# x=a.flatten()
# print(x)
# y=a.flatten(order="F")
# print(y)
# z=a.flatten(order="C")
# print(z)

# t=np.array([1,2,3,4,5,6,2,3,7,5,8,90,8])
# print(t)
# y=np.unique(t)
# print(y)
# y1=np.unique(t,return_index=True)
# print(y1)
# y2=np.unique(t,return_index=True,return_counts=True)
# print(y2)

# x=np.zeros(3)
# print(x)
# x1=np.zeros((2,3))
# print(x1)
# x2=np.zeros(3,dtype=int)
# print(x2)

# x=np.ones(5)
# print(x)
# x1=np.ones((2,3))
# print(x1)
# x2=np.ones((2,3),dtype=int)
# print(x2)

# x=np.eye(4)
# print(x)
# print(x.ndim)

# x=np.full((2,3),12)
# print(x)

# x=np.array([11,14,15,99,100])
# y=x.copy()
# print(x)
# print(y)
# #indexing:
# print(x[1])
# #modification:
# x[1]=1212
# print(x)
# print(y)
# y[2]=80
# print(y)
# print(x)


# x=np.array([11,14,15,99,100])
# y=x.view()
# print(x)
# print(y)
# #indexing:
# print(x[1])
# #modification in x:
# x[1]=1212
# print(x)
# print(y)
# #modification in y:
# y[2]=80
# print(y)
# print(x)

# x=[1,2,3,4,5,6,7,8]
# y=np.array_split(x,2)
# print(y)
# y1=np.split(x,2)
# print(y1)

# x=np.array([1,2,3,4,5])
# y=np.array([6,7,8,9,10])
# z=np.concatenate((x,y))
# print(z)
# y1=np.concatenate((x,y),axis=1)  #Error
# print(y1)
# a=np.array([[1,2,3],[4,5,6]])
# b=np.array([[3,2,1],[6,5,4]])
# z1=np.concatenate((a,b))
# print(z1)
# z2=np.concatenate((a,b),axis=1)
# print(z2)

#stack---> it will be used to merge the array. it convert single to 2d
# x=np.array([1,2,3,4,5])
# y=np.array([6,7,8,9,10])
# z=np.stack((x,y),axis=0) #axis:it is dimension  axis=0-->row  axis=1-->column
# print(z)
# z1=np.stack((x,y),axis=1)
# print(z1)

# x=np.array([1,2,3,4,5])
# y=np.array([6,7,8,9,10])
# y1=np.array([16,17,18,19,20])
# z=np.vstack((x,y,y1))  #It always work in row format. We cant change axis.
# print(z)

# x=np.array([1,2,3,4,5])
# y=np.array([6,7,8,9,10])
# y1=np.array([16,17,18,19,20])
# z=np.hstack((x,y,y1))  #work as Horizontal format. We cant change axis
# print(z)

# x=np.array([1,2,3,4])
# y=np.array([6,7,8,9])
# z=np.dstack((x,y))  #Based on depth height. Always 3D
# print(z)


#Arithematic Operations
# x=np.array([1,2,3])
# y=np.array([1,2,3])
# z=np.add(x,y)
# print(z)

# x=np.array([1,2,3])
# y=np.array([1,2,3])
# z=np.subtract(x,y)
# print(z)

# x=np.array([1,2,3])
# y=np.array([1,2,3])
# z=np.multiply(x,y)
# print(z)

# x=np.array([1,2,3])
# y=np.array([1,2,3])
# z=np.divide(x,y)
# print(z)

# x=np.array([1,2,3])
# y=np.array([1,2,3])
# z=np.mod(x,y)
# print(z)

# x=np.array([1,2,3])
# y=np.array([1,2,3])
# z=np.power(x,y)
# print(z)

# #Scalar Operation  ----> we can use all assignment operator
# #syntax---> previous_var=previous_var+number  or   previous_var+=number
# x=np.array([1,2,3,4,5])
# x+=5
# print(x)
# x-=5
# print(x)

