

# Dependencies and Setup
import pandas as pd
import numpy as np

# File to Load (Remember to Change These)
school_data_to_load = "../SchoolDistrictAnalysis/schools_complete.csv"
student_data_to_load = "../SchoolDistrictAnalysis/students_complete.csv"



# Read School and Student Data File and store into Pandas Data Frames
school_data = pd.read_csv(school_data_to_load)
student_data = pd.read_csv(student_data_to_load)


school_data

# Combine the data into a single dataset
school_data_complete = pd.merge(student_data, school_data, how="left", on=["school_name", "school_name"])
school_data_complete

# Calculate the total number of schools
uniqueschooldata = school_data["school_name"].unique() #gave me the list of all schools individually and didn't include repeat mentions.


countschooldata = school_data["school_name"].value_counts()

len(['Huang High School', 'Figueroa High School', 'Shelton High School',
  'Hernandez High School', 'Griffin High School', 'Wilson High School',
  'Cabrera High School', 'Bailey High School', 'Holden High School',
  'Pena High School', 'Wright High School', 'Rodriguez High School',
  'Johnson High School', 'Ford High School', 'Thomas High School'])


# Calculate the total number of students


countstudentdata = len(student_data["student_name"])
countstudentdata



# Calculate the total budget
totalbudget = school_data["budget"].sum()
totalbudget

mathaverage = student_data["math_score"].mean()
mathaverage

rdaverage = student_data["reading_score"].mean()
rdaverage

#Calculate the overall passing rate (overall average score), i.e. (avg. math score + avg. reading score)/2
overallavgscore = (mathaverage + rdaverage)/2
overallavgscore


#Call the math and reading data and separate data to display 70 or greater scores and calc. into percents.
passmath = len(student_data[student_data["math_score"] >= 70])

percpassmath = (passmath/ countstudentdata)*100
percpassmath


#Percent passing Reading

passreading = len(student_data[student_data["reading_score"] >=70])
#passreading
percpassreading = (passreading/countstudentdata)*100
percpassreading


#createdf = { } to make the single rowed table displaying the above results
districtsummary = [{'Total Schools': 15,  'Total Students': 39170, 'Total Budget': 24649428, 'Avg. Math Score': 78.98, 'Avg. Reading Score': 81.87, '% Passing Math': 74.98, '% Passing Reading': 85.80, '% Overall Passing Rate': 80.43}]
#districtsummary
#Why doesn't this print the zero in the hundredths place of % Passing Reading?
dist= pd.DataFrame(districtsummary)
#Why is this in the order that it is? dist

dist = dist[['Total Schools', 'Total Students', 'Total Budget', 'Avg. Math Score', 'Avg. Reading Score', '% Passing Math', '% Passing Reading', '% Overall Passing Rate']]
dist




#school_data.head(15)



# School Summary
# Create an overview table that summarizes key metrics about each school, including:
# School Name, type, size, budget...
# school_data.loc[:15, ["school_name", "type", "size", "budget"]]
SchoolTypes = school_data.set_index(["school_name"])['type']


PerSchoolCounts = school_data_complete["school_name"].value_counts()
#PerSchoolCounts



# Total School Budget
TotalSchoolBudget = school_data_complete.groupby(["school_name"]).mean()["budget"]
# TotalSchoolBudget

PerStudentCapa = TotalSchoolBudget/PerSchoolCounts
# PerStudentCapa
# # Calc per student budget: 


#Create a new column that calcs (and titles) the per school data and student budget for each school?
# school_data['Per Student Budget'] = school_data['budget']/school_data['size']

# Average Math Score
eachschoolsmath = school_data_complete.groupby(["school_name"]).mean()["math_score"]

# Average Reading Score
eachschoolsread = school_data_complete.groupby(["school_name"]).mean()["reading_score"]

# % Passing Math
stuspassmt = school_data_complete[(school_data_complete["math_score"] >= 70)]
# stuspassmt
sclpassmt = stuspassmt.groupby(["school_name"]).count()["student_name"]/PerSchoolCounts*100

# % Passing Reading
stuspassrd = school_data_complete[(school_data_complete["reading_score"] >= 70)]

sclpassrd = stuspassrd.groupby(["school_name"]).count()["student_name"]/PerSchoolCounts*100


# Overall Passing Rate (Average of the above two)

overpassrt = (sclpassrd + sclpassmt)/2


# Create a dataframe to hold the above results
SchoolSummarydf = pd.DataFrame({"Total Students": PerSchoolCounts, 
                                "Type": SchoolTypes, 
                                "Total School Budget": TotalSchoolBudget,
                                "Per Student Budget": PerStudentCapa,
                                "Average Math Score": eachschoolsmath, 
                                "Average Reading Score": eachschoolsread, 
                                "% Passing Math": sclpassmt, 
                                "% Passing Reading": sclpassrd, 
                                "Overall Passing Rate": overpassrt })


SchoolSummarydf = SchoolSummarydf[["Total Students", "Type", "Total School Budget", "Per Student Budget", "Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "Overall Passing Rate"]]
SchoolSummarydf



# Sort and display the top five schools in overall passing rate
topoverall = SchoolSummarydf.sort_values("Overall Passing Rate", ascending=False)

topoverall.head()

#Sort and display the five worst-performing schools
lowoverall = SchoolSummarydf.sort_values("Overall Passing Rate")
lowoverall.head()


#Create a table that lists the average Reading Score for students of each grade level (9th, 10th, 11th, 12th) at each school.

# Create a pandas series for each grade. Hint: use a conditional statement.
Ni = school_data_complete[school_data_complete["grade"] == "9th"].groupby("school_name").mean()["reading_score"]
Te = school_data_complete[school_data_complete["grade"] == "10th"].groupby("school_name").mean()["reading_score"]
El = school_data_complete[school_data_complete["grade"] == "11th"].groupby("school_name").mean()["reading_score"]
Tw = school_data_complete[school_data_complete["grade"] == "12th"].groupby("school_name").mean()["reading_score"]
# Group each series by school
# Combine the series into a dataframe
SummRd = pd.DataFrame({"9th Grade": Ni, "10th Grade": Te, "11th Grade": El, "12th Grade": Tw})
SummRd
# Optional: give the displayed data cleaner formatting

# Create a table that lists the average Math Score for students of each grade level (9th, 10th, 11th, 12th) at each school.
# Create a pandas series for each grade. Hint: use a conditional statement.
Nim = school_data_complete[school_data_complete["grade"] == "9th"].groupby("school_name").mean()["math_score"]
Tem = school_data_complete[school_data_complete["grade"] == "10th"].groupby("school_name").mean()["math_score"]
Elm = school_data_complete[school_data_complete["grade"] == "11th"].groupby("school_name").mean()["math_score"]
Twm = school_data_complete[school_data_complete["grade"] == "12th"].groupby("school_name").mean()["math_score"]
# Group each series by school
# Combine the series into a dataframe
SummMt = pd.DataFrame({"9th Grade": Nim, "10th Grade": Tem, "11th Grade": Elm, "12th Grade": Twm})
SummMt

# Sample bins. Feel free to create your own bins.
spending_bins = [0, 585, 615, 645, 675]
spendrg = ["<$585", "$585-615", "$615-645", "$645-675"]



school_data_complete.head()


# Create a table that breaks down school performances based on average Spending Ranges. Use 4 reasonable bins to group school spending. Include in the table each of the following:

# Average Math Score
# Average Reading Score
# % Passing Math
# % Passing Reading
SchoolSummarydf["Spending Ranges"] = pd.cut(PerStudentCapa, spending_bins, labels=spendrg)

mathscorespend = SchoolSummarydf.groupby(["Spending Ranges"]).mean()["Average Math Score"]
readscorespend = SchoolSummarydf.groupby(["Spending Ranges"]).mean()["Average Reading Score"]
passmathspend = SchoolSummarydf.groupby(["Spending Ranges"]).mean()["% Passing Math"]
passreadspend = SchoolSummarydf.groupby(["Spending Ranges"]).mean()["% Passing Reading"]


# Overall Passing Rate (Average of the above two)

Spendoverallpassrt = (passmathspend + passreadspend)/2
#school_data.head

SpendSumm = SchoolSummarydf[["Average Math Score","Average Reading Score","% Passing Math","% Passing Reading", "Overall Passing Rate"]]

#DataFrame
SpendSumm = pd.DataFrame({"Average Math Score"     :mathscorespend,
                          "Average Reading Score"     :readscorespend,
                          "% Passing Math"     :passmathspend,
                          "% Passing Reading"     :passreadspend,
                          "Overall Passing Rate"     :Spendoverallpassrt})

SpendSumm.groupby("Spending Ranges").head(15)

# Sample bins. Feel free to create your own bins.
size_bins = [0, 1000, 2000, 5000]
sizerange = ["Small (<1000)", "Medium (1000-2000)", "Large (2000-5000)"]

# Create a table that breaks down school performances based on School Size. Use 4 reasonable bins to group school spending. Include in the table each of the following:
SchoolSummarydf["Size Ranges"] = pd.cut(PerStudentCapa, size_bins, labels=sizerange)

szmtscore = SchoolSummarydf.groupby(["Size Ranges"]).mean()["Average Math Score"]
szrdscore = SchoolSummarydf.groupby(["Size Ranges"]).mean()["Average Reading Score"]
szpasmt =SchoolSummarydf.groupby(["Size Ranges"]).mean()["% Passing Math"]
szpasrd =SchoolSummarydf.groupby(["Size Ranges"]).mean()["% Passing Reading"]
# Average Math Score
# Average Reading Score
# % Passing Math
# % Passing Reading


# Overall Passing Rate (Average of the above two)
szoverallpass = (szpasmt + szpasrd)/2
SchoolSummarydf

# Create a table that breaks down school performances based on school type. 

# Average Math Score
# Average Reading Score
# % Passing Math
# % Passing Reading
typms = SchoolSummarydf.groupby(["Type"]).mean()["Average Math Score"]
typrs = SchoolSummarydf.groupby(["Type"]).mean()["Average Reading Score"]
typpmt =SchoolSummarydf.groupby(["Type"]).mean()["% Passing Math"]
typprd =SchoolSummarydf.groupby(["Type"]).mean()["% Passing Reading"]
# Overall Passing Rate (Average of the above two)
typoverallpassingrate = (typpmt + typprd)/2
typoverallpassingrate

#Show results by indexing
TypeSum = pd.DataFrame({"Average Math Score"     :typms,
                        "Average Reading Score"     :typrs,
                        "% Passing Math"          :typpmt,
                        "% Passing Reading"           :typprd,
                        "Overall Passing Rate"          :typoverallpassingrate})

#df
TypeSum = TypeSum[["Average Math Score", "Average Reading Score", "% Passing Math", "% Passing Reading", "Overall Passing Rate"]]

TypeSum.groupby("Type").head()


