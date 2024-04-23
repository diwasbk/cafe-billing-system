from tkinter import*
from PIL import ImageTk, Image
from tkinter.ttk import Combobox
from tkinter import messagebox
import datetime
import sqlite3
root =Tk()
root.title("the urban cafe and krispy chicken")
root.geometry("1000x600")
root.resizable(False, False)

#Creating Database and Table
conn = sqlite3.connect('cafe.db')
cursor = conn.cursor()
cursor.execute('''
          CREATE TABLE IF NOT EXISTS records (
              order_id TEXT PRIMARY KEY,
              tea INT,
              momo TEXT,
              grilled_chicken TEXT,
              coke TEXT,
              coffee TEXT,
              burger TEXT,
              date INT,
              discount REAL DEFAULT 0.0,
              total INT
          )
          ''')
conn.commit()
conn.close()

#Heading Label
cafe_name = Label(root, text="the urban cafe and crispy chicken", font="Arial 18 bold", fg="#4CAF50")
cafe_name.place(x=120, y=2)

#Adding images
image1 = Image.open('tea.png')
resized_image = image1.resize((150, 150))
img1 = ImageTk.PhotoImage(resized_image)
label = Label(root, image=img1)
label.place(x= 50, y=50)


image2= Image.open('momo.png')
resized_image = image2.resize((150, 150))
img2 = ImageTk.PhotoImage(resized_image)
label = Label(root, image=img2)
label.place(x = 240, y=50)


image3= Image.open('grilledchicken.png')
resized_image = image3.resize((150, 150))
img3 = ImageTk.PhotoImage(resized_image)
label = Label(root, image=img3)
label.place(x = 440, y=50)


image4= Image.open('coke.png')
resized_image = image4.resize((150, 150))
img4 = ImageTk.PhotoImage(resized_image)
label = Label(root, image=img4)
label.place(x = 50, y=300)


image5= Image.open('coffee.png')
resized_image = image5.resize((150, 150))
img5 = ImageTk.PhotoImage(resized_image)
label = Label(root, image=img5)
label.place(x = 240, y=300)


image6= Image.open('burger.png')
resized_image = image6.resize((150, 150))
img6 = ImageTk.PhotoImage(resized_image)
label = Label(root, image=img6)
label.place(x = 440, y=300)


#Function to calculate total amount
def calculate():
    order_id = order_id_entry.get()
    tea = int(tea_combobox.get())
    momo = int(momo_combobox.get())
    grilled_chicken = int(grilled_chicken_combobox.get())
    coke = int(coke_combobox.get())
    coffee = int(coffee_combobox.get())
    burger = int(burger_combobox.get())
    discount = float(0)
    bill = (tea*50)+(momo*200)+(grilled_chicken*500)+(coke*50)+(coffee*100)+(burger*300)
    total_bill = bill-discount

    #Making frames and adding labels

    bill_frame1 = Frame(root, width=300, height=600, bg="white")
    bill_frame1.place(x=650, y=200)

    bill_frame2 = Frame(root, width=300, height=600, bg="#4CAF50")
    bill_frame2.place(x=650, y=400)

    cafe_name = Label(bill_frame1, text= "the urban cafe and crispy chicken", font="Arial 12 bold", fg="#4CAF50", bg="white")
    cafe_name.place(x=15, y=10)

    date_label = Label(bill_frame1, text="Date:",font="Arial 10 bold", fg="gray20", bg="white")
    date_label.place(x=50, y=50)

    bill_date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    bill_date_label = Label(bill_frame1, text= bill_date, font="Arial 10 bold", fg="gray20", bg="white")
    bill_date_label.place(x=90, y=50)  

    order_id_label = Label(bill_frame1, text="Id:", font="Arial 10 bold", fg="gray20", bg="white")
    order_id_label.place(x=50, y=80)

    order_id_ = Label(bill_frame1, text= order_id, font="Arial 10 bold", fg="gray20", bg="white")
    order_id_.place(x=70, y=80)

    discount_label = Label(bill_frame1, text="Discount:", font="Arial 10 bold", fg="gray20", bg="white")
    discount_label.place(x=50, y=110)

    discount_amount = Label(bill_frame1, text=discount, font="Arial 10 bold", fg="gray20", bg="white")
    discount_amount.place(x=115, y=110)

    total_bill_label = Label(bill_frame1, text="Total: $", font="Arial 10 bold", fg="gray20", bg="white")
    total_bill_label.place(x=200, y=140)

    total_bill_amount = Label(bill_frame1, text=total_bill, font="Arial 10 bold", fg="gray20", bg="white")
    total_bill_amount.place(x=250, y=140)

    #Saving bill
    def save_bill():
        if order_id_entry.get() == "":
            messagebox.showerror("Error", "Please generate order id.")
        else:
            # Inserting data into SQLite database
            conn = sqlite3.connect('cafe.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO records (order_id, tea, momo, grilled_chicken, coke, coffee, burger, date, discount, total) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (order_id, tea, str(momo), str(grilled_chicken), str(coke), str(coffee), str(burger), datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'), discount, total_bill))
            conn.commit()
            conn.close()
            messagebox.showinfo("Saved", "Saved Successfully!")

    #Clearing bill
    def clear_bill():
        order_id_entry.delete(0, END)
        cafe_name.place(x=15, y= 30)
        date_label.config(text="")
        bill_date_label.config(text="")
        order_id_label.config(text="")
        order_id_.config(text="")
        discount_label.config(text="")
        discount_amount.config(text="")
        total_bill_label.config(text="")
        total_bill_amount.config(text="")
        tea_combobox.set("0")
        momo_combobox.set("0")
        grilled_chicken_combobox.set("0")
        coke_combobox.set("0")
        coffee_combobox.set("0")
        burger_combobox.set("0")

    #save bill button
    save_bill_button = Button(bill_frame2, text = "Save ",font="Arial 10 bold", bg="blue", fg="white", width=10, cursor="hand2", command=save_bill)
    save_bill_button.place(x=40, y=80)
    #clear bill button
    clear_bill_button = Button(bill_frame2, text = "Clear",font="Arial 10 bold", bg="red", fg="white", width=10, cursor="hand2", command=clear_bill)
    clear_bill_button.place(x=170, y=80) 

#Generating order id randomly
def generate_order_id():
    import random
    import string
    random_number = ''.join(str(random.randint(0, 9))for i in range(3))
    alphabet = random.choice(string.ascii_uppercase)
    order_id = alphabet+(random_number)
    order_id_entry.delete(0, END)
    order_id_entry.insert(0,order_id)

#Price Label
tea_price = Label(root, text="$50", font="Arial 12 bold", fg="black")
tea_price.place(x=100, y= 210)

momo_price = Label(root, text="$200", font="Arial 12 bold", fg="black")
momo_price.place(x=300, y= 210)

grilled_chicken_price = Label(root, text="$500", font="Arial 12 bold", fg="black")
grilled_chicken_price.place(x=500, y= 210)

coke_price = Label(root, text="$50", font="Arial 12 bold", fg="black")
coke_price.place(x=100, y= 460)

coffee_price = Label(root, text="$100", font="Arial 12 bold", fg="black")
coffee_price.place(x=300, y= 460)

burger_price = Label(root, text="$300", font="Arial 12 bold", fg="black")
burger_price.place(x=500, y= 460)


#ComboBox
tea_combobox = Combobox(root, values=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], width=22, state="readonly")
tea_combobox.place(x=50, y=240)
tea_combobox.set(0)

momo_combobox = Combobox(root, values=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], width=22, state="readonly")
momo_combobox.place(x=240, y=240)
momo_combobox.set(0)

grilled_chicken_combobox = Combobox(root, values=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], width=22, state="readonly")
grilled_chicken_combobox.place(x=440, y=240)
grilled_chicken_combobox.set(0)

coke_combobox = Combobox(root, values=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], width=22, state="readonly")
coke_combobox.place(x=50, y=490)
coke_combobox.set(0)

coffee_combobox = Combobox(root, values=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], width=22, state="readonly")
coffee_combobox.place(x=240, y=490)
coffee_combobox.set(0)

burger_combobox = Combobox(root, values=[0,1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], width=22, state="readonly")
burger_combobox.place(x=440, y=490)
burger_combobox.set(0)

#Bill Frame
bill_frame0 = Frame(root, width=300, height=600, bg="#4CAF50")
bill_frame0.place(x=650, y=0)

#customer name label and entry
order_id_label = Label(bill_frame0, text="Order ID: ",font="Arial 12 bold", bg="#4CAF50", fg="gray20")
order_id_label.place(x=10, y= 50)

order_id_entry = Entry(bill_frame0)
order_id_entry.place(x=90, y=50)

# calculate button
calculate_button = Button(bill_frame0, text = "Calculate",font="Arial 10 bold", bg="white", fg="gray20", width=10, cursor="hand2", command=calculate)
calculate_button.place(x=155, y=100)


#order button
order_button = Button(bill_frame0, text = "Order",font="Arial 10 bold", bg="white", fg="gray20", width=10, cursor="hand2", command=generate_order_id)
order_button.place(x=55, y=100)

#retrieving the records from table
def view_records():
    import records

#View Records button
view_records_button = Button(bill_frame0, text = "View",font="Arial 10 bold", bg="white", fg="gray20", width=10, cursor="hand2", command= view_records)
view_records_button.place(x=100, y=150)

#developer
developer = Label(root, text="© 2024 Diwas Bk", font="Arial 12 bold", fg="gray20")
developer.place(x=250, y=550)

root.mainloop()
