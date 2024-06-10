import random
import string
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pyperclip

def generate():
    characters = string.ascii_letters + string.digits + string.punctuation

    required = [random.choice(string.ascii_uppercase),
                random.choice(string.ascii_uppercase),
                random.choice(string.ascii_lowercase),
                random.choice(string.punctuation),
                random.choice(string.punctuation),
                random.choice(string.digits),
                random.choice(string.digits)]

    randomstring = [random.choice(characters) for _ in range(5)]
    finalrand = required + randomstring
    random.shuffle(finalrand)

    placeholder = ''.join(finalrand)
    genpass.set(placeholder)
    save_button.config(state=NORMAL)
    copy_button.config(state=NORMAL)


def copy():
    pyperclip.copy(genpass.get())

def save():
    try:
        file = filedialog.asksaveasfile(defaultextension='.txt',
                                        filetypes=[("Text file", ".txt")])
        filetext = str(genpass.get())
        file.write(filetext)
        file.close()
    except AttributeError:
        genpass.set("Aborted")

window = Tk()
window.title("Password Generator")

style = ttk.Style()
style.configure('TButton', font=('Consolas', 15), padding=10)
style.configure('TLabel', font=('Consolas', 15), padding=10)

genpass = StringVar()
genpass.set("Click Generate")

password_label = ttk.Label(window, textvariable=genpass, background="lightgray")
password_label.grid(row=0, column=0, columnspan=4, pady=10, padx=10, sticky="ew")

copy_button = ttk.Button(window, text="Copy", command=copy,state=DISABLED)
copy_button.grid(row=1, column=0, padx=10, pady=10)

generate_button = ttk.Button(window, text="Generate", command=generate)
generate_button.grid(row=1, column=1, padx=10, pady=10)

exit_button = ttk.Button(window, text="Quit", command=window.quit)
exit_button.grid(row=1, column=2, padx=10, pady=10)

save_button = ttk.Button(window, text="Save", command=save, state=DISABLED)
save_button.grid(row=1, column=3, padx=10, pady=10)


window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.columnconfigure(2, weight=1)
window.columnconfigure(3, weight=1)

window.minsize(400, 150)

window.mainloop()