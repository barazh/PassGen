from tkinter import *
from random import *


def generate_password():
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_'
    print("".join(sample(chars, 6)))
    # return "".join(sample(chars, length))


window = Tk()
window["bg"] = '#fafafa'  # Цвет окна
window.title("Генератор паролей")  # Загаловок окна
window.wm_attributes("-alpha", 1)
window.geometry("300x250")  # Устанавливаем размер окна
window.resizable(width=False, height=False)  # Позволяет пользователю изменять размер окна

btn = Button(window, text='Сгенерировать пароль', command=generate_password)
btn.grid(column=0, row=5)



window.mainloop()  # Вызывает окно прогрмы пока мы его не закроем
