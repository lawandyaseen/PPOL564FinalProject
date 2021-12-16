import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
from plotnine import *

style.available
style.use('fivethirtyeight')

#importing cleaned data
data = pd.read_csv("/Users/lawandyaseen/Desktop/PPOL564FinalProject/project_data.csv")
#dropping index column lol
data = data.drop(columns = ["Unnamed: 0"])


gender = pd.melt(data, id_vars = ['SCHOOL_NAME'], value_vars = ['FEMALE', 'MALE'])

race = pd.melt(data, id_vars = ['SCHOOL_NAME'], value_vars = ['NATIVE', 'ASIAN', 'BLACK', 'HISPANIC', 'AAPI', 'WHITE'])


ggplot(data, aes(x = "BLACK", y = "IN_SCHOOL_SUSPENSION_RATE")) + geom_point()

ggplot(data, aes(x = "WHITE", y = "IN_SCHOOL_SUSPENSION_RATE")) + geom_point()

SCHOOL_NAME	IN_SCHOOL_SUSPENSION_RATE	ALL STUDENTS	FEMALE	MALE	NATIVE	ASIAN	BLACK	HISPANIC	MULTIPLE	AAPI	WHITE	TEACH_INEXP	SCHOOL_LEVEL_PER_PUPIL


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


#plots for final report

#suspension rates as a function of black, white, hispanic, asian
ggplot(gender, aes(x = "factor(variable)", y = "value")) + geom_point()

#racial density
ggplot(race, aes(x = "factor(variable)", y = "value")) + geom_point()
#suspension rates as a function of teacher experience

ggplot(data, aes(x = "TEACH_INEXP", y = "IN_SCHOOL_SUSPENSION_RATE")) + geom_point()

#teacher inexperience does not seem to have an efffect on suspension rates





#tile plot - how do i want to break it down
sorted = data.sort_values(by = ["IN_SCHOOL_SUSPENSION_RATE"], ascending = False)
sorted['SCHOOL_LEVEL_PER_PUPIL_QUARTILE'] = pd.qcut(sorted['SCHOOL_LEVEL_PER_PUPIL'], q = 4, labels = ['0-25 %', '25-50 %', '50-75 %', '75-100 %'])
sorted['SCHOOL_LEVEL_PER_PUPIL_QUARTILE'] = sorted['SCHOOL_LEVEL_PER_PUPIL_QUARTILE'].astype("category")
quartile_dummy = pd.get_dummies(sorted['SCHOOL_LEVEL_PER_PUPIL_QUARTILE'])
sorted = pd.concat([sorted,quartile_dummy], axis = 1)
top25 = sorted[:25]

(ggplot(top25, aes(x = "SCHOOL_NAME", y = "SCHOOL_LEVEL_PER_PUPIL_QUARTILE")) + geom_tile() + guides(fill = False) + theme(axis_text_x = element_text(angle = 90, hjust = 1)))
