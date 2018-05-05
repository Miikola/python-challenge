#import dependencies
import os
import csv
import datetime

file_to_load = "employee_data1.csv"
file_to_output = os.path.join()

# Dictionary of states with abbreviations
us_state_abbrev = {
    "Alabama": "AL",
    "Alaska": "AK",
    "Arizona": "AZ",
    "Arkansas": "AR",
    "California": "CA",
    "Colorado": "CO",
    "Connecticut": "CT",
    "Delaware": "DE",
    "Florida": "FL",
    "Georgia": "GA",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Illinois": "IL",
    "Indiana": "IN",
    "Iowa": "IA",
    "Kansas": "KS",
    "Kentucky": "KY",
    "Louisiana": "LA",
    "Maine": "ME",
    "Maryland": "MD",
    "Massachusetts": "MA",
    "Michigan": "MI",
    "Minnesota": "MN",
    "Mississippi": "MS",
    "Missouri": "MO",
    "Montana": "MT",
    "Nebraska": "NE",
    "Nevada": "NV",
    "New Hampshire": "NH",
    "New Jersey": "NJ",
    "New Mexico": "NM",
    "New York": "NY",
    "North Carolina": "NC",
    "North Dakota": "ND",
    "Ohio": "OH",
    "Oklahoma": "OK",
    "Oregon": "OR",
    "Pennsylvania": "PA",
    "Rhode Island": "RI",
    "South Carolina": "SC",
    "South Dakota": "SD",
    "Tennessee": "TN",
    "Texas": "TX",
    "Utah": "UT",
    "Vermont": "VT",
    "Virginia": "VA",
    "Washington": "WA",
    "West Virginia": "WV",
    "Wisconsin": "WI",
    "Wyoming": "WY",
}

#lists to store data
empID = []
firstname = []
lastname = []
dob = []
ssn = [] 
state = []

with open(file_to_load) as emp_data:
    reader = csv.DictReader(emp_data)

    for row in reader: 

    empID = empID + [row["Emp ID]]

#reformat name
    split_name = row["Name"].split(" ")
    firstname = firstname + [split_name[0]]
    lastname = lastname + [split_name[1]]

#reformat dob
    reformatted_dob = datetime.datetime.strptime(row["DOB"], "%Y-%m-%d")
    reformatted_dob = reformatted_dob.strftime('%m/%d/%Y")

    dob = dob + [reformatted_dob]

#reformat SSN
    reformatted_ssn = list(row["SSN"])
    reformatted_ssn[0:3] = ("*","*","*")
    reformatted_ssn[4:6] = ("*","*")
    joined_ssn = "".join(reformatted_ssn)

    ssn = ssn + [joined_ssn]

    state_abbrev = us_state_abbrev[row["State"]]

    state = state + [state_abbrev]

empzip = zip(empID, firstname, lastname, dob, ssn, state)

with open(file_to_output, "w" newline="") as datafile:
        writer = csv.writer(datafile)
        
        writer.writerow(["Emp ID", "First Name", "Last Name", "DOB", "SSN", "State"])

        writer.writerows(empzip)

        



    