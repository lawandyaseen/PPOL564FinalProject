import csv
import pandas as pd

#Data Preprocessing

#Unit of Analysis - In School Suspension in each School


#discipline data at school level
discipline = pd.read_excel("/Users/lawandyaseen/Desktop/PPOL564 Final Project/Raw Data/discipline_201819.xlsx")
data = pd.read_csv("/Users/lawandyaseen/Desktop/PPOL564FinalProject/project_data.csv")

#dropping unwanted columns
discipline = discipline.drop(columns = ["SCHOOL_YEAR", "DISTRICT_NO", "STUDENT_CNT", "DISTRICT_NAME", "SCHOOL_NO", "EXPULSION_RATE","OUT_OF_SCHOOL_SUSPENSION_RATE"])

#subsets of students
student_groups = list(discipline.STUDENT_GROUP.unique())

#pulling unique school names
school_list = list(discipline.SCHOOL_NAME.unique())

#removing "All Schools"
school_list.remove('All Schools')


#total number of schools
len(school_list)




#ALL STUDENTS

#subset of only student group being ALL students
all_students = discipline[discipline["STUDENT_GROUP"] == student_groups[0]]

#cross referencing school list
schools = all_students.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools = all_students[schools]

filtered_schools = filtered_schools.rename(columns = {"IN_SCHOOL_SUSPENSION_RATE":"ALL STUDENTS"})

#dropping subset descriptive column
filtered_schools = filtered_schools.drop(columns = ["STUDENT_GROUP"])

#duplicate school names
filtered_schools = filtered_schools.drop_duplicates(subset=['SCHOOL_NAME'])




#Asian Students
asian_students = discipline[discipline["STUDENT_GROUP"] == student_groups[1]]

#cross referencing school list
schools = asian_students.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_asian = asian_students[schools]


filtered_schools_asian = filtered_schools_asian.rename(columns = {"IN_SCHOOL_SUSPENSION_RATE":"ASIAN"})
filtered_schools_asian = filtered_schools_asian.drop(columns = ["STUDENT_GROUP"])

filtered_schools_asian = filtered_schools_asian.drop_duplicates(subset=['SCHOOL_NAME'])

#merging dataframes based on the school column
result = pd.merge(filtered_schools,filtered_schools_asian, on = "SCHOOL_NAME", how = "left")

result





#Black students
black_students = discipline[discipline["STUDENT_GROUP"] == student_groups[2]]

#cross referencing school list
schools = black_students.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_black = black_students[schools]


filtered_schools_black = filtered_schools_black.rename(columns = {"IN_SCHOOL_SUSPENSION_RATE":"BLACK"})
filtered_schools_black = filtered_schools_black.drop(columns = ["STUDENT_GROUP"])

filtered_schools_black = filtered_schools_black.drop_duplicates(subset=['SCHOOL_NAME'])


result = pd.merge(result,filtered_schools_black, on = "SCHOOL_NAME", how = "left")






#black/hispanic/nativeamerican
BHNA_students = discipline[discipline["STUDENT_GROUP"] == student_groups[3]]

#cross referencing school list
schools = BHNA_students.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_BHNA = BHNA_students[schools]


filtered_schools_BHNA = filtered_schools_BHNA.rename(columns = {"IN_SCHOOL_SUSPENSION_RATE":"BHNA"})
filtered_schools_BHNA = filtered_schools_BHNA.drop(columns = ["STUDENT_GROUP"])

filtered_schools_BHNA = filtered_schools_BHNA.drop_duplicates(subset=['SCHOOL_NAME'])


result = pd.merge(result,filtered_schools_BHNA, on = "SCHOOL_NAME", how = "left")








#economically disadvantaged
econ_students = discipline[discipline["STUDENT_GROUP"] == student_groups[4]]

#cross referencing school list
schools = econ_students.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_econ = econ_students[schools]


filtered_schools_econ = filtered_schools_econ.rename(columns = {"IN_SCHOOL_SUSPENSION_RATE":"ECONOMICALLY DISADVANTAGED"})
filtered_schools_econ = filtered_schools_econ.drop(columns = ["STUDENT_GROUP"])

filtered_schools_econ = filtered_schools_econ.drop_duplicates(subset=['SCHOOL_NAME'])

result = pd.merge(result,filtered_schools_econ, on = "SCHOOL_NAME", how = "left")








#ELA
ELA_students = discipline[discipline["STUDENT_GROUP"] == student_groups[5]]

#cross referencing school list
schools = ELA_students.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_ELA = ELA_students[schools]


filtered_schools_ELA = filtered_schools_ELA.rename(columns = {"IN_SCHOOL_SUSPENSION_RATE":"ELA"})
filtered_schools_ELA = filtered_schools_ELA.drop(columns = ["STUDENT_GROUP"])

filtered_schools_ELA = filtered_schools_ELA.drop_duplicates(subset=['SCHOOL_NAME'])

result = pd.merge(result,filtered_schools_ELA, on = "SCHOOL_NAME", how = "left")








#female
female_students = discipline[discipline["STUDENT_GROUP"] == student_groups[6]]

#cross referencing school list
schools = female_students.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_female = female_students[schools]


filtered_schools_female = filtered_schools_female.rename(columns = {"IN_SCHOOL_SUSPENSION_RATE":"FEMALE"})
filtered_schools_female = filtered_schools_female.drop(columns = ["STUDENT_GROUP"])

filtered_schools_female = filtered_schools_female.drop_duplicates(subset=['SCHOOL_NAME'])

result = pd.merge(result,filtered_schools_female, on = "SCHOOL_NAME", how = "left")







#hispanic
hispanic_students = discipline[discipline["STUDENT_GROUP"] == student_groups[7]]

#cross referencing school list
schools = hispanic_students.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_hispanic = hispanic_students[schools]


filtered_schools_hispanic = filtered_schools_hispanic.rename(columns = {"IN_SCHOOL_SUSPENSION_RATE":"HISPANIC"})
filtered_schools_hispanic = filtered_schools_hispanic.drop(columns = ["STUDENT_GROUP"])

filtered_schools_hispanic = filtered_schools_hispanic.drop_duplicates(subset=['SCHOOL_NAME'])

result = pd.merge(result,filtered_schools_hispanic, on = "SCHOOL_NAME", how = "left")







#male
male_students = discipline[discipline["STUDENT_GROUP"] == student_groups[8]]

#cross referencing school list
schools = male_students.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_male = male_students[schools]


filtered_schools_male = filtered_schools_male.rename(columns = {"IN_SCHOOL_SUSPENSION_RATE":"MALE"})
filtered_schools_male = filtered_schools_male.drop(columns = ["STUDENT_GROUP"])

filtered_schools_male = filtered_schools_male.drop_duplicates(subset=['SCHOOL_NAME'])

result = pd.merge(result,filtered_schools_male, on = "SCHOOL_NAME", how = "left")







#native
native_students = discipline[discipline["STUDENT_GROUP"] == student_groups[9]]

#cross referencing school list
schools = native_students.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_native = native_students[schools]


filtered_schools_native = filtered_schools_native.rename(columns = {"IN_SCHOOL_SUSPENSION_RATE":"NATIVE"})
filtered_schools_native = filtered_schools_native.drop(columns = ["STUDENT_GROUP"])

filtered_schools_native = filtered_schools_native.drop_duplicates(subset=['SCHOOL_NAME'])

result = pd.merge(result,filtered_schools_native, on = "SCHOOL_NAME", how = "left")








#pacific_islander
pacific_islander_students = discipline[discipline["STUDENT_GROUP"] == student_groups[10]]

#cross referencing school list
schools = pacific_islander_students.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_pacific_islander = pacific_islander_students[schools]


filtered_schools_pacific_islander = filtered_schools_pacific_islander.rename(columns = {"IN_SCHOOL_SUSPENSION_RATE":"PACIFIC ISLANDER"})
filtered_schools_pacific_islander = filtered_schools_pacific_islander.drop(columns = ["STUDENT_GROUP"])

filtered_schools_pacific_islander = filtered_schools_pacific_islander.drop_duplicates(subset=['SCHOOL_NAME'])

result = pd.merge(result,filtered_schools_pacific_islander, on = "SCHOOL_NAME", how = "left")






#white students
white_students = discipline[discipline["STUDENT_GROUP"] == student_groups[12]]

#cross referencing school list
schools = white_students.SCHOOL_NAME.isin(school_list)


#dataframe only including schools
filtered_schools_white = white_students[schools]


filtered_schools_white = filtered_schools_white.rename(columns = {"IN_SCHOOL_SUSPENSION_RATE":"WHITE"})
filtered_schools_white = filtered_schools_white.drop(columns = ["STUDENT_GROUP"])

filtered_schools_white = filtered_schools_white.drop_duplicates(subset=['SCHOOL_NAME'])

result = pd.merge(result,filtered_schools_white, on = "SCHOOL_NAME", how = "left")







#double checking no duplicates or dropped schools
len(result)










#Educator Licensure
licensure = pd.read_excel("/Users/lawandyaseen/Desktop/PPOL564 Final Project/Raw Data/EducatorExperienceandLicensureData1819.xlsx", sheet_name = "School Data 18-19")
licensure


#licensure reported as a fraction of 1
licensure['Percentage'] = licensure['Percentage']*100
licensure = licensure.rename(columns = {"School Name":"SCHOOL_NAME"})
licensure = licensure.drop(columns = ["District Number", "District Name", "School Number", "Number"])
#renaming school column to use isin

#same thing as previous --- want the percentage of each teacher category

teacher_groups = list(licensure.Category.unique())

#6 identifies here so will have 17 markers in total



#inexperienced
inexperienced_teachers = licensure[licensure["Category"] == teacher_groups[0]]

#cross referencing school list
schools = inexperienced_teachers.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools = inexperienced_teachers[schools]

filtered_schools = filtered_schools.rename(columns = {"Percentage":"TEACH_INEXP"})
filtered_schools = filtered_schools.drop(columns = ["Category"])


#duplicate school names
filtered_schools = filtered_schools.drop_duplicates(subset=['SCHOOL_NAME'])

result = result.merge(filtered_schools, on = "SCHOOL_NAME")





#experienced
experienced_teachers = licensure[licensure["Category"] == teacher_groups[1]]

#cross referencing school list
schools = experienced_teachers.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_exp = experienced_teachers[schools]

filtered_schools_exp = filtered_schools_exp.rename(columns = {"Percentage":"TEACH_EXP"})
filtered_schools_exp = filtered_schools_exp.drop(columns = ["Category"])


#duplicate school names
filtered_schools_exp = filtered_schools_exp.drop_duplicates(subset=['SCHOOL_NAME'])


result = result.merge(filtered_schools_exp, on = "SCHOOL_NAME")




#emergency
emergency_teachers = licensure[licensure["Category"] == teacher_groups[2]]

#cross referencing school list
schools = emergency_teachers.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_emerg = emergency_teachers[schools]

filtered_schools_emerg = filtered_schools_emerg.rename(columns = {"Percentage":"TEACH_EMERG"})
filtered_schools_emerg = filtered_schools_emerg.drop(columns = ["Category"])


#duplicate school names
filtered_schools_emerg = filtered_schools_emerg.drop_duplicates(subset=['SCHOOL_NAME'])


result = result.merge(filtered_schools_emerg, on = "SCHOOL_NAME")





#notemergency
notemergency_teachers = licensure[licensure["Category"] == teacher_groups[3]]

#cross referencing school list
schools = notemergency_teachers.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_notemerg = notemergency_teachers[schools]

filtered_schools_notemerg = filtered_schools_notemerg.rename(columns = {"Percentage":"TEACH_NOT_EMERG"})
filtered_schools_notemerg = filtered_schools_notemerg.drop(columns = ["Category"])


#duplicate school names
filtered_schools_notemerg = filtered_schools_notemerg.drop_duplicates(subset=['SCHOOL_NAME'])

result = result.merge(filtered_schools_notemerg, on = "SCHOOL_NAME")


#out of field
out_of_field = licensure[licensure["Category"] == teacher_groups[4]]

#cross referencing school list
schools = out_of_field.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_out = out_of_field[schools]

filtered_schools_out = filtered_schools_out.rename(columns = {"Percentage":"TEACH_OUT_OF_FIELD"})
filtered_schools_out = filtered_schools_out.drop(columns = ["Category"])


#duplicate school names
filtered_schools_out = filtered_schools_out.drop_duplicates(subset=['SCHOOL_NAME'])

result = result.merge(filtered_schools_out, on = "SCHOOL_NAME")





#out of field
in_field = licensure[licensure["Category"] == teacher_groups[5]]

#cross referencing school list
schools = in_field.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools_in = in_field[schools]

filtered_schools_in = filtered_schools_in.rename(columns = {"Percentage":"TEACH_IN_FIELD"})
filtered_schools_in = filtered_schools_in.drop(columns = ["Category"])


#duplicate school names
filtered_schools_in = filtered_schools_in.drop_duplicates(subset=['SCHOOL_NAME'])


result = result.merge(filtered_schools_in, on = "SCHOOL_NAME")





#Expenditure
finance = pd.read_excel("/Users/lawandyaseen/Desktop/PPOL564 Final Project/Raw Data/FinalReportCarddata2018201921.xlsx")
finance

#selecting columns of interest
finance = finance[["School Name", 'Total School Level Per Pupil Expenditures']]

finance = finance.rename(columns = {"School Name": "SCHOOL_NAME"})
finance = finance.rename(columns = {"Total School Level Per Pupil Expenditures": "SCHOOL_LEVEL_PER_PUPIL"})

schools = finance.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_finance = finance[schools]

filtered_finance = filtered_finance.drop_duplicates(subset=['SCHOOL_NAME'])

result = result.merge(filtered_finance, on = "SCHOOL_NAME")



#changing all NA entries to 0 for suspensions
for y in range(0,len(result)):
    for x in result.columns:
        if result[x].values[y] == "*":
            result[x].values[y] = 0

#quartile creation for funding --- useful for tile plot and economic disad. analyses
result['SCHOOL_LEVEL_PER_PUPIL_QUARTILE'] = pd.qcut(result['SCHOOL_LEVEL_PER_PUPIL'], q = 4, labels = ['0-25 %', '25-50 %', '50-75 %', '75-100 %'])
result['SCHOOL_LEVEL_PER_PUPIL_QUARTILE'] = result['SCHOOL_LEVEL_PER_PUPIL_QUARTILE'].astype("category")
quartile_dummy = pd.get_dummies(result['SCHOOL_LEVEL_PER_PUPIL_QUARTILE'])
result = pd.concat([result,quartile_dummy], axis = 1)


#final dataframe export

result

result.to_csv('Suspension_TeachExp_Finance.csv')


#1651 total schools
