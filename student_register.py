# Program will take the number of students taking an exam and generate a sign in sheet by asking for each students ID number

# Ask how many students there are.

while True: # While loop to ensure correct data entered by user
    try:
        No_Students = int(input("\nHow many students are there in total?\n"))
        break
    except ValueError:
        print("Please enter digits 0-9 only.\n")

print("\n") # For presentation

# Enter ID for each student into a dictionary

List_StudentID = [] # Create a list to store student IDs in

for i in range(No_Students): # For loop to ensure every student can enter in their ID
    List_StudentID.append(input(f"Please enter the ID for pupil {i+1}: ")) # Adds each ID to the list


# Open and add student IDs to a text file.
open_file = False # Boolean to help ensure file opened correctly

while open_file == False:
    textfile = input("\nEnter the name of the file you would like to store the student IDs in (A new file be created if it doesn't exist already):\n")

    if ".txt" in textfile:
        file = open(textfile, 'w+')
    else:
        textfile = textfile + ".txt"
        file =  open(textfile, 'w+')

    open_file = True

# write the list to the text file
for i in range(len(List_StudentID)):
    file.write(List_StudentID[i] + "...............................................................\n")

file.close() # close the file

print("\n\nOperation complete\n")
