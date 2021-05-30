from tkinter import *
from random import *
from tkinter import scrolledtext


def generate_password():
    chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&*+-=?@^_'
    txt.delete(1.0, END)  # Очищаем окно текста
    txt.insert(INSERT, "".join(sample(chars, 8)))  # Вставляем в окно снгенерируемый пароль
    #print("".join(sample(chars, 8)))
    # return "".join(sample(chars, length))


window = Tk()  # Основное создание окна IU
window["bg"] = '#fafafa'  # Цвет окна
window.title("Генератор паролей")  # Загаловок окна
window.wm_attributes("-alpha", 1)  # Настройка прозрачности
window.geometry("300x400")  # Устанавливаем размер окна
window.resizable(width=True, height=True)  # Позволяет пользователю изменять размер окна

btn = Button(window, text='Сгенерировать пароль', command=generate_password)  # создаем кнопку
btn.grid(column=0, row=5)

txt = scrolledtext.ScrolledText(window, width=30, height=6)
txt.grid(column=0, row=0)



window.mainloop()  # Вызывает окно прогрмы пока мы его не закроем
