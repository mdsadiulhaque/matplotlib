import matplotlib.pyplot as pt #importing matplotlib pt is an alias of pyplot
import pandas as pd #importing pandas , pd is an elias of pandas
#If we want to read something from dataset or csv file we use read_csv() method.
data= pd.read_csv("cgpa.csv")
data= data.head(40) # head() method is used to select some elements of dataset
#here i am plotting rollno vs cgpa so x-axis will be rollno and y-axis will be cgpa
#color of scatter is blue and we also include label as scatter.
#scatter() method is used to plot the scatter
pt.scatter(data["rollno"],data["cgpa"],color="blue",label="scatter")
pt.xlabel("RollNo",color="green") #xlabel() defines the label of x-axis
pt.ylabel("CGPA",color="blue") #ylabel() defines the label of x-axis
pt.title("CGPA vs Roll No",color="green") #title() is used to give title of this scatter plot
#pt.show()
pt.plot(data["rollno"],data["cgpa"],color="red",label="line graph") #plot() is used to create line graph
pt.legend() # Calling&nbsp;legend()&nbsp;with no arguments automatically fetches the legend handlesand their associated labels
pt.show()


#Hence the output will be as-----


import matplotlib.pyplot as pt
import pandas as pd
data = pd.read_csv("cgpa.csv")
data= data.head(30)
#bar() method is used to plot a bar graph
#Here i am taking a list of colors to showing graph attractive
pt.bar(data["rollno"],data["cgpa"],color=["green","blue","pink","red"])
pt.xlabel("RollNo",color="green")
pt.ylabel("CGPA",color="blue")
pt.title("CGPA vs Roll No",color="green")
pt.show()

#pi cheart

import matplotlib.pyplot as pt
import pandas as pd
data = pd.read_csv("cgpa.csv")
data = data.head(30)

x=len(data[data.cgpa>=9]) #students having cgpa over 9 point
x1=len(data[(data.cgpa>=8) & (data.cgpa<9)]) #students got over 8 point but less than 9 point
x2=len(data[data.cgpa<8]) #students having cgpa less than 8 point
pt.axis('equal') #for making pie chart circular,that makes major axis and minor axis equal
#Here we need a list of values that are simply x,x1 and x2
#colors specify a list of colors in pie chart
#In order to specify labels we use labels attribute
pt.pie([x,x1,x2],colors=['yellow','red','blue'],labels=['9 pointer','8 pointer','others'])
pt.legend(title='Description') # to shown the labels as legends
pt.show()