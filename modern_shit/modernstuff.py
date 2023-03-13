import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.geometry("400x240")


def button_func():
    print("Button Pressed")


button = customtkinter.CTkButton(
    master=app, text="A Button", command=button_func)
button.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

app.mainloop()
