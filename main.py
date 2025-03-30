import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("300x400")
        self.create_widgets()

    def create_widgets(self):
        self.header = tk.Label(self.root, text="💲 Currency Converter 🤑", font=("Arial", 24))
        self.header.pack(pady=20)

        self.select = tk.Label(self.root, text="Select currency to convert from:", font=("Arial", 16))
        self.select.pack()

        self.usdtoeur = tk.IntVar()
        self.usdtoeurbtn = tk.Checkbutton(self.root, text="💵USD to EUR💶", variable=self.usdtoeur)
        self.usdtoeurbtn.pack(pady=10)

        self.usdtogbp = tk.IntVar()
        self.usdtogbpbtn = tk.Checkbutton(self.root, text="💵USD to GBP💷", variable=self.usdtogbp)
        self.usdtogbpbtn.pack()

        self.usdtocad = tk.IntVar()
        self.usdtocadbtn = tk.Checkbutton(self.root, text="💵USD to CAD💰", variable=self.usdtocad)
        self.usdtocadbtn.pack(pady=10)

        self.usdtojpy = tk.IntVar()
        self.usdtojpybtn = tk.Checkbutton(self.root, text="💵USD to JPY💴", variable=self.usdtojpy)
        self.usdtojpybtn.pack()

        self.usdamtlabel = tk.Label(self.root, text="💵 How many USD will you convert? 💵", font=("Arial", 16))
        self.usdamtlabel.pack(pady=10)

        self.usdamt = tk.Entry(self.root, width=10)
        self.usdamt.pack()

        self.button = tk.Button(self.root, text="Convert!", command=self.convert_func)
        self.button.pack(pady=10)

    def convert_func(self):
        if self.usdtoeur.get() == 1:
            print("?? Converting USD to EUR ??")

        elif self.usdtogbp.get() == 1:
            print("?? Converting USD to GBP ??")

        elif self.usdtocad.get() == 1:
            print("?? Converting USD to CAD ??")

        elif self.usdtojpy.get() == 1:
            print("?? Converting USD to JPY ??")

        else:
            print("Please select a currency to convert from.")
            
App(tk.Tk())


print("Hello")
tk.mainloop()