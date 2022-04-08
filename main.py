from tkinter import *
import requests


def get_quote():
    response = requests.get(url="https://api.kanye.rest")
    response.raise_for_status()

    data = response.json()
    quote = data["quote"]
    canvas.itemconfig(quote_text, text=quote)


window = Tk()
window.title("Kanye Says...")
window.config(pady=50, padx=50)

canvas = Canvas(width=300, height=414)
background_image = PhotoImage(file="img/background.png")
canvas.create_image(150, 207,image=background_image)
quote_text = canvas.create_text(150, 207, text="Kanye Quote Goes Here", width=250, font=("Arial", 30, "bold"), fill="white")
canvas.grid(row=0, column=0)

kayne_img = PhotoImage(file="img/kanye.png")
kayne_button = Button(image=kayne_img, highlightthickness=0, command=get_quote)
kayne_button.grid(row=1, column=0)

window.mainloop()
