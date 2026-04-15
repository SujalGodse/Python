# import matplotlib.pyplot as plt
# from torch.utils.benchmark import Language
import numpy as np


#-------->Line Graph
# x=[10,20,30,40,50]
# y=[10,20,30,40,50]
# plt.plot(x,y,marker="o",ms=10,mec="r",mfc="y",ls="dashed",label="Graph")
# plt.xlabel("x-axis",fontsize=10)
# plt.ylabel("y-axis",fontsize=10)
# plt.title("Line Graph",fontsize=15)
# plt.legend(loc="upper left",framealpha=1,shadow=True,fancybox=False,facecolor="red",edgecolor="r")
# plt.grid(axis="both",ls="dotted",c="b")
# plt.show()

#-------->Scatter Graph
# x=[10,20,30,40,50]
# y=[10,20,30,40,50]
# sizes=[500,450,700,650,500]
# plt.scatter(x,y,s=sizes,c=["r","y","g","m","c"],label="Scatter")
# plt.xlabel("x-axis",fontsize=10)
# plt.ylabel("y-axis",fontsize=10)
# plt.title("Line Graph",fontsize=15)
# plt.legend(loc="upper left",framealpha=1,shadow=True,fancybox=False,facecolor="y",edgecolor="r")
# plt.grid(axis="both",ls="dotted",c="black")
# plt.show()

# import matplotlib.pyplot as plt
# language=["python","java","c","c++"]
# Rank=[10,20,30,70]
# plt.pie(Rank,labels=language,explode=[0.1,0.0,0.0,0.0],colors=["r","b","y","m"],autopct="1.1f%%",shadow=True,rotatelabels=True,radius=1,
#         labeldistance=1,startangle=80,counterclock=False,textprops={"fontsize":10})
# plt.show()

import matplotlib.pyplot as plt
language=["python","java","dijango","pycharm"]
Rank=[30,30,30,40]
Rank1=[20,20,20,30]

# plt.pie(Rank,labels=language,explode=[0.1,0.0,0.0,0.0],colors=["r","b","y","m"],autopct="1.1f%%",shadow=True,rotatelabels=True,radius=1,
#         labeldistance=1,startangle=80,counterclock=False,textprops={"fontsize":10})
# plt.show()
width=0.4
x=np.arange(len(language))
print(x)
for i in x:
    print(i,end=" ")
y=[i+width for i in  x]
print(y)
plt.bar(x,Rank,width=0.4,color="b")
plt.bar(y,Rank1,width=0.4,color="y")
plt.xlabel("Language")
plt.ylabel("Rank")
plt.show()