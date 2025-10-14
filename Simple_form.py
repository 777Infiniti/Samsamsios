import tkinter as tk
from tkinter import messagebox

def submit_form():
    # Получаем данные из полей
    name = entry_name.get()
    phone = entry_phone.get()
    hobby = entry_hobby.get()
    
    # Проверяем, заполнены ли поля
    if name and phone and hobby:
        messagebox.showinfo("Успех", f"Данные сохранены:\nФИО: {name}\nТелефон: {phone}\nХобби: {hobby}")
    else:
        messagebox.showwarning("Ошибка", "Заполните все поля!")

# Создаем главное окно
root = tk.Tk()
root.title("Форма")
root.geometry("300x250")

# Создаем и размещаем метки и поля ввода
tk.Label(root, text="ФИО:").pack(pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="Телефон:").pack(pady=5)
entry_phone = tk.Entry(root, width=30)
entry_phone.pack()

tk.Label(root, text="Хобби:").pack(pady=5)
entry_hobby = tk.Entry(root, width=30)
entry_hobby.pack()

# Кнопка отправки
tk.Button(root, text="Отправить", command=submit_form).pack(pady=20)

# Запускаем приложение
root.mainloop()