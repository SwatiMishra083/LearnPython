
from tkinter import Tk, Label, Entry;
mainwin=Tk()
mainwin.configure(bg="yellow");
mainwin.title("Swati's title bar")
mainwin.geometry("500x300")

heading=Label (text="REgistration form ", bg="red", fg="black");
heading.place(x="200", y="50")

heading=Label (text="First name", bg="yellow", fg="black");
heading.place(x="20", y="90")

heading=Entry ( bg="yellow", fg="black");
heading.place(x="100", y="90")

mainwin.mainloop()

