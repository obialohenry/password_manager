from tkinter import * # type: ignore
from tkinter import messagebox
import random
import pyperclip
import json

SPACING = 50
CANVAS_SIZE = 200
IMAGE_SIZE = 100
# --------------------------- PASSWORD GENERATOR ---------------------------- #

def generate_password():
  """"""
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = [random.choice(letters) for _ in range(nr_letters)]
  password_list += [random.choice(symbols) for _ in range(nr_symbols)]
  password_list += [random.choice(numbers) for _ in range(nr_numbers)]

  random.shuffle(password_list)

  password = "".join(password_list)
  password_entry.insert(0,password)
  pyperclip.copy(password)
# --------------------------- SAVE PASSWORD ---------------------------- #

def save_details():
  """"""
  website = website_entry.get().title()
  email = email_username_entry.get()
  password = password_entry.get()
  data = {
    website:{
      "email": email,
      "password": password
    }
  }

  if not website or not password:
    messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    return
  
  is_ok = messagebox.askokcancel(title=website,message=f"These are the details entered: \nEmail: {email} "
                         f"\nPassword: {password} \nIs it ok to save?",icon="question")
  if not is_ok:
    return

  try:
    with open("data.json",mode="r") as data_file:
     new_data = json.load(data_file)
  except FileNotFoundError:
    with open("data.json",mode="w") as data_file:
      json.dump(data,data_file,indent=4)
  else:
    new_data.update(data)
    with open("data.json",mode="w") as data_file:
      json.dump(new_data, data_file, indent=4)
  finally:
    website_entry.delete(0,END)
    password_entry.delete(0,END)
# --------------------------- FIND PASSWORD ---------------------------- #

def find_password():
  """"""
  website = website_entry.get().title()
  if not website :
    messagebox.showinfo(title="Oops", message="Please fill the website field!")
    return
  
  with open("data.json",mode="r") as data_file:
     data = json.load(data_file)
  
  try:
    messagebox.showinfo(title="", message=f"Email: {data[website]["email"]}\nPassword: {data[website]["password"]}")
  except KeyError:
    messagebox.showinfo(title="", message=f"No Data File Found.")

# --------------------------- UI SETUP ---------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=SPACING,pady=SPACING)

canvas = Canvas(width=CANVAS_SIZE,height=CANVAS_SIZE,highlightthickness=0)
canvas_img = PhotoImage(file="./asset/logo.png")
canvas.create_image(IMAGE_SIZE,IMAGE_SIZE,image= canvas_img)
canvas.grid(column=1,row=0)

website_label = Label(text="Website:")
website_label.grid(column=0,row=1)

website_entry = Entry(width=22)
website_entry.grid(column=1,row=1)
website_entry.focus()

search_button = Button(text="Search",width=13,command=find_password)
search_button.grid(column=2,row=1)

email_username_label = Label(text="Email/Username:")
email_username_label.grid(column=0,row=2)

email_username_entry = Entry(width=40)
email_username_entry.grid(column=1,row=2,columnspan=2)
email_username_entry.insert(0,"obilaorchisomebi123@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0,row=3)

password_entry = Entry(width=22)
password_entry.grid(column=1,row=3)

generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(column=2,row=3)

add_button = Button(text="Add",width=34,command=save_details)
add_button.grid(column=1,row=4,columnspan=2)





window.mainloop()