import tkinter as tk
import customtkinter as ctk


def convert():
    mile_input = int(entry.get())
    km_output = str(mile_input * 1.609)
    output_string.set("Equals "+km_output+" Km")


# window
window = ctk.CTk()
window.title('M2K ')
window.geometry('400x250')

# title
title_label = ctk.CTkLabel(master=window, text='Miles to Kilometer', font=('Calibre', 24, 'bold'),
                           text_color="light blue",
                           corner_radius=15)
title_label.pack(expand=True)

# input field
input_frame = ctk.CTkFrame(master=window)

entry = ctk.CTkEntry(master=input_frame, placeholder_text="enter in miles", width=200, border_width=1,
                     border_color="blue")
button = ctk.CTkButton(master=input_frame, text="convert", width=100, command=convert)
entry.pack(side='left', padx=10, pady=25)
button.pack(side='left', padx=10, pady=25)
input_frame.pack(expand=True)

# output label
output_string = tk.StringVar()
output_label = ctk.CTkLabel(master=window, textvariable=output_string, font=("calibre", 24))
output_label.pack(pady=15, expand=True)

# run
window.mainloop()
