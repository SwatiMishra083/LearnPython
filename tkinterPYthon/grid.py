
from tkinter import Tk, Label, Entry;
mainwin=Tk()
mainwin.configure(bg="yellow");
mainwin.title("Swati's title bar")
mainwin.geometry("500x300")
mainwin.configure(cols)
heading=Label (text="REgistration form ", bg="red", fg="black");
heading.grid(row="0", column="0",columnspan="2")

heading=Label (text="First name", bg="yellow", fg="black");
heading.grid(row="1", column="0")

heading=Entry ( bg="yellow", fg="black");
heading.grid(row="1", column="1")

mainwin.mainloop()

