import tkinter as tk
import tkinter.messagebox as msgbox
import clipboard

class IntegerToRomanConverter:
    def __init__(self, master):

        self.master = master
        self.master.title("Integer to Roman Numeral Converter")

        self.author_label = tk.Label(self.master, text="created by Arshia ( ͡° ͜ʖ ͡°)", font=('Helvetica', 10))
        self.author_label.pack(side="top", anchor="ne", pady=2, padx=5)


        self.title_label = tk.Label(self.master, text="Integer to Roman numeral converter", font=('Helvetica', 18, 'bold'))
        self.title_label.pack(side="top", pady=10, padx=10)



        self.label = tk.Label(self.master, text="Enter an integer between 1 and 3999:")
        self.label.pack()

        self.entry = tk.Entry(self.master, width=10)
        self.entry.pack()

        self.convert_button = tk.Button(self.master, text="Convert to Roman", command=self.convert_to_roman)
        self.convert_button.pack()

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack()

        self.label_roman = tk.Label(self.master, text="Enter a Roman numeral:")
        self.label_roman.pack()

        self.entry_roman = tk.Entry(self.master, width=10)
        self.entry_roman.pack()

        self.convert_roman_button = tk.Button(self.master, text="Convert to Integer", command=self.convert_to_int)
        self.convert_roman_button.pack()

        self.result_label_roman = tk.Label(self.master, text="")
        self.result_label_roman.pack()

        self.copy_button = tk.Button(self.master, text="Copy Result", command=self.copy_result)
        self.copy_button.pack()

    def convert_to_roman(self):
        num = int(self.entry.get())
        roman_numeral = self.int_to_roman(num)
        self.result_label.config(text=roman_numeral)

    def convert_to_int(self):
        roman_numeral = self.entry_roman.get()
        num = self.roman_to_int(roman_numeral)
        self.result_label_roman.config(text=num)


    def convert(self):
        num = self.entry.get()
        if not num.isnumeric() or int(num) < 1 or int(num) > 3999:
            msgbox.showerror("Error", "Please enter a valid integer between 1 and 3999.")
            return
        roman_numeral = self.int_to_roman(int(num))
        self.result_label.config(text=roman_numeral)


    def int_to_roman(self, num):
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result = ''
        i = 0
        while num > 0:
            if num - values[i] >= 0:
                result += symbols[i]
                num -= values[i]
            else:
                i += 1
        return result
    
    def roman_to_int(self, s):
        roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        for c in s:
            curr_value = roman_map[c]
            if curr_value > prev_value:
                result += curr_value - 2 * prev_value
            else:
                result += curr_value
            prev_value = curr_value
        return result
    
    def copy_result(self):
        result = self.result_label.cget("text")
        if result:
            clipboard.copy(result)
    

    

root = tk.Tk()
app = IntegerToRomanConverter(root)
root.mainloop()
