# Timetable Extractor in Python

# Import modules
from openpyxl import *
import sqlite3
import os

"""
Task:
1. Create a simple database and table structure (ONF) for timetable schedule in SQLite.
2. Create a Python function (def) to :
a. read all timetable in Microsoft Excel format
b. extract the timetable contents
c. store the contents into the created table (in item #1)
"""

def insert2db(in_course, in_room, in_day, in_sem, in_timeStart, in_timeEnd):
    # Create / open Database
    db = sqlite3.connect("timetable.db")

    # Get cursor object
    cursor = db.cursor()

    # Create the Table
    cursor.execute("""
         CREATE TABLE IF NOT EXISTS timetable 
         (id INTEGER PRIMARY KEY, 
         course TEXT, 
         roomID TEXT, 
         day TEXT, 
         semester TEXT, 
         timeStart TEXT, 
         timeEnd TEXT)
    """)

    # Commit the transaction
    db.commit()

    # Execute the SQL syntax for INSERT
    try:
        cursor.execute("""
            INSERT INTO timetable (course, roomID, day, semester,
            timeStart, timeEnd) VALUES (?,?,?,?,?,?) """, (in_course,
            in_room, in_day, in_sem, in_timeStart, in_timeEnd))
        db.commit()
        print("\nRecord successfully inserted!\n")

    except Exception as e:
        print("\nUnable to insert record.\nError type:"+ str (e) +"\n")
        db.rollback()

    # Close the DB connection
    db.close()


def readDailyData(read_startRow, read_endRow, read_day, read_Sem):
    # List to store data
    cellColData = []
    cellRowData = []

    # Read Excel's specific row and column grid/cell
    for row_data in sheet[read_startRow:read_endRow]:
        for cell_data in row_data:
            cellColData.append(cell_data.coordinate)
            cellRowData.append(cell_data.value) # Store cell's value in list

    # Get schedule from Excel's cell
    # Check if list is not empty (got data)
    if cellRowData:
        print(cellRowData[2], cellRowData[13])  # 09:00-10:00
        print(cellRowData[3], cellRowData[14])  # 10:00-12:00
        print(cellRowData[4], cellRowData[15])  # 11:00-12:00
        print(cellRowData[5], cellRowData[16])  # 12:00-13:00
        print(cellRowData[6], cellRowData[17])  # 13:00-14:00
        print(cellRowData[7], cellRowData[18])  # 14:00-15:00
        print(cellRowData[8], cellRowData[19])  # 15:00-16:00
        print(cellRowData[9], cellRowData[20])  # 16:00-17:00
        print(cellRowData[10], cellRowData[21]) # 17:00-18:00

        # Insert data into record
        try:
            if cellRowData[1] != None: # We do not want empty/null values to be stored into DB
                print(cellRowData[1], cellRowData[12])  # 08:00-09:00
                insert2db(cellRowData[1], cellRowData[12], read_day, read_Sem, "08:00", "09:00")
            else:
                pass

            if cellRowData[2] != None:
               insert2db(cellRowData[2], cellRowData[13], read_day, read_Sem, "09:00", "10:00")
            else:
                pass

            if cellRowData[3] != None:
               insert2db(cellRowData[3], cellRowData[14], read_day, read_Sem, "10:00", "11:00")
            else:
                pass

            if cellRowData[4] != None:
               insert2db(cellRowData[4], cellRowData[15], read_day, read_Sem, "11:00", "12:00")
            else:
                pass

            if cellRowData[5] != None:
               insert2db(cellRowData[5], cellRowData[16], read_day, read_Sem, "12:00", "13:00")
            else:
                pass

           # Rehat / break don't need to be inserted into DB


            if cellRowData[7] != None:
              insert2db(cellRowData[7], cellRowData[18], read_day, read_Sem, "14:00", "15:00")
            else:
               pass

            if cellRowData[8] != None:
              insert2db(cellRowData[8], cellRowData[19], read_day, read_Sem, "15:00", "16:00")
            else:
               pass

            if cellRowData[9] != None:
             insert2db(cellRowData[9], cellRowData[20], read_day, read_Sem, "16:00", "17:00")
            else:
              pass

            if cellRowData[10] != None:
             insert2db(cellRowData[10], cellRowData[21], read_day, read_Sem, "17:00", "18:00")
            else:
              pass

        except Exception as e:
            print("Error cellRowData: " + str(e))


if __name__ == "__main__":

   # Read all MS Excel file (*.xls or *.xlsx) from a folder
   # Path for MS Excel files folder
   directory_path = "./"

   # Check if directory exists or not
   checkDir = os.path.exists(directory_path)

   if checkDir == True: # Folder exists
       # Define MS Excel file extension
       fileExtension = [".xls",".xlsx"]

       # Loop the whole directory including sub-folders for files with an extension of .xls or.xlsx
       i = 0
       for folder, sub_folders, file in os.walk(directory_path):
           for name in file:
               if name.endswith(tuple(fileExtension)):
                   filename_final = os.path.join(folder, name)
                   i += 1
                   print(str(i) + filename_final)
                   wb = load_workbook(filename_final)
                   # Get active sheet
                   sheet_name = wb.sheetnames
                   active_sheet = wb.active
                   sheet = wb[sheet_name[0]] # Get the first sheet

                   # Get lecturer name
                   lecturer_name = sheet["A6"].value

                   # Sunday schedule
                   readDailyData("A9","K10", "sun", "20172018-2")

                   # Get Monday schedule
                   readDailyData ("A11", "K12", "mon", "20172018-2")

                   # Get Tuesday schedule
                   readDailyData ("A13", "K14", "tue", "20172018-2")

                   # Get Wednesday schedule
                   readDailyData ("A15", "K16", "wed", "20172018-2")

                   # Get Thursday schedule
                   readDailyData("A17", "K18", "thu", "20172018-2")

               else:
                   print("\nNo MS Excel file found!\nPlease make sure all Excel file must be in the same folder.\n")

   else:
        # Folder doesn't exists
        print("\nDirectory not found!\nPlease make sure the directory is available.")



























