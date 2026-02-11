from tkinter import *
import random

window = Tk()
window.geometry("800x400")
window.title("КАМЕНЬ НОЖНИЦЫ БУМАГА")
window.configure(bg="#f0f0f0")

frame = Frame(window, bg="#f0f0f0")
frame.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.98)

# Заголовок
name = Label(frame, text="КАМЕНЬ НОЖНИЦЫ БУМАГА", font=("Arial", 24, "bold"), bg="#f0f0f0")
name.pack(pady=20)

# Метки имен
Label(frame, text="Игрок", font="Arial 15 bold", bg="#f0f0f0").place(x=130, y=70)
Label(frame, text="Компьютер", font="Arial 15 bold", bg="#f0f0f0").place(x=550, y=70)

# Вместо картинок используем большие Label для эмодзи
user_emoji = Label(frame, text="❓", font=("Arial", 80), bg="#f0f0f0")
user_emoji.place(x=100, y=110)

comp_emoji = Label(frame, text="❓", font=("Arial", 80), bg="#f0f0f0")
comp_emoji.place(x=550, y=110)

# Поле результата
label_res = Label(frame, text="Выберите предмет!", font=("Arial", 18), width=25, 
                  borderwidth=2, relief="flat", bg="#ffffff")
label_res.place(x=225, y=250)

# Словарь для сопоставления названий и эмодзи
emoji_map = {
    "Rock": "✊",
    "Paper": "✋",
    "Scissors": "✌️"
}

def play(user_choice):
    options = ["Rock", "Paper", "Scissors"]
    comp_choice = random.choice(options)

    # Обновляем эмодзи на экране
    user_emoji.config(text=emoji_map[user_choice])
    comp_emoji.config(text=emoji_map[comp_choice])

    # Логика определения победителя
    if user_choice == comp_choice:
        result = "Ничья! 🤝"
        color = "gray"
    elif (user_choice == "Rock" and comp_choice == "Scissors") or \
         (user_choice == "Paper" and comp_choice == "Rock") or \
         (user_choice == "Scissors" and comp_choice == "Paper"):
        result = "Ты выиграл! 🎉"
        color = "green"
    else:
        result = "Компьютер выиграл! 🤖"
        color = "red"
    
    label_res.config(text=result, fg=color)

# Кнопки управления
btn_style = {"font": ("Arial", 12, "bold"), "width": 12, "height": 2, "cursor": "hand2"}

b1 = Button(frame, text="Камень ✊", **btn_style, command=lambda: play("Rock"))
b1.place(x=100, y=320)

b2 = Button(frame, text="Бумага ✋", **btn_style, command=lambda: play("Paper"))
b2.place(x=325, y=320)

b3 = Button(frame, text="Ножницы ✌️", **btn_style, command=lambda: play("Scissors"))
b3.place(x=550, y=320)

window.mainloop()
