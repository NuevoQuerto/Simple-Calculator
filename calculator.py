# Simple Calculator
# Agung Rizal Suryo Laksono
# NuevoQuerto@gmail.com
# 10-03-2019

import tkinter

class Calculator(object):
	def __init__(self):
		self.root_window = tkinter.Tk()
		self.root_window.title("Calculator")
		self.input_operator = None
		self.active_operator = False
		
		# Frame Output
		self.f_output = tkinter.Frame(self.root_window)
		self.show_output = tkinter.Entry(self.f_output)
		self.show_output.grid(row=0, column=0, pady=10)
		self.show_output.insert(0, "0")
		self.f_output.pack()
		
		# Frame Input
		self.f_input = tkinter.Frame(self.root_window)
		# Tombol Angka
		tkinter.Button(self.f_input, text=0, command=lambda: self.angka(0), width=6).grid(row=1, column=0, sticky="w")
		tkinter.Button(self.f_input, text=1, command=lambda: self.angka(1), width=6).grid(row=1, column=1, sticky="w")
		tkinter.Button(self.f_input, text=2, command=lambda: self.angka(2), width=6).grid(row=1, column=2, sticky="w")
		tkinter.Button(self.f_input, text=3, command=lambda: self.angka(3), width=6).grid(row=2, column=0, sticky="w")
		tkinter.Button(self.f_input, text=4, command=lambda: self.angka(4), width=6).grid(row=2, column=1, sticky="w")
		tkinter.Button(self.f_input, text=5, command=lambda: self.angka(5), width=6).grid(row=2, column=2, sticky="w")
		tkinter.Button(self.f_input, text=6, command=lambda: self.angka(6), width=6).grid(row=3, column=0, sticky="w")
		tkinter.Button(self.f_input, text=7, command=lambda: self.angka(7), width=6).grid(row=3, column=1, sticky="w")
		tkinter.Button(self.f_input, text=8, command=lambda: self.angka(8), width=6).grid(row=3, column=2, sticky="w")
		tkinter.Button(self.f_input, text=9, command=lambda: self.angka(9), width=6).grid(row=4, column=0, sticky="w")
		# Tombol Operator
		tkinter.Button(self.f_input, text="+", command=lambda: self.operator("+"), width=6).grid(row=1, column=3, sticky="w")
		tkinter.Button(self.f_input, text="-", command=lambda: self.operator("-"), width=6).grid(row=2, column=3, sticky="w")
		tkinter.Button(self.f_input, text="x", command=lambda: self.operator("x"), width=6).grid(row=3, column=3, sticky="w")
		tkinter.Button(self.f_input, text="/", command=lambda: self.operator("/"), width=6).grid(row=4, column=3, sticky="w")
		# Tombol Hasil
		tkinter.Button(self.f_input, text="=", command=self.hasil, width=6).grid(row=5, column=3, sticky="w")
		self.f_input.pack()
		
	# Fungsi untuk mendapatkan inputan angka
	def angka(self, i):
		if self.show_output.get() == "0":
			self.show_output.delete(0, len(self.show_output.get()))
		self.show_output.insert(len(self.show_output.get()), i)
		
	# Fungsi untuk mendapatkan inputan operator
	def operator(self, operator):
		if self.show_output.get().find(operator) == -1 and self.active_operator == False:
			self.show_output.insert(len(self.show_output.get()), operator)
			self.input_operator = operator
			self.active_operator = True
	
	# Fungsi untuk mengeluarkan output
	def hasil(self):
		self.active_operator = False
		operand = self.show_output.get().split(self.input_operator)
		def ret_hasil(operator):
			return {
				"+" : int(operand[0]) + int(operand[1]),
				"-" : int(operand[0]) - int(operand[1]),
				"x" : int(operand[0]) * int(operand[1]),
				"/" : int(operand[0]) / int(operand[1]),
			}[operator]
		self.show_output.delete(0, len(self.show_output.get()))
		self.show_output.insert(0, str(ret_hasil(self.input_operator)))
		
kalkulator = Calculator()
kalkulator.root_window.mainloop()
