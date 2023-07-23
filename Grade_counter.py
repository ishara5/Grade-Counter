import os

#get file names from a directory
def get_file_name(file_path):
    text_files = []
    # iterate over all files in the directory
    for filename in os.listdir(file_path):
        if filename.endswith(".txt"):
            text_files.append(filename)
    return text_files

# this function inputs 7 lenght string and return 1 if final letter is Uppercase otherwise 0
def is_uppercase_final_letter(string):
    if len(string) != 7:
        return False
    if string[6].isupper():
        return True
    else:
        return False    

# n lenth list with all elements are zero
def zero_list(n):
    list = []
    for i in range(n):
        list.append(0)
    return list   

# make grade list
Grades = ["A", "B", "C", "D", "F","I-we","I-re"]
Auxileries = ["+", "-"]
Final_grades = []
for grade in Grades:
    Final_grades.append(grade)
    if grade == "D" or grade == "F" or grade == "I-we" or grade == "I-re":
        continue    
    Final_grades.append(grade + Auxileries[0])
    Final_grades.append(grade + Auxileries[1])
    
#make dictionary that count the number of grades   
initiate_count = zero_list(len(Final_grades))
Final_grade_count = dict(zip(Final_grades, initiate_count))

file_path = "E:\Programming\Python"
text_files = get_file_name(file_path)

for i in range(len(text_files)):
    print(i+1, ":", text_files[i])
    
print("input number to select the file: ")
file_num = int(input())

result_sheet_name = str(text_files[file_num-1])
file_path = file_path + "\\" + result_sheet_name

try:
    reult_sheet = open(file_path, "r")
except FileNotFoundError:
    print("File not found")
    exit()

# read line by line
for line in reult_sheet:
    line = line.strip()
    line_list = line.split()

    j = len(line_list)
    i = 0
    
    while i < j:
        if is_uppercase_final_letter(line_list[i]) and line_list[i+1] in Final_grades:
            try:
                Final_grade_count[line_list[i+1]] += 1
            except KeyError:
                print("Error result ID: ", line_list[i])
                exit()
        # let's check the next id
        i += 2

print("For module ", result_sheet_name, " the result is: ")        
for key in Final_grade_count:      
    print(key, ":", Final_grade_count[key])
 