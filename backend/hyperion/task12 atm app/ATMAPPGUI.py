from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import Font

root = Tk()
root.geometry('480x260+400+200')
root.title("ATM app")
style = ttk.Style()
window = Toplevel(root)
winwithdraw = Toplevel(root)
windeposit = Toplevel(root)
window.withdraw()
winwithdraw.withdraw()
windeposit.withdraw()

class Account:

	def button_press(self,value):
		entry_val = self.number_entry.get()
		entry_val += value
		self.number_entry.delete(0, "end")
		self.number_entry.insert(0, entry_val)
		if int(entry_val) < 1 or int(entry_val) > 8:
			messagebox.showinfo("Error", "Invalid ID number. Please re-enter.")
			self.number_entry.delete(0, "end")
		else:
			self.main_menu(value)

	def get_name(self,value):
		style.configure("TLabel", 
						font ="Arial 20",
						padding = 10)
		return "What would you like to do {}?".format(accountholders[value].name)

	def main_menu(self,userID):
		window.deiconify()
		root.withdraw()
		window.geometry('420x300+420+200')
		window.title("Banking Options")
		label_greeting = ttk.Label(window,text = self.get_name(int(userID))).grid(row=0,column=0) 
		self.checkbalance = ttk.Button(window, text="Check Balance",
			command=lambda: self.get_balance(int(userID))).grid(row=1,column=0)
		self.withdrawbutton = ttk.Button(window, text="Withdraw",
			command=lambda: self.withdraw_page(int(userID))).grid(row=2,column=0)
		self.depostbutton = ttk.Button(window, text="Deposit",
			command=lambda: self.deposit_page(int(userID))).grid(row=3,column=0)
		self.logout = ttk.Button(window, text="Log Out",
			command=lambda: self.close()).grid(row=4,column=0)

	def close(self):
		root.deiconify()
		window.withdraw()
		windeposit.withdraw()
		winwithdraw.withdraw()
		self.number_entry.delete(0, "end")

	def get_balance(self,userID):
		style.configure("TMessage", 
						font ="Serif 30",
						padding = 10,
						fg="#ffdddd",
						relief = SUNKEN)
		messagebox.showinfo("Balance", "Your balance is: " + str(accountholders[userID].balance))

	def deposit_page(self,userID):
		window.withdraw()
		windeposit.deiconify()
		windeposit.geometry('400x270+420+200')
		windeposit.title("Withdraw")
		style.configure("TLabel", 
						font ="Arial 20",
						padding = 10)
		label = ttk.Label(windeposit,text="Choose how much to deposit.").grid(row=0,column=0)	

		button100 = ttk.Button(windeposit, text = "$100",
			command=lambda: self.deposit(userID,"100")).grid(row=1,column=0)
		button200 = ttk.Button(windeposit, text = "$200",
			command=lambda: self.deposit(userID,"200")).grid(row=2,column=0)
		button300 = ttk.Button(windeposit, text = "$300",
			command=lambda: self.deposit(userID, "300")).grid(row=3,column=0)
		mainMenu = ttk.Button(windeposit, text = "Main Menu",
			command=lambda: self.main_menu(userID)).grid(row=4,column=0)

	def withdraw_page(self,userID):
		window.withdraw()
		winwithdraw.deiconify()
		winwithdraw.geometry('400x270+420+200')
		winwithdraw.title("Withdraw")
		style.configure("TLabel", 
						font ="Arial 20",
						padding = 10)
		label = ttk.Label(winwithdraw,text="Choose how much to withdraw.").grid(row=0,column=0)	

		button100 = ttk.Button(winwithdraw, text = "$100",
			command=lambda: self.withdraw(userID,"100")).grid(row=1,column=0)
		button200 = ttk.Button(winwithdraw, text = "$200",
			command=lambda: self.withdraw(userID,"200")).grid(row=2,column=0)
		button300 = ttk.Button(winwithdraw, text = "$300",
			command=lambda: self.withdraw(userID, "300")).grid(row=3,column=0)
		mainMenu = ttk.Button(winwithdraw, text = "Main Menu",
			command=lambda: self.main_menu(userID)).grid(row=4,column=0)

	def deposit(self,userID, amount):
		accountholders[userID].balance = accountholders[userID].balance + int(amount)
		messagebox.showinfo("Balance","Your new balance is " + str(accountholders[userID].balance))

	def withdraw(self,userID, amount):
		if int(amount) > accountholders[userID].balance:
			messagebox.showinfo("Balance","Insufficient funds. Your balance is: " + str(accountholders[userID].balance) + "\nReturning to Main Menu") 
			self.main_menu(userID)
		else:
			accountholders[userID].balance = accountholders[userID].balance - int(amount)
			messagebox.showinfo("Balance","Your remaining balance is " + str(accountholders[userID].balance))

	def __init__(self,root,name,idNum,balance):

		self.idNum = idNum
		self.balance = balance
		self.name = name 
		
		self.entry_value = StringVar(root, value = "")

		style = ttk.Style()

		style.configure("TButton", 
						font ="Serif 16",
						background="white",
						padding = 10,
						foreground = "blue",
						relief = "SUNKEN")

		style.configure("TEntry", 
						font ="Serif 20",
						padding = 10)

		style.configure("TLabel", 
						font ="Arial 20",
						padding = 10)
		label = ttk.Label(root,text="Enter your ID number.").grid(row=0,columnspan=3)

		self.number_entry = ttk.Entry(root,
						textvariable = self.entry_value, width = 50)

		self.number_entry.grid(row=1,columnspan=3)

		self.button7 = ttk.Button(root,text="7",
			command=lambda: self.button_press("7")).grid(row=2,column=0)

		self.button8 = ttk.Button(root, text="8",
			command=lambda: self.button_press("8")).grid(row=2,column=1)

		self.button9 = ttk.Button(root, text="9",
			command=lambda: self.button_press("9")).grid(row=2,column=2)

		self.button4 = ttk.Button(root, text="4",
			command=lambda: self.button_press("4")).grid(row=3,column=0)

		self.button5 = ttk.Button(root, text="5",
			command=lambda: self.button_press("5")).grid(row=3,column=1)

		self.button6 = ttk.Button(root, text="6",
			command=lambda: self.button_press("6")).grid(row=3,column=2)

		self.button1 = ttk.Button(root, text="1",
			command=lambda: self.button_press("1")).grid(row=4,column=0)

		self.button2 = ttk.Button(root, text="2",
			command=lambda: self.button_press("2")).grid(row=4,column=1)

		self.button3 = ttk.Button(root, text="3",
			command=lambda: self.button_press("3")).grid(row=4,column=2)


idNum = 0
balance = 100
amount = 0
A0 = Account (root,"None",0,0)
A1 = Account (root,"Sue",1,100)
A2 = Account(root,"Meg",2,150)
A3 = Account(root,"Dan",3,150)
A4 = Account(root,"Bob",4,150)
A5 = Account(root,"Sara",5,150)
A6 = Account(root,"Al",6,150)
A7 = Account(root,"Mark",7,150)
A8 = Account(root,"Mike",8,150)
A9 = Account(root,"Dwain",9,150)

accountholders = [A0,A1,A2,A3,A4,A5,A6,A7,A8,A9]

root.mainloop()


