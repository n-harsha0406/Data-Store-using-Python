import tkinter
from tkinter import ttk
from tkinter import messagebox
import pandas as pd        
import csv
import io
global dat
with open("Data.csv","r") as f:
    data=list()
def enter_data():
    accepted = accept_var.get()
    
    if accepted=="Accepted":
        # User info
        firstname = first_name_entry.get()
        lastname = last_name_entry.get()
        
        if firstname and lastname:
            title = title_combobox.get()
            age = age_spinbox.get()
            nationality = nationality_combobox.get()
            
            # Course info
            registration_status = reg_status_var.get()
            numcourses = numcourses_spinbox.get()
            numsemesters = int(numsemesters_spinbox.get())
            
            print("First name: ", firstname, "Last name: ", lastname)
            print("Title: ", title, "Age: ", age, "Nationality: ", nationality)
            print("# Courses: ", numcourses, "# Semesters: ", numsemesters)
            print("Registration status", registration_status)
            print("------------------------------------------")
            rows=[firstname,lastname,title,age,nationality,numcourses,numsemesters,registration_status]
            with open("Data.csv","a") as f:
                csv_writer=csv.writer(f)            
                csv_writer.writerow(rows)
            
        else:
            messagebox.showwarning(title="Error", message="First name and last name are required.")
    else:
        messagebox.showwarning(title= "Error", message="You have not accepted the terms")

def print_data():
    d=pd.read_csv("Data.csv") 
    print(d) 



def Edit_data():
    def Edit_data2():
        Topics=['FirstName','Lastname','Title','Age','Nationality','No_of_Courses','No_of_semesters','Resgistration_status']
        userfirstname=user_first_name_entry.get()
        userlastname=user_last_name_entry.get()
        userchoice=choice_entry.get()
        choicedata=choice_data_entry.get()
        edf=pd.read_csv("Data.csv")
        for i in edf.index:
            if (edf.loc[i,"FirstName"] == userfirstname):
                for k in edf.index:
                    if (edf.loc[k,"Lastname"] == userlastname):
                        break
        for j in range(len(Topics)):
            if userchoice==Topics[j]:
                break 
        edf.loc[k,Topics[j]]=choicedata
        print(pd.read_csv(io.StringIO(edf.to_csv(index=False))))     
      
    tab=tkinter.Tk()
    tab.title("Edit Details")
    
    frame = tkinter.Frame(tab)
    frame.pack()
    
    #editing values
    user_info_frame =tkinter.LabelFrame(frame, text="User Information",bg="#900C3F",fg='#FFC300')
    user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

    user_first_name_label = tkinter.Label(user_info_frame, text="First Name",fg='#FF5733')
    user_first_name_label.grid(row=0, column=0)
    user_last_name_label = tkinter.Label(user_info_frame, text="Last Name",fg='#FF5733')
    user_last_name_label.grid(row=0, column=1)

    user_first_name_entry = tkinter.Entry(user_info_frame)
    user_last_name_entry = tkinter.Entry(user_info_frame)
    user_first_name_entry.grid(row=1, column=0)
    user_last_name_entry.grid(row=1, column=1)
    for widget in user_info_frame.winfo_children():
        widget.grid_configure(padx=10, pady=5)
    
    #editing choice
    editing_frame =tkinter.LabelFrame(frame, text="Editing choice",bg="#900C3F",fg='#FFC300')
    editing_frame.grid(row= 1, column=0, padx=20, pady=10)
    
    choice_label = tkinter.Label(editing_frame, text="Choice",fg='#FF5733')
    choice_label.grid(row=0, column=0)
    
    choice_data_label = tkinter.Label(editing_frame, text="Correct Data",fg='#FF5733')
    choice_data_label.grid(row=1, column=0)

    choice_entry = tkinter.Entry(editing_frame)
    choice_entry.grid(row=0, column=1)
    choice_data_entry = tkinter.Entry(editing_frame)
    choice_data_entry.grid(row=1, column=1)
    
    for widget in editing_frame.winfo_children():
        widget.grid_configure(padx=30, pady=5)
    
    #button
    button=tkinter.Button(frame, text="Edit Data", command= Edit_data2, bg="#900C3F",fg='#FFC300')
    button.grid(row=2, column=0, sticky="news", padx=20, pady=2.5)
    
    
    
    
window = tkinter.Tk()
window.title("Data Entry Form")

frame = tkinter.Frame(window)
frame.pack()

# Saving User Info
user_info_frame =tkinter.LabelFrame(frame, text="User Information",bg="#900C3F",fg='#FFC300')
user_info_frame.grid(row= 0, column=0, padx=20, pady=10)

first_name_label = tkinter.Label(user_info_frame, text="First Name",fg='#FF5733')
first_name_label.grid(row=0, column=0)
last_name_label = tkinter.Label(user_info_frame, text="Last Name",fg='#FF5733')
last_name_label.grid(row=0, column=1)

first_name_entry = tkinter.Entry(user_info_frame)
last_name_entry = tkinter.Entry(user_info_frame)
first_name_entry.grid(row=1, column=0)
last_name_entry.grid(row=1, column=1)

title_label = tkinter.Label(user_info_frame, text="Title",fg='#FF5733')
title_combobox = ttk.Combobox(user_info_frame, values=["", "Mr.", "Ms.", "Dr."])
title_label.grid(row=0, column=2)
title_combobox.grid(row=1, column=2)

age_label = tkinter.Label(user_info_frame, text="Age",fg='#FF5733')
age_spinbox = tkinter.Spinbox(user_info_frame, from_=18, to=110)
age_label.grid(row=2, column=0)
age_spinbox.grid(row=3, column=0)

nationality_label = tkinter.Label(user_info_frame, text="Nationality",fg='#FF5733')
nationality_combobox = ttk.Combobox(user_info_frame, values=["Africa", "Antarctica", "Asia", "Europe", "North America", "Oceania", "South America"])
nationality_label.grid(row=2, column=1)
nationality_combobox.grid(row=3, column=1)

for widget in user_info_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Saving Course Info
courses_frame = tkinter.LabelFrame(frame,text="Course Information",bg="#900C3F",fg='#FFC300')
courses_frame.grid(row=1, column=0, sticky="news", padx=20, pady=10)

registered_label = tkinter.Label(courses_frame, text="Registration Status",fg='#FF5733')

reg_status_var = tkinter.StringVar(value="Not Registered")
registered_check = tkinter.Checkbutton(courses_frame, text="Currently Registered",
                                       variable=reg_status_var, onvalue="Registered", offvalue="Not registered",fg='#FF5733')

registered_label.grid(row=0, column=0)
registered_check.grid(row=1, column=0)

numcourses_label = tkinter.Label(courses_frame, text= "# Completed Courses",fg='#FF5733')
numcourses_spinbox = tkinter.Spinbox(courses_frame, from_=0, to='infinity')
numcourses_label.grid(row=0, column=1)
numcourses_spinbox.grid(row=1, column=1)

numsemesters_label = tkinter.Label(courses_frame, text="# Semesters",fg='#FF5733')
numsemesters_spinbox = tkinter.Spinbox(courses_frame, from_=0, to="infinity")
numsemesters_label.grid(row=0, column=2)
numsemesters_spinbox.grid(row=1, column=2)

for widget in courses_frame.winfo_children():
    widget.grid_configure(padx=10, pady=5)

# Accept terms
terms_frame = tkinter.LabelFrame(frame, text="Terms & Conditions",bg="#900C3F",fg='#FFC300')
terms_frame.grid(row=2, column=0, sticky="news", padx=20, pady=10)

accept_var = tkinter.StringVar(value="Not Accepted")
terms_check = tkinter.Checkbutton(terms_frame, text= "I accept the terms and conditions.",
                                  variable=accept_var, onvalue="Accepted", offvalue="Not Accepted",fg='#FF5733')
terms_check.grid(row=0, column=0)

#Saving data
save_frame=tkinter.LabelFrame(frame, text="Options",bg="#900C3F",fg='#FFC300')
save_frame.grid(row=3, column=0, sticky="news", padx=20, pady=10)
# Button
button = tkinter.Button(save_frame, text="Enter Data", command= enter_data,bg="#900C3F",fg='#FFC300')
button.grid(row=0, column=0, sticky="news", padx=20, pady=10)

#print button
button1 = tkinter.Button(save_frame, text="Print Data", command= print_data, bg="#900C3F",fg='#FFC300')
button1.grid(row=0, column=1, sticky="news", padx=20, pady=10)

#edit details
button2 = tkinter.Button(save_frame, text="Edit Data", command= Edit_data, bg="#900C3F",fg='#FFC300')
button2.grid(row=0, column=2, sticky="news", padx=20, pady=10)

for widget in save_frame.winfo_children():
    widget.grid_configure(padx=50, pady=2.5)
    
window.mainloop()
