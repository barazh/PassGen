from tkinter import *
from tkinter import scrolledtext
from random import *


def generate_password():  # Функция генерирует пароль и выводит его в окно вывода при нажатии на кнопку
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_'
    txt.delete(1.0, END)  # Очищаем окно текста
    txt.insert(INSERT, "".join(sample(chars, 8)))  # Вставляем в окно снгенерируемый пароль
    # print("".join(sample(chars, 8)))
    # return "".join(sample(chars, length))


root = Tk()  # Основное создание окна IU
root.title("Генератор паролей")  # Загаловок окна
root["bg"] = '#fafafa'  # Цвет окна
root.wm_attributes("-alpha", 1)  # Настройка прозрачности
root.geometry("300x400")  # Устанавливаем размер окна
root.resizable(width=True, height=True)  # Позволяет пользователю изменять размер окна

btn = Button(root, text='Сгенерировать пароль', command=generate_password)  # создаем кнопку
btn.grid(column=0, row=5)

txt = scrolledtext.ScrolledText(root, width=30, height=6)
txt.grid(column=0, row=0)

root.mainloop()  # Вызывает окно прогрмы пока мы его не закроем
