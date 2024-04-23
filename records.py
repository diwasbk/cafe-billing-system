from tkinter import *
root = Tk()
import sqlite3
root.title("Records")
root.geometry("1200x1200")
root.resizable(0, 0)

#Labels Bar
line_label = Label(root, text="__________________________________________________________________________________________________________________________________________________________________________________________", font=("Arial", 16, "bold"),fg="green")
line_label.place(y=25)

order_id_label = Label(root, text="Order Id ", font=("Arial", 12, "bold"),fg="blue")
order_id_label.grid(row=1, column=1,padx=40,pady=20)

tea_label = Label(root, text="Tea  ", font=("Arial", 12, "bold"),fg="blue")
tea_label.grid(row=1, column=2,padx=20,pady=20)

momo_label = Label(root, text="Momo ", font=("Arial", 12, "bold"),fg="blue")
momo_label.grid(row=1, column=3,padx=20,pady=20)

grilled_chicken_label = Label(root, text="Grilled Chicken  ", font=("Arial", 12, "bold"),fg="blue")
grilled_chicken_label.grid(row=1, column=4,padx=20,pady=20)

coke_label = Label(root, text="Coke ", font=("Arial", 12, "bold"),fg="blue")
coke_label.grid(row=1, column=5,padx=20,pady=20)

coffee_label = Label(root, text="Coffee", font=("Arial", 12, "bold"),fg="blue")
coffee_label.grid(row=1, column=6,padx=20,pady=20)

burger_label = Label(root, text="Burger", font=("Arial", 12, "bold"),fg="blue")
burger_label.grid(row=1, column=7,padx=20,pady=20)

date_label = Label(root, text="Date", font=("Arial", 12, "bold"),fg="blue")
date_label.grid(row=1, column=8,padx=50,pady=20)

discount_label = Label(root, text="Discount", font=("Arial", 12, "bold"),fg="blue")
discount_label.grid(row=1, column=9,padx=20,pady=20)

total_label = Label(root, text="Total", font=("Arial", 12, "bold"),fg="blue")
total_label.grid(row=1, column=10,padx=20,pady=20)



#Establishing database
conn = sqlite3.connect('cafe.db')
cursor = conn.cursor()
cursor.execute("SELECT * FROM records")
details = cursor.fetchall()
num=2
for i in details:
    order_id_label=Label(root, text=i[0],font=("Arial", 10, "bold"))
    order_id_label.grid(row=num,column=1,padx=2,pady=5)

    tea_label=Label(root, text=i[1],font=("Arial", 10, "bold"))
    tea_label.grid(row=num,column=2,padx=2,pady=5)

    momo_label=Label(root, text=i[2],font=("Arial", 10, "bold"))
    momo_label.grid(row=num,column=3,padx=2,pady=5)

    grilled_chicken_label=Label(root, text=i[3],font=("Arial", 10, "bold"))
    grilled_chicken_label.grid(row=num,column=4,padx=2,pady=5)

    coke_label=Label(root, text=i[4],font=("Arial", 10, "bold"))
    coke_label.grid(row=num,column=5,padx=2,pady=5)

    coffee_label=Label(root, text=i[5],font=("Arial", 10, "bold"))
    coffee_label.grid(row=num,column=6,padx=2,pady=5)

    burger_label=Label(root, text=i[6],font=("Arial", 10, "bold")) 
    burger_label.grid(row=num,column=7,padx=2,pady=5)

    date_label = Label(root, text=i[7], font=("Arial", 12, "bold"), fg="gray20")
    date_label.grid(row=num, column=8,padx=2,pady=5)

    discount_label = Label(root, text=i[8], font=("Arial", 12, "bold"),fg="green")
    discount_label.grid(row=num, column=9,padx=2,pady=5)

    total_label = Label(root, text=i[9], font=("Arial", 12, "bold"),fg="green")
    total_label.grid(row=num, column=10,padx=2,pady=5)

    num=num+1

conn.commit()
conn.close()

root.mainloop()
