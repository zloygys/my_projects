from tkinter import*


window = Tk()
window.geometry("300x300")
window.title("Шифрование")

frame1 = LabelFrame(text="Символы")
frame1.pack(padx=5, pady=5, expand=True)
lowercase = BooleanVar()
numbers = BooleanVar()
uppercase = BooleanVar()
symbols = BooleanVar()
check_lowercase = Checkbutton(frame1, text="abcdefghijklmnopqrstuvwxyz", variable=lowercase, offvalue=False, onvalue=True)
check_lowercase.pack(padx=5, pady=5, anchor = W)
check_numbers = Checkbutton(frame1, text="0123456789", variable=numbers, offvalue=False, onvalue=True)
check_numbers.pack(padx=5, pady=5, anchor = W)
check_uppercase = Checkbutton(frame1, text="ABCDEFGHIJKLMNOPQRSTUVWXYZ", variable=uppercase, offvalue=False, onvalue=True)
check_uppercase.pack(padx=5, pady=5, anchor = W)
check_symbols = Checkbutton(frame1, text="!@#$%^&*()", variable=symbols, offvalue=False, onvalue=True)
check_symbols.pack(padx=5, pady=5, anchor = W)
passwordbox = Entry(frame1, width=20)
passwordbox.pack(padx=5, pady=5)
button = Button(frame1, text = "Сгенерировать пароль")
button.pack(padx = 5, pady=5)



