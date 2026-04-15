# import pandas
# print(pandas.__version__)

import pandas as pd

# print(pd.__version__)


#Series()

# x=["a","b","c","d"]
# data=pd.Series(x)
# print(data)
# data=pd.Series(x,index=["i","ii","iii","iv"])   #index---> to change index
# print(data)
# data=pd.Series(x,index=["i","ii","iii","iv"],name="String data type")  #name---> to give name to the series
# print(data)

# y="pandas class"
# z=pd.Series(y)
# print(z)

# w={1,2,3,4}
# u=pd.Series(w)
# print(w)   #TypeError: 'set' type is unordered

# a={1:2,3:4,5:6}
# b=pd.Series(a)
# print(b)

# p=(1,2,3,4,5)
# q=pd.Series(p)
# print(q)

#Series Attribute
# a=[1,2,3,4,5,6,7,2,3,5,2,4,1,4,2]
# x=pd.Series(a)
# print(x)
# print(x.size)
# print(x.shape)
# print(x.values)
# print(x.index)
# print(x.unique())
# print(x.nunique())
