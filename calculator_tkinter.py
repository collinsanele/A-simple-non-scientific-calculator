import tkinter as tk
from decimal import Decimal

class Calculator_App():
	def __init__(self, *args):
		self.window = tk.Tk()
		self.window.title('Calculator app')
		
		self.fonts = ('times', 9,  'bold')
		
		
		self.text_display = tk.Text(height=5,
		bd=15)
		self.text_display.pack()
		
		
		self.btn_exit = tk.Button(text='Exit', bg='red', fg='black', command=self.exit)
		self.btn_exit.place(x=90, y=220, in_=self.window)
		
		self.btn_back = tk.Button(text='<----',
		bg='yellow', fg='black', command=self.back)
		self.btn_back.place(x=310, y=220, in_=self.window)
		
		self.btn_clear = tk.Button(text='Clear',
		bg='yellow', fg='black', command=self.clear)
		self.btn_clear.place(x=510, y=220, in_=self.window)
		
		self.btn_1 = tk.Button(text='1',
		bg='gray', fg='black', width=8, height=2, command=self.btn1, font=self.fonts)
		self.btn_1.place(x=22, y=320, in_=self.window)
		
		
		self.btn_2 = tk.Button(text='2',
		bg='gray', fg='black', width=8, height=2, command=self.btn2, font=self.fonts)
		self.btn_2.place(x=240, y=320, in_=self.window)
		
		
		self.btn_3 = tk.Button(text='3',
		bg='gray', fg='black', width=8, height=2, command=self.btn3, font=self.fonts)
		self.btn_3.place(x=466, y=320, in_=self.window)
		
		
		self.btn_4 = tk.Button(text='4',
		bg='gray', fg='black', width=8, height=2, command=self.btn4, font=self.fonts)
		self.btn_4.place(x=22, y=420, in_=self.window)
		
		
		
		self.btn_5 = tk.Button(text='5',
		bg='gray', fg='black', width=8, height=2, command=self.btn5, font=self.fonts)
		self.btn_5.place(x=240, y=420, in_=self.window)
		
		
		
		self.btn_6 = tk.Button(text='6',
		bg='gray', fg='black', width=8, height=2, command=self.btn6, font=self.fonts)
		self.btn_6.place(x=466, y=420, in_=self.window)
		
		
		
		self.btn_7 = tk.Button(text='7',
		bg='gray', fg='black', width=8, height=2, command= self.btn7, font=self.fonts)
		self.btn_7.place(x=22, y=520, in_=self.window)
		
		
		
		self.btn_8 = tk.Button(text='8',
		bg='gray', fg='black', width=8, height=2, command=self.btn8, font=self.fonts)
		self.btn_8.place(x=240, y=520, in_=self.window)
		
		
		
		self.btn_9 = tk.Button(text='9',
		bg='gray', fg='black', width=8, height=2, command=self.btn9, font=self.fonts)
		self.btn_9.place(x=466, y=520, in_=self.window)
		
		
		
		self.btn_0 = tk.Button(text='0',
		bg='gray', fg='black', width=8, height=2, command=self.btn0, font=self.fonts)
		self.btn_0.place(x=22, y=620, in_=self.window)
		
		
		
		self.btn_dot = tk.Button(text='.',
		bg='gray', fg='black', width=8, height=2, command=self.dot, font=self.fonts)
		self.btn_dot.place(x=240, y=620, in_=self.window)
		
		
		
		self.btn_add = tk.Button(text='+',
		bg='gray', fg='black', width=8, height=2, command=self.plus, font=self.fonts)
		self.btn_add.place(x=466, y=620, in_=self.window)
		
		
		
		self.btn_sub = tk.Button(text='-',
		bg='gray', fg='black', width=8, height=2, command=self.minus, font=self.fonts)
		self.btn_sub.place(x=22, y=720, in_=self.window)
		
		
		
		self.btn_mul = tk.Button(text='*',
		bg='gray', fg='black', width=8, height=2, command=self.times, font=self.fonts)
		self.btn_mul.place(x=240, y=720, in_=self.window)
		
		
		
		self.btn_divide = tk.Button(text='/',
		bg='gray', fg='black', width=8, height=2, command=self.divide, font=self.fonts)
		self.btn_divide.place(x=466, y=720, in_=self.window)
		
		
		
		self.btn_equal = tk.Button(text='=',
		bg='gray', fg='black', width=31, height=2, command=self.process, font= self.fonts)
		self.btn_equal.place(x=17,  y=829, in_=self.window)
		
		
		self.label_made = tk.Label(text='This calculator was made by' + '\n' + 'collinsanele@gmail.com', fg='green')
		self.label_made.place(x=116, y=975,
		in_=self.window)
		
		
		
	def btn1(self, *args):
		output = '1'
		self.text_display.insert(tk.END, output)
		
	
	def btn2(self, *args):
		output = '2'
		self.text_display.insert(tk.END, output)
		
		
	
	def btn3(self, *args):
		output = '3'
		self.text_display.insert(tk.END, output)
		
		
	
	def btn4(self, *args):
		output = '4'
		self.text_display.insert(tk.END, output)
		
		
	
	def btn5(self, *args):
		output = '5'
		self.text_display.insert(tk.END, output)
		
		
		
	def btn6(self, *args):
		output = '6'
		self.text_display.insert(tk.END, output)
		
		
	
	def btn7(self, *args):
		output = '7'
		self.text_display.insert(tk.END, output)
		
		
	
	def btn8(self, *args):
		output = '8'
		self.text_display.insert(tk.END, output)
		
		
	
	def btn9(self, *args):
		output = '9'
		self.text_display.insert(tk.END, output)
		
		
	
	def btn0(self, *args):
		output = '0'
		self.text_display.insert(tk.END, output)
		
		
	
	def dot(self, *args):
		output = '.'
		self.text_display.insert(tk.END, output)
		
		
	
	def plus(self, *args):
		output = '+'
		self.text_display.insert(tk.END, output)
		
		
	
	def minus(self, *args):
		output = '-'
		self.text_display.insert(tk.END, output)
		
		
	
	def divide(self, *args):
		output = '/'
		self.text_display.insert(tk.END, output)
		
		
	
	def times(self, *args):
		output = '*'
		self.text_display.insert(tk.END, output)
		
		
	def process(self, *args):
		try:
			result = self.text_display.get('1.0', tk.END)
			result = eval(result)
			result = str(result)
			if len(result) > 9:
				result = '{:.2E}'.format(Decimal(result))
			self.text_display.delete('1.0', tk.END)
			self.text_display.insert(tk.END, result)
		except Exception:
			self.text_display.delete('1.0', tk.END)
			error = 'Error verify input'
			self.text_display.insert(tk.END, error)
			
			
	def back(self, *args):
		try:
			output = self.text_display.get('1.0', tk.END)
			output = list(output)
			output.pop()
			output.pop()
			output = ''.join(output)
			self.text_display.delete('1.0', tk.END)
			self.text_display.insert(tk.END, output)
			
		except Exception as e:
			self.text_display.delete('1.0', tk.END)
			self.text_display.insert(tk.END, str(e))
			
			
	
	def clear(self, *args):
		self.text_display.delete('1.0', tk.END)
		
		
	def exit(self, *args):
		self.window.destroy()
		
		
		
		
				

myapp = Calculator_App()
myapp.window.mainloop()









