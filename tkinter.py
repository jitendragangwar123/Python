from tkinter import Toplevel, Button, Tk, Menu  
top = Tk()  
menubar = Menu(top)  

#Main Menu
Main= Menu(menubar, tearoff=0)  
Main.add_command(label="Shawarma($6)")  
Main.add_command(label="Chicken over rice($7)")  
Main.add_command(label="Lamb over rice($8)")  
menubar.add_cascade(label="Main", menu=Main) 


#Appetizer Menu
Appetizer= Menu(menubar, tearoff=0)  
Appetizer.add_command(label="Salad($3)") 
Appetizer.add_command(label="Soup($2)")  
menubar.add_cascade(label="Appetizer", menu=Appetizer) 

#Dessert Menu
Dessert= Menu(menubar, tearoff=0)  
Dessert.add_command(label="Conafa($4)")  
Dessert.add_command(label="Boklava($3)")  
menubar.add_cascade(label="Dessert", menu=Dessert)  
  
top.config(menu=menubar)  
top.mainloop()  