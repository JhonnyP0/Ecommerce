import mysql.connector
import tkinter as tk
from tkinter import simpledialog

root=tk.Tk()
root.title("ItemPlacer")
root.geometry("500x300")

AppFrame=tk.Frame()
LogFrame=tk.Frame()
LogFrame.pack()
AppFrame.pack()


config = {
    "host": "localhost",
    "user": "root",
    "password": "mypass",
    "database": "ecom",
    "port":"5200"
}

class sqlops:
    def connection(self):
        try:
            self.conn = mysql.connector.connect(**config)
            self.sqlcursor = self.conn.cursor()
            ConStateLab.config(text="connected",fg="green")
            so.sqlfetch()
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            ConStateLab.config(text=err, fg="red")

    def sqlfetch(self):
            item_list.delete(0, tk.END)
            query="SELECT * FROM items"
            so.sqlcursor.execute(query)
            result=so.sqlcursor.fetchall()
            AppFrame.tkraise()

            for row in result:
                item_list.insert(tk.END, row)

    def additem(self):
        varo=simpledialog.askstring("Item name","Item name: ")
        vart=simpledialog.askstring("Item price","Item price: ")
        new_item=(varo,vart)
        query="INSERT INTO items (name,price) VALUES (%s,%s)"
        self.sqlcursor.execute(query,new_item)
        self.conn.commit()
        
    def removeitem(self):
        selected_item=item_list.curselection()
        itemid=item_list.get(selected_item)
        query="DELETE FROM items WHERE id = %s",(6,)
        self.sqlcursor.execute("DELETE FROM items WHERE id = %s",(itemid[0],))
        query="ALTER TABLE items AUTO_INCREMENT = 1;"
        self.sqlcursor.execute(query)
        self.conn.commit()
        

        
so=sqlops()

item_list = tk.Listbox(AppFrame, selectmode=tk.SINGLE)
item_list.pack()

AddBut=tk.Button(AppFrame,text="Add",command=lambda:[so.additem(),so.sqlfetch()])
AddBut.pack()
RemBut=tk.Button(AppFrame,text="Remove",command=lambda:[so.removeitem(),so.sqlfetch()])
RemBut.pack()

ConStateLab = tk.Label(LogFrame,text="---", fg="orange")
ConStateLab.pack()

ConBut=tk.Button(LogFrame,text="connect", command=so.connection)
ConBut.pack()

root.mainloop()