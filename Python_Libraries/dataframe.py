#Dataframe()

import pandas as pd


name=["pooja","anushka","anish","anant","sujal","rutuja","sakshi","pranjal","prajwal","krushna"]
age=[15,12,60,55,21,24,22,35,15,29]
marks=[99,99,35,34,0,100,90,45,76,55]
details={"NAME":name,"AGE":age,"MARKS":marks}
data=pd.DataFrame(details)
print(data)

#head()--->v_n.head() --->top to bottom
# print(data.head())
# print(data.head(3))

#tail()--->bottom to top
# print(data.tail())
# print(data.tail(3))

#columns--->to print titles
# print(data.columns)

#shape--->to print shape of table
# print(data.shape)

#size
# print(data.size)

#index
# print(data.index)

#dtypes
# print(data.dtypes)

#values
# print(data.values)

#describe()--->it will show statistical data
# print(data.describe())
# print(data.describe(include="object"))
# print(data.describe(include="number"))
# print(data.describe(include="all"))


#to print single column    --->data[col_name]
# print(data["NAME"])
#t print multiple column   --->data[["col1","col2"....]]
# print(data[["NAME","AGE"]])

#slicing---> v_n[["c1","c2"]][si:ei:sv]
# print(data[0:5:1])
# print(data[["NAME","AGE"]][0:3:1])

#iterrows()
#by using looping
# for i in data.iterrows():
#     print(i)
#by type-casing
# x=list(data.iterrows())
# print(x)

#sample()
# print(data.sample(n=5))

#info()
# print(data.info())
# print(data.info(memory_usage="deep"))

#loc--->included
# print(data.loc)
# print(data.loc[7])                        #perticular row
# print(data.loc[7,["AGE"]])                #fetching content of particular row
# print(data.loc[7,["AGE","NAME"]])         #fetching multiple content of particular row
# print(data.loc[0:4])
# print(data.loc[0:5:2])
# print(data.loc[0:3:1,"AGE"])                  #slicing and fetching particular column
# print(data.loc[0:3:1,["AGE","NAME"]])         #slicing and fetching multiple particular column
# print(data.loc[0:4,"NAME":"MARKS"])             #slicing and fetching column range ["col_1":"col_n"]

#iloc--->excluded
# print(data.iloc[2,2])
# print(data.iloc[2:5,0:2])
# print(data.iloc[0:4:1,0])
# print(data.iloc[[0,1,3,4,6,7]])

p=pd.read_csv(r"D:\Python\Dating App Dataset.csv")
print(p)

p.head()
print(p.head())


