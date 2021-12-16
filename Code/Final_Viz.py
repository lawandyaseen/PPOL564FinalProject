import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.style as style
from plotnine import *


#importing cleaned data
data = pd.read_csv("/Users/lawandyaseen/Desktop/PPOL564FinalProject/Cleaned Data/project_data.csv")
#dropping index column lol
data = data.drop(columns = ["Unnamed: 0"])




#comparison of race percentage and suspension rates
viz1 = ggplot(data, (aes(x = "BLACK", y = "IN_SCHOOL_SUSPENSION_RATE"))) + geom_point() + geom_jitter(data, aes(x = "WHITE", y = "IN_SCHOOL_SUSPENSION_RATE"), color = 'red') + geom_jitter(data, aes(x = "HISPANIC", y = "IN_SCHOOL_SUSPENSION_RATE"), color = 'blue') + labs(title="Figure 1. ISS Rates Across Racial Groups", x= "Percent of Population", y="ISS Rate")
#saving graphic
viz1.save (filename = "viz1.png", dpi = 90)



#visualizing racial density
ggplot(race, aes(x = "factor(variable)", y = "value")) + geom_boxplot() + theme_538()



#suspension rates as a function of teacher experience
viz2 = ggplot(data, aes(x = "TEACH_INEXP", y = "IN_SCHOOL_SUSPENSION_RATE")) + geom_point() + geom_smooth(method = "lm") + labs(title="Figure 2. Impact of Inexperienced Teachers on ISS Rate", x= "Percent of Inexperienced Teachers", y="ISS Rate") + theme_538()
#saving graphic
viz2.save(filename = "viz2.png", dpi = 100)

#teacher inexperience does not seem to have an efffect on suspension rates





sorted = data.sort_values(by = ["IN_SCHOOL_SUSPENSION_RATE"], ascending = False)
#spliting spending into quartiles
sorted['SCHOOL_LEVEL_PER_PUPIL_QUARTILE'] = pd.qcut(sorted['SCHOOL_LEVEL_PER_PUPIL'], q = 4, labels = ['0-25 %', '25-50 %', '50-75 %', '75-100 %'])
#creating dummy variables for spending quartiles
sorted['SCHOOL_LEVEL_PER_PUPIL_QUARTILE'] = sorted['SCHOOL_LEVEL_PER_PUPIL_QUARTILE'].astype("category")
quartile_dummy = pd.get_dummies(sorted['SCHOOL_LEVEL_PER_PUPIL_QUARTILE'])
sorted = pd.concat([sorted,quartile_dummy], axis = 1)
#only selecting top 25
top25 = sorted[:25]

#creating viz of above as a tile plot
viz3 = (ggplot(top25, aes(x = "SCHOOL_NAME", y = "SCHOOL_LEVEL_PER_PUPIL_QUARTILE")) + geom_tile() + guides(fill = False) + theme(axis_text_x = element_text(angle = 75, hjust = 1)) + labs(title="Figure 3.Funding Across Schools with Highest ISS Rates", x = "School", y="Spending Quartile"))
#saving viz
viz3.save(filename = "viz3.png", dpi = 100)
