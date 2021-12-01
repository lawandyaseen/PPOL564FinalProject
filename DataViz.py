import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
from plotnine import *

style.available
style.use('fivethirtyeight')

#importing cleaned data
data = pd.read_csv("/Users/lawandyaseen/Desktop/PPOL564FinalProject/Suspension_TeachExp_Finance.csv")
#dropping index column lol
data = data.drop(columns = ["Unnamed: 0"])



#viz1 draft
viz1 = data

#creating ggplot viz
test = ggplot(viz1, aes(x = "ALL STUDENTS", y ="ECONOMICALLY DISADVANTAGED")) + geom_point() + theme_classic() + facet_wrap(["SCHOOL_LEVEL_PER_PUPIL_QUARTILE"])

#adding labels
test = test + labs(x = "Percent of Students Suspended", y = "Percent of Economically Disadvantaged Students Suspended", title = "Per Student Funding Effect on ISS")
test



#holding off on how to visually interpret teacher experience level


#all students tile plot
ggplot(data, aes(x = "SCHOOL_NAME", weight="ALL STUDENTS"))+geom_bar()

#teacher experience level and economically disadvanteg students
#ggplot(data, aes(x= "TEACH_EXP", y= "ECONOMICALLY DISADVANTAGED")) + geom_point()

ggplot(data, aes(x = "TEACH_EXP", y = stat(density))) + geom_line()
#teacher experience, black, BHNA, economically disadvantaged
#percent of students Suspended



# circles with colors from default color cycle
for i, color in enumerate(plt.rcParams['axes.prop_cycle']):
    xy = np.random.normal(size=2)
    ax4.add_patch(plt.Circle(xy, radius=0.3, color=color['color']))
ax4.axis('equal')
ax4.margins(0)

plt.show()


#spending per school tile plot using quartiles
viz3 = data.sort_values(by = "ECONOMICALLY DISADVANTAGED", ascending = False)
viz3 = viz3[:50]
plot = (ggplot(viz3, aes(x = "SCHOOL_NAME", y = "SCHOOL_LEVEL_PER_PUPIL_QUARTILE")) + geom_tile() + guides(fill = False) + theme(axis_text_x = element_text(angle = 90, hjust = 1)))

plot



#could be useful to exclude elementary schools... if analysis doesn't lose signficant power by dropping those values
