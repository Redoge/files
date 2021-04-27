from tkinter import *
import requests

root = Tk()


def to_money():
	try:

		count = loginInput.get()
		url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
		result = requests.get(url)
		result = result.json()
		if var.get() == 0:
			usd = result[0]
		elif var.get() == 1:
			usd = result[1] 
		sale = usd['sale']
		res_out_sum = str(float(sale) * float(count))
		res_out.config(text = f'{res_out_sum} UAH\n')

	except:
		res_out.config(text = 'ERROR\n')	


def to_uah():
	try:
		count = loginInput.get()
		url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
		result = requests.get(url)
		result = result.json()
		if var.get() == 0:
			usd = result[0]
		elif var.get() == 1:
			usd = result[1] 
		sale = usd['sale']
		res_out_sum = float( float(count) / float(sale))
		res_out_sum = str("%.2f" % res_out_sum)
		res_out.config(text = f'{res_out_sum} UAH\n')

	except:
		res_out.config(text = 'ERROR\n')	

def exange():
	if toinfobutton['text'] == '->':
		toinfobutton['text'] = '<-'
		btn['command'] = to_uah
	elif toinfobutton['text'] == '<-':
		toinfobutton['text'] = '->'
		btn['command'] = to_money


def infmoney():
	if var.get() == 0:
		text_money['text'] = 'USD'
		mtouah['text'] = 'USD -> UAH\n'
	elif var.get() == 1:
		text_money['text'] = 'EUR'
		mtouah['text'] = 'EUR -> UAH\n'



root['bg'] = '#222'
root.title('Курс валют')
root.wm_attributes('-alpha', 0.98)
root.geometry('400x400')


root.resizable(width=False, height=False)

frameb = Frame(root, bg='#995')
frameb.place(relx=0.13, rely=0.13, relwidth=0.74, relheight=0.74)

footr = Frame(root, bg='#116')
footr.place(relx=0.1, rely=0.1, relwidth=0.1, relheight=0.1)

foobr = Frame(root, bg='#116')
foobr.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.1)

footl = Frame(root, bg='#116')
footl.place(relx=0.8, rely=0.1, relwidth=0.1, relheight=0.1)

foobl = Frame(root, bg='#116')
foobl.place(relx=0.8, rely=0.8, relwidth=0.1, relheight=0.1)

frame = Frame(root, bg='silver')
frame.place(relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)



title = Label(frame, text='', bg='silver', font=40)
title.pack()

title = Label(frame, text='Конвертер валют', bg='silver', font=40, foreground="#222")
title.pack()


mtouah = Label(frame, text='USD -> UAH\n', bg='silver', font=40, foreground="#222")
mtouah.pack()


loginInput = Entry(frame, bg='white')
loginInput.pack()

text_money = Label(frame, text='USD',bg='silver', fg='#222', font="15")
text_money.place(x=210, y=105)

res_out = Label(frame, text='UAH\n', bg='silver', font=40, foreground="#222")
res_out.pack()

btn = Button(frame, text='Перевести', bg='#999', command=to_money, font = '15', fg='#ddd')
btn.pack()


footer = Label(frame, text='\n\nКурс ПРИВАТ БАНК, купівля', bg='silver',  foreground="#222")
footer.pack()

var = IntVar()
var.set(0)

usd = Radiobutton(frame, text="USD", variable=var, value=0, bg='silver', command=infmoney)
usd.place(relx=0.05, rely=0.35)

eur = Radiobutton(frame, text="EUR", variable=var, value=1, bg='silver', command=infmoney)
eur.place(relx=0.05, rely=0.45)

toinfobutton =  Button(frame, text='->', bg='silver', command=exange, font = '15', fg='black')
toinfobutton.place(relx=0.455, rely=0.235, relwidth=0.1, relheight=0.05)


root.mainloop()


