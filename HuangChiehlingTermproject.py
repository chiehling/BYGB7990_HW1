# Chiehling Huang Term Project

import pandas as pd

file = input("Please enter the path of file: ")
df = pd.read_table(file, delimiter="\t")
df.fillna("NA")


def Main():
    print("1. Displaying all student records")
    print("2. Searching student record by last name ")
    print("3. Searching student record by graduating year")
    print("4. Displaying program summary report")

    while True:
        query = input("Please enter the number from 1 to 4 to select the query: ")
        if query == "1":
            print(AllRecord())
            break
        elif query == "2":
            print(LastName())
            break
        elif query == "3":
            print(GradYear())
            break
        elif query == "4":
            print(ProgramSum())
            break
        else:
            print("Please enter a valid number from 1 to 4!")


# Display all student records
def AllRecord():
    return df


# Display students whose last name begins with a certain string (case-insensitive)
def LastName():
    entered_str = input("Please enter the start of last name: ").title()
    df["Last"] = df["Last"].str.title()
    last_name = df[df["Last"].str[:len(entered_str)].isin([entered_str])]
    return last_name


# Display all records for students whose graduating year is a certain year
def GradYear():
    while True:
        try:
            entered_year = int(input("Please enter the graduating year: "))
            grad_year = df.loc[df["GradYear"] == entered_year]
            return grad_year
        except:
            print("Please enter a valid number")


# Display a summary report of number and percent of students in each program,
# for students graduating on/after a certain year
def ProgramSum():
    while True:
        try:
            entered_grad = int(input("Please enter the graduating year: "))
            grad_record = df[df["GradYear"] >= entered_grad]
            record_count = grad_record.groupby("DegreeProgram")["ID"].count()
            record_sum = pd.DataFrame({"DegreeProgram": record_count.index, "Count": record_count.values})
            record_sum["Percent"] = round((record_sum["Count"] / record_sum["Count"].sum()), 2)
            return record_sum
        except:
            print("Please enter a valid number")


Main()