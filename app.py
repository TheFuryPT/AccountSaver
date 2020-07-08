import tkinter as tk

root = tk.Tk()

HEIGHT = 120
WIDTH = 320

txt_file = ""

login_name = "1"
login_pass = "1"


def toggle_password():
    if button_pass.var.get():
        password_entry['show'] = "*"
    else:
        password_entry['show'] = ""


def login_verify():
    if username_entry.get() == login_name and password_entry.get() == login_pass:
        print("Fury is in the file")
        root.iconify()
        screen_1()


canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg="#D5D0D0")
frame.place(relwidth=1, relheight=1)

# Root Labels

username_label = tk.Label(frame, text="UserName:", bg="#D5D0D0", fg="gray")
username_label.place(relx=-0.39, rely=0.15, relwidth=1, relheight=0.1)

pass_label = tk.Label(frame, text="Password:", bg="#D5D0D0", fg="gray")
pass_label.place(relx=-0.4, rely=0.5, relwidth=1, relheight=0.1)

# Root Entry

username_entry = tk.Entry(frame)
username_entry.place(relx=0.25, rely=0.11, relwidth=0.55, relheight=0.2)

password_entry = tk.Entry(frame)
password_entry.place(relx=0.25, rely=0.47, relwidth=0.55, relheight=0.2)

password_entry.default_show_val = password_entry['show']
password_entry['show'] = "*"

# Root Buttons

button_login = tk.Button(frame, text="Login", bg="#908F8F", fg="#464545", command=login_verify)
button_login.place(relx=0, rely=0.75, relwidth=1, relheight=0.25)

button_pass = tk.Checkbutton(frame, text="Hide", bg="#D5D0D0", onvalue=True, offvalue=False, command=toggle_password)
button_pass.var = tk.BooleanVar(value=True)
button_pass['variable'] = button_pass.var
button_pass.place(relx=0.83, rely=0.47, relwidth=0.15, relheight=0.2)


# screen1 stuff

def screen_1():
    # fUNCTIONS

    def lista():
        save_read = open("user_logs", "r")
        txt = save_read.read()
        txt_list = list(txt.split("?"))
        print(txt_list)
        print(len(txt_list))

        # Screen1 Label Data

        tot = 0
        for i in txt_list:
            data = tk.Label(screen1, text=i, bg="#D5D0D0", fg="gray")
            data.place(relx=0, rely=0.6 + tot, relwidth=1, relheight=0.1)
            tot -= 0.1

    def clear_user():
        clear = open("user_logs", "w")
        clear.write("")
        clear_read = open("user_logs", "r")
        print(clear_read.read())
        clear_read.close()
        clear.close()

    def save_screen1():
        save = open("user_logs", "a")
        save.write(f"?{name_entry.get()} --> {pass_entry.get()}")
        save.close()
        save_read = open("user_logs", "r")
        txt = save_read.read()
        save_read.close()
        txt_list = list(txt.split("?"))
        print(txt_list)
        print(len(txt_list))
        # Screen1 Label Data
        lista()

    # Screen1 stuff

    screen1 = tk.Toplevel(root, bg="#D5D0D0")  # generate a screen after de main ROOT
    screen1.title("Fury Stuff")  # Fury Stuff is the name of the window
    screen1.geometry(f"{WIDTH}x{HEIGHT * 2}")  # Width and height of the window

    # Screen1 Labels

    save_name = tk.Label(screen1, text="Name:", bg="#D5D0D0", fg="black")
    save_name.place(relx=-0.43, rely=0, relwidth=1, relheight=0.1)

    save_pass = tk.Label(screen1, text="Pass:", bg="#D5D0D0", fg="black")
    save_pass.place(relx=-0.44, rely=0.1, relwidth=1, relheight=0.1)

    # Root Entry

    name_entry = tk.Entry(screen1)
    name_entry.place(relx=0.25, rely=0, relwidth=0.6, relheight=0.1)

    pass_entry = tk.Entry(screen1)
    pass_entry.place(relx=0.25, rely=0.1, relwidth=0.6, relheight=0.1)

    # Screen1 Buttons

    button_quit = tk.Button(screen1, text="QUIT", bg="#908F8F", fg="#464545", command=quit)
    button_quit.place(relx=0.5, rely=0.9, relwidth=0.5, relheight=0.1)

    button_quit = tk.Button(screen1, text="CLEAR", bg="#908F8F", fg="#464545", command=clear_user)
    button_quit.place(relx=0, rely=0.9, relwidth=0.5, relheight=0.1)

    button_save = tk.Button(screen1, text="SAVE", bg="#908F8F", fg="#464545", command=save_screen1)
    button_save.place(relx=0, rely=0.8, relwidth=1, relheight=0.1)

    button_clear = tk.Button(screen1, text="SHOW", bg="#908F8F", fg="#464545", command=lista)
    button_clear.place(relx=0, rely=0.7, relwidth=1, relheight=0.1)


root.mainloop()
