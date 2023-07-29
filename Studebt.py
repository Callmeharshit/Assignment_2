import csv

def write_info(infolist):
    with open('Info.csv', 'a', newline='') as csv_file:  # Use 'a' (append) mode to add new rows
        writer = csv.writer(csv_file)

      if csv_file.tell() == 0:
        writer.writerow(["Name", "Age", "Contact no", "E-Mail ID"])
        
      writer.writerow(infolist)
if _name_ == '_main_': 
  while True:  # Add an infinite loop to keep asking for student info
      Info = input("Enter student info (separated by spaces, e.g., Name Age Grade): ")
      print(Info)
  
      Info_list = Info.split(' ')
      print(str(Info_list))
  
      write_info(Info_list)  # Call the write_info function to save the student info to the CSV file
  
      condition_check = input("Enter Yes or No for another student: ")
      if condition_check.lower() != "yes":  # Allow any case for "Yes" (e.g., yes, YES, yEs, etc.)
          break  # Exit the loop if the user enters anything other than "Yes"
