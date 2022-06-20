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