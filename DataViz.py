import csv
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *

#importing cleaned data
data = pd.read_csv("/Users/lawandyaseen/Desktop/PPOL564FinalProject/Suspension_TeachExp_Finance.csv")
#dropping index column lol
data = data.drop(columns = ["Unnamed: 0"])



#sorting
viz1 = data.sort_values(by = "ALL STUDENTS", ascending = False)

viz1

ggplot(data, aes(x = "SCHOOL_LEVEL_PER_PUPIL_QUARTILE", y="ECONOMICALLY DISADVANTAGED"))+geom_point()

ggplot(data, aes(x = "SCHOOL_LEVEL_PER_PUPIL", y="ECONOMICALLY DISADVANTAGED")) + geom_point()


#animate all students and each student demographic maybe?
data

ggplot(data, aes(x = "ECONOMICALLY DISADVANTAGED", y=""))+geom_point()


#all students tile plot
ggplot(data, aes(x = "SCHOOL_NAME", weight="ALL STUDENTS"))+geom_bar()

#teacher experience level and economically disadvanteg students
ggplot(data, aes(x= "TEACH_EXP", y= "SCHOOL_LEVEL_PER_PUPIL")) + geom_point()





#spending per school tile plot using quartiles
viz3 = data.sort_values(by = "ECONOMICALLY DISADVANTAGED", ascending = False)
viz3 = viz3[:50]
plot = (ggplot(viz3, aes(x = "SCHOOL_NAME", y = "SCHOOL_LEVEL_PER_PUPIL_QUARTILE")) + geom_tile() + guides(fill = False))

plot
