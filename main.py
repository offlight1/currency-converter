import tkinter as tk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("300x500")
        self.create_widgets()

    def create_widgets(self):
        self.header = tk.Label(self.root, text="💲 Currency Converter 🤑", font=("Arial", 24))
        self.header.pack(pady=20)

        self.select = tk.Label(self.root, text="Select currency to convert from:", font=("Arial", 16))
        self.select.pack()

        self.currencies = {
            "💵USD to EUR💶": tk.IntVar(),
            "💵USD to GBP💷": tk.IntVar(),
            "💵USD to CAD💰": tk.IntVar(),
            "💵USD to JPY💴": tk.IntVar()
        }

        for text, var in self.currencies.items():
            tk.Checkbutton(self.root, text=text, variable=var).pack(pady=10)

        self.usdamtlabel = tk.Label(self.root, text="💵 How many USD will you convert? 💵", font=("Arial", 16))
        self.usdamtlabel.pack(pady=10)

        self.usdamt = tk.Entry(self.root, width=10)
        self.usdamt.pack()

        self.button = tk.Button(self.root, text="Convert!", command=self.convert_func)
        self.button.pack(pady=10)

        self.amtlabel = tk.Label(self.root, text="Amount:", font=("Arial", 16))
        self.amtlabel.pack()

    def convert_func(self):
        selected_currencies = [text for text, var in self.currencies.items() if var.get() == 1]
        if selected_currencies:
            for currency in selected_currencies:
                print(f"Converting {currency}")
        else:
            print("Please select a currency to convert from.")

App(tk.Tk())


print("Hello")
tk.mainloop()