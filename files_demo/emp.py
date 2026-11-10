"""Scenario: A company receives employee details in a JSON file. 
Read the file, filter employees whose salary is greater than ₹50,000,
and write the filtered employees into a new JSON file."""


import json
#extract 
with open("emp.json", 'r') as file:
    employees = json.load(file)

#transform - [filter]
filtered_emp = []
for employee in employees:
    if employee["salary"] > 50000:
        filtered_emp.append(employee)

#load/write

with open("high_sal_emp.json", 'w') as file:
    json.dump(filtered_emp, file, indent=4)

print("Data Processed Succesfully")

# take patients data (multiple patients)
# disease = 1) cancer, 2) fever, 3) cough

patients folder - pat1.json , pat2.json, pat3.json -- each file with 10 records
-> name, age, address:[street: "hitech city", state: "ts", country:"ind"], disease:"cancer",


output_folder
    cancer.json # data in one json 

    folder -> ind = ind.json 
    folder -> us = us.json 