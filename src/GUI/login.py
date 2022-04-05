from tkinter import Entry, ttk, constants

class Login:
    def __init__(self, root, handle_play,show_register):
        self._root = root
        self._handle_play = handle_play
        self._show_register = show_register
        self._frame = None

        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        main_label = ttk.Label(master=self._frame, text="Login or Register")

        username_label = ttk.Label(master=self._frame, text="Username")
        username_entry = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        password_entry = ttk.Entry(master=self._frame)

        login_button = ttk.Button(master=self._frame,text="Login",command=self._handle_play)
        register_button = ttk.Button(master=self._frame,text="Register",command=self._show_register)

        main_label.grid(row=0, column=1)
        username_label.grid(row=1, column=0)
        username_entry.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        password_entry.grid(row=2, column=1)
        login_button.grid(row=3, column=0)
        register_button.grid(row=3, column=1)
