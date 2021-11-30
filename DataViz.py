import csv
import pandas as pd
import matplotlib.pyplot as plt
from plotnine import *

#importing cleaned data
data = pd.read_csv("/Users/lawandyaseen/Desktop/PPOL564FinalProject/Suspension_TeachExp_Finance.csv")
#dropping index column lol
data = data.drop(columns = ["Unnamed: 0"])



#viz1 draft
viz1 = data
ggplot(viz1, aes(x = "ALL STUDENTS", y ="ECONOMICALLY DISADVANTAGED", color = 'factor(SCHOOL_LEVEL_PER_PUPIL_QUARTILE)')) + geom_point() + facet_wrap(["SCHOOL_LEVEL_PER_PUPIL_QUARTILE"])
#facet wrap separates the four quartile plots

#all students tile plot
ggplot(data, aes(x = "SCHOOL_NAME", weight="ALL STUDENTS"))+geom_bar()

#teacher experience level and economically disadvanteg students
ggplot(data, aes(x= "TEACH_EXP", y= "BLACK")) + geom_point()

data.describe() #exploring the teach experience values

#spending per school tile plot using quartiles
viz3 = data.sort_values(by = "ECONOMICALLY DISADVANTAGED", ascending = False)
viz3 = viz3[:50]
plot = (ggplot(viz3, aes(x = "SCHOOL_NAME", y = "SCHOOL_LEVEL_PER_PUPIL_QUARTILE")) + geom_tile() + guides(fill = False) + theme(axis_text_x = element_text(angle = 90, hjust = 1)))

plot



#could be useful to exclude elementary schools... if analysis doesn't lose signficant power by dropping those values 
