# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# JJepson,2.14.23,Added code to complete assignment 5
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
import os
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = ""  # A Capture the user option selection


# -- Processing -- #
# Step 1 - When the program starts, load any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)

if os.path.exists(objFile):
    with open(objFile, 'r') as file:
        for row in file:
            lstrow = row.split(',')
            dicRow = {'Task': lstrow[0], 'Priority': lstrow[1].strip()}
            lstTable.append(dicRow)


# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print("""
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        if len(lstTable) == 0:
            print('No Tasks.')
        else:
            for row in lstTable:
                print('Task:', row['Task'] + ',', 'Priority:', row['Priority'])
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        dicRow = {'Task': input('Task: '), 'Priority': input('Priority: ')}
        lstTable.append(dicRow)
        print('\nTask Added!')
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strRemove = input('Which task would you like to remove?\n\n'
                          '\tTask: ')
        for row in lstTable:
            if strRemove.lower() == row['Task'].lower():
                lstTable.remove(row)
                print('\nTask Removed!')
            else:
                print('Error! Task does not exist.')

        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        with open(objFile, 'w') as file:
            for row in lstTable:
                file.write(row['Task']+','+row['Priority']+'\n')
        print('Data Saved!')
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        print('Exiting Program!')
        break  # and Exit the program
    else:  # Error if anything input but 1-5
        print('Error! Please enter a number from 1 to 5.')
        