import os
from tkinter import *
from tkinter import messagebox
import random
import json
import pyperclip
from dotenv import load_dotenv
load_dotenv()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for char in range(nr_letters)]
    password_list1 = [random.choice(symbols) for s in range(nr_symbols)]
    password_list2 = [random.choice(numbers) for n in range(nr_numbers)]
    final_list = password_list1 + password_list2 + password_list
    random.shuffle(final_list)

    passcode= "".join(final_list)
    entry3.insert(0,passcode)
    pyperclip.copy(passcode) #for directly coping passowrod when it is generated
# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    web_entry=entry1.get()
    mail_entry=entry2.get()
    password_entry=entry3.get()
    new_data={
        web_entry:{
            "email":mail_entry,
            "password":password_entry,
        }
    }
    if len(web_entry)==0 or len(password_entry)==0:
        messagebox.showinfo(title="ops",message="Please do not leave any fields empty")
    else:
        # is_ok=messagebox.askokcancel(title=web_entry,message=f"these are the details entered:\nEmail: {mail_entry}"
        #                                                       f"\nPassword: {password_entry} \n Is it ok to ssave?")
        # if is_ok:
        try:
            with open("record.json","r") as file:
                #reading old data
                data=json.load(file)
        except FileNotFoundError:
            with open("record.json","w") as file:
                json.dump(new_data,file,indent=4)
        else:
            #updating
            data.update(new_data)

            with open("record.json","w") as file:
                #saving updated data
                json.dump(data,file,indent=4)
        finally:
            entry1.delete(0,END)
            entry3.delete(0,END)

def find_password():
    web_entry = entry1.get()
    try:
        with open("record.json","r") as file:
            data=json.load(file)
        if web_entry in data:
            messagebox.showinfo(title=web_entry,message=f"Email:{data[web_entry]["email"]}\n"
                                                    f"Password:{data[web_entry]['password']}")
        else:
            messagebox.showinfo(title="oops",message="No details for the website exists")

    except FileNotFoundError:
        messagebox.showinfo(title="Error",message="No data file found")



# ---------------------------- UI SETUP ------------------------------- #
# window = Tk()
# window.title("Password Manager")
# window.config(padx=50,pady=50)
#
# canvas=Canvas(height=200, width=200)
# lock=PhotoImage(file="logo.png")
# canvas.create_image(100,100,image=lock)
# canvas.grid(row=0,column=1)
#
# web=Label(text="Website:",font=("Times New Roman",12))
# web.grid(row=1,column=0)
#
# mail=Label(text="Email/Username:",font=("Times New Roman",12))
# mail.grid(row=2,column=0)
#
# password=Label(text="Password:",font=("Times New Roman",12))
# password.grid(row=3,column=0)
#
# entry1=Entry(width=21)
# entry1.focus()#cursor will be in this entry box
# entry1.grid(row=1,column=1)
#
# entry2=Entry(width=25)
# entry2.insert(0,"krish260659@gmail.com")
# entry2.grid(row=2,column=1,columnspan=2)
#
# entry3=Entry(width=21)
# entry3.grid(row=3,column=1)
#
# button1=Button(text="Generate Password",width=20,command=generate_password)
# button1.grid(row=3,column=3)
#
# button2=Button(text="Add",width=60,command=add)
# button2.grid(row=4,column=1,columnspan=3)
#
# button3=Button(text="Search",width=20,command=find_password)
# button3.grid(row=1,column=3)
#
#
# window.mainloop()
import customtkinter as ctk
from PIL import Image

# Initialize the main window using CTk
window = ctk.CTk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Set the appearance mode (Optional: "System", "Dark", "Light")
ctk.set_appearance_mode("dark")

# For images in CTk, it's best to use CTkImage for high-DPI scaling
# Replace "logo.png" with your actual file path
logo_image = ctk.CTkImage(light_image=Image.open("logo.png"),
                                  dark_image=Image.open("logo.png"),
                                  size=(200, 200))

canvas_label = ctk.CTkLabel(window, image=logo_image, text="")
canvas_label.grid(row=0, column=1, pady=20)

# Labels
web = ctk.CTkLabel(window, text="Website:", font=("Times New Roman", 14))
web.grid(row=1, column=0, sticky="e", padx=10, pady=5)

mail = ctk.CTkLabel(window, text="Email/Username:", font=("Times New Roman", 14))
mail.grid(row=2, column=0, sticky="e", padx=10, pady=5)

password = ctk.CTkLabel(window, text="Password:", font=("Times New Roman", 14))
password.grid(row=3, column=0, sticky="e", padx=10, pady=5)

# Entries
entry1 = ctk.CTkEntry(window, width=200)
entry1.focus()
entry1.grid(row=1, column=1, pady=5)

entry2 = ctk.CTkEntry(window, width=380)
entry2.insert(0, os.environ["MAIL"])
entry2.grid(row=2, column=1, columnspan=2, pady=5)

entry3 = ctk.CTkEntry(window, width=200)
entry3.grid(row=3, column=1, pady=5)

# Buttons
button3 = ctk.CTkButton(window, text="Search", width=150, command=find_password)
button3.grid(row=1, column=2, padx=5)

button1 = ctk.CTkButton(window, text="Generate Password", width=150, command=generate_password)
button1.grid(row=3, column=2, padx=5)

button2 = ctk.CTkButton(window, text="Add", width=380, command=add)
button2.grid(row=4, column=1, columnspan=2, pady=20)

window.mainloop()