import mysql.connector
import tkinter as tk

root=tk.Tk()
root.title("ItemPlacer")
root.geometry("600x600")

AppFrame=tk.Frame()
LogFrame=tk.Frame()
LogFrame.pack()
AppFrame.pack()


config = {
    "host": "localhost",
    "user": "root",
    "password": "my-secret-pw",
    "database": "ecom"
}


def connection():
    try:
        
        conn = mysql.connector.connect(**config)
        sqlcursor = conn.cursor()
        ConStateLab.config(text="connected",fg="green")
        query="SELECT * FROM items"
        sqlcursor.execute(query)
        result=sqlcursor.fetchall()
        AppFrame.tkraise()
        item_list = tk.Listbox(AppFrame, selectmode=tk.SINGLE)
        item_list.grid(row=2,column=1)

        for row in result:
            item_list.insert(tk.END, row)
        
        AddBut=tk.Button(AppFrame)
        AddBut.grid(row=2,column=1)
        RemBut=tk.Button(AppFrame)
        RemBut.grid(row=2,column=1)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        ConStateLab.config(text=err, fg="red")
        

ConStateLab = tk.Label(LogFrame,text="---", fg="orange")
ConStateLab.grid(row=1,column=1)

ConBut=tk.Button(LogFrame,text="connect", command=connection)
ConBut.grid(row=1,column=2)

root.mainloop()