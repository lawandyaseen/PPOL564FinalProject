import csv
import pandas as pd
import numpy as np

discipline = pd.read_excel("/Users/lawandyaseen/Desktop/PPOL564 Final Project/Raw Data/discipline_201819.xlsx")
race_data = pd.read_excel("/Users/lawandyaseen/Desktop/PPOL564FinalProject/Raw Data/201819_membership.xlsx")

#renaming column for easier use
race_data = race_data.rename(columns = {"SCHOOL NAME": "SCHOOL_NAME"})

#looking at entire school instead of individual grade levels
race_data = race_data[race_data["GRADE"] == "All Grades"]

#removing elementary schools from this group
discipline = discipline[~discipline.SCHOOL_NAME.str.contains("Elementary")]
school_list = list(discipline.SCHOOL_NAME.unique())
school_list.remove('All Schools')
len(school_list)


#race dataset
race_data_test = race_data.SCHOOL_NAME.isin(school_list)

race_data_filtered = race_data[race_data_test]

race_pivot = pd.pivot_table(race_data_filtered, values = ["ENROLLMENT"], index = ['SCHOOL_NAME', 'RACE'], aggfunc = np.sum)

race_pivot.reset_index(inplace = True)

races = list(race_pivot.RACE.unique())

#outcome of interest --- in school suspension rate

#dropping un-needed columns
discipline = discipline.drop(columns = ["SCHOOL_YEAR", "DISTRICT_NO", "STUDENT_CNT", "DISTRICT_NAME", "SCHOOL_NO", "EXPULSION_RATE","OUT_OF_SCHOOL_SUSPENSION_RATE"])

#subset of only student group being ALL students
iss_students = discipline[discipline["STUDENT_GROUP"] == "All Students"]

#cross referencing school list
schools = iss_students.SCHOOL_NAME.isin(school_list)

#dataframe only including schools
filtered_schools = iss_students[schools]

#dropping subset descriptive column
filtered_schools = filtered_schools.drop(columns = ["STUDENT_GROUP"])

#duplicate school names
filtered_schools = filtered_schools.drop_duplicates(subset=['SCHOOL_NAME'])




#pivot_table with school and gender values
test_pivot = pd.pivot_table(race_data_filtered, values = ["ENROLLMENT"], index = ['SCHOOL_NAME', 'GENDER'], aggfunc = np.sum)

test_pivot.reset_index(inplace = True)

genders = list(test_pivot.GENDER.unique())


#follow the same methodology used in DataTransform?

#all students
all_genders = test_pivot[test_pivot["GENDER"] == genders[0]]

schools = all_genders.SCHOOL_NAME.isin(school_list)

filtered_all_genders = all_genders[schools]

filtered_all_genders = filtered_all_genders.rename(columns = {"ENROLLMENT":"ALL STUDENTS"})

#dropping subset descriptive column
filtered_all_genders = filtered_all_genders.drop(columns = ["GENDER"])

result = pd.merge(filtered_schools, filtered_all_genders, on = "SCHOOL_NAME", how = "left")



#female students
all_female = test_pivot[test_pivot["GENDER"] == genders[1]]

schools = all_female.SCHOOL_NAME.isin(school_list)

filtered_all_female = all_female[schools]

filtered_all_female = filtered_all_female.rename(columns = {"ENROLLMENT":"FEMALE"})

#dropping subset descriptive column
filtered_all_female = filtered_all_female.drop(columns = ["GENDER"])

result = pd.merge(result,filtered_all_female, on = "SCHOOL_NAME", how = "left")

result["FEMALE"] = (result["FEMALE"]/result["ALL STUDENTS"])*100




#male students
all_male = test_pivot[test_pivot["GENDER"] == genders[2]]

schools = all_male.SCHOOL_NAME.isin(school_list)

filtered_all_male = all_male[schools]

filtered_all_male = filtered_all_male.rename(columns = {"ENROLLMENT":"MALE"})

#dropping subset descriptive column
filtered_all_male = filtered_all_male.drop(columns = ["GENDER"])

result = pd.merge(result,filtered_all_male, on = "SCHOOL_NAME", how = "left")


result["MALE"] = (result["MALE"]/result["ALL STUDENTS"])*100




#race dataset
race_data_test = race_data.SCHOOL_NAME.isin(school_list)

race_data_filtered = race_data[race_data_test]

race_pivot = pd.pivot_table(race_data_filtered, values = ["ENROLLMENT"], index = ['SCHOOL_NAME', 'RACE'], aggfunc = np.sum)

race_pivot.reset_index(inplace = True)

races = list(race_pivot.RACE.unique())
#total values for "All Genders" and "All Races" match -- a good sign



#native students
native_students = race_pivot[race_pivot["RACE"] == races[1]]

schools = native_students.SCHOOL_NAME.isin(school_list)

filtered_native_students = native_students[schools]

filtered_native_students = filtered_native_students.rename(columns = {"ENROLLMENT":"NATIVE"})

#dropping subset descriptive column
filtered_native_students = filtered_native_students.drop(columns = ["RACE"])

result = pd.merge(result,filtered_native_students, on = "SCHOOL_NAME", how = "left")

result["NATIVE"] = (result["NATIVE"]/result["ALL STUDENTS"])*100




#asian students
asian_students = race_pivot[race_pivot["RACE"] == races[2]]

schools = asian_students.SCHOOL_NAME.isin(school_list)

filtered_asian_students = asian_students[schools]

filtered_asian_students = filtered_asian_students.rename(columns = {"ENROLLMENT":"ASIAN"})

#dropping subset descriptive column
filtered_asian_students = filtered_asian_students.drop(columns = ["RACE"])

result = pd.merge(result,filtered_asian_students, on = "SCHOOL_NAME", how = "left")

result["ASIAN"] = (result["ASIAN"]/result["ALL STUDENTS"])*100




#black students
black_students = race_pivot[race_pivot["RACE"] == races[3]]

schools = black_students.SCHOOL_NAME.isin(school_list)

filtered_black_students = black_students[schools]

filtered_black_students = filtered_black_students.rename(columns = {"ENROLLMENT":"BLACK"})

#dropping subset descriptive column
filtered_black_students = filtered_black_students.drop(columns = ["RACE"])

result = pd.merge(result,filtered_black_students, on = "SCHOOL_NAME", how = "left")

result["BLACK"] = (result["BLACK"]/result["ALL STUDENTS"])*100




#hispanic students
hispanic_students = race_pivot[race_pivot["RACE"] == races[4]]

schools = hispanic_students.SCHOOL_NAME.isin(school_list)

filtered_hispanic_students = hispanic_students[schools]

filtered_hispanic_students = filtered_hispanic_students.rename(columns = {"ENROLLMENT":"HISPANIC"})

#dropping subset descriptive column
filtered_hispanic_students = filtered_hispanic_students.drop(columns = ["RACE"])

result = pd.merge(result,filtered_hispanic_students, on = "SCHOOL_NAME", how = "left")

result["HISPANIC"] = (result["HISPANIC"]/result["ALL STUDENTS"])*100





#multiple students
multiple_students = race_pivot[race_pivot["RACE"] == races[5]]

schools = multiple_students.SCHOOL_NAME.isin(school_list)

filtered_multiple_students = multiple_students[schools]

filtered_multiple_students = filtered_multiple_students.rename(columns = {"ENROLLMENT":"MULTIPLE"})

#dropping subset descriptive column
filtered_multiple_students = filtered_multiple_students.drop(columns = ["RACE"])

result = pd.merge(result,filtered_multiple_students, on = "SCHOOL_NAME", how = "left")

result["MULTIPLE"] = (result["MULTIPLE"]/result["ALL STUDENTS"])*100




#AAPI students
AAPI_students = race_pivot[race_pivot["RACE"] == races[6]]

schools = AAPI_students.SCHOOL_NAME.isin(school_list)

filtered_AAPI_students = AAPI_students[schools]

filtered_AAPI_students = filtered_AAPI_students.rename(columns = {"ENROLLMENT":"AAPI"})

#dropping subset descriptive column
filtered_AAPI_students = filtered_AAPI_students.drop(columns = ["RACE"])

result = pd.merge(result,filtered_AAPI_students, on = "SCHOOL_NAME", how = "left")

result["AAPI"] = (result["AAPI"]/result["ALL STUDENTS"])*100




#white students
white_students = race_pivot[race_pivot["RACE"] == races[7]]

schools = white_students.SCHOOL_NAME.isin(school_list)

filtered_white_students = white_students[schools]

filtered_white_students = filtered_white_students.rename(columns = {"ENROLLMENT":"WHITE"})

#dropping subset descriptive column
filtered_white_students = filtered_white_students.drop(columns = ["RACE"])

result = pd.merge(result,filtered_white_students, on = "SCHOOL_NAME", how = "left")

result["WHITE"] = (result["WHITE"]/result["ALL STUDENTS"])*100


#done with gender and race school breakdown here !




#teacher experience level

licensure = pd.read_excel("/Users/lawandyaseen/Desktop/PPOL564 Final Project/Raw Data/EducatorExperienceandLicensureData1819.xlsx", sheet_name = "School Data 18-19")



#licensure reported as a fraction of 1
licensure['Percentage'] = licensure['Percentage']*100
licensure = licensure.rename(columns = {"School Name":"SCHOOL_NAME"})
licensure = licensure.drop(columns = ["District Number", "District Name", "School Number", "Number"])


#inexperienced
inexperienced_teachers = licensure[licensure["Category"] == "Inexperienced Teachers"]

#cross referencing school list
schools = inexperienced_teachers.SCHOOL_NAME.isin(school_list)


#dataframe only including schools
filtered_schools = inexperienced_teachers[schools]

filtered_schools = filtered_schools.rename(columns = {"Percentage":"TEACH_INEXP"})
filtered_schools = filtered_schools.drop(columns = ["Category"])


result = result.merge(filtered_schools, on = "SCHOOL_NAME")







#Expenditure
finance = pd.read_excel("/Users/lawandyaseen/Desktop/PPOL564 Final Project/Raw Data/FinalReportCarddata2018201921.xlsx")


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

result


result.to_csv('project_data.csv')
