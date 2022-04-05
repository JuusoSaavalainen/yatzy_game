from data.database_connection import get_database_connection
from repot import yatzyrepo
from tkinter import ttk, constants, Tk, StringVar

class Register:
    def __init__(self,root,handle_back,):
        self._root = root
        self._handle_back = handle_back
        self._frame = None
        self._username = None
        self._password = None
        self._initialize()
        
    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _register_user(self):
        username = self._username.get()
        password = self._password.get()
        user_repository = yatzyrepo.Loginrepo(get_database_connection())
        a = user_repository.create_acc(username,password)

    def _initialize(self):

        self._frame = ttk.Frame(master=self._root)
        main_label = ttk.Label(master=self._frame, text="Register,")
        main2_label = ttk.Label(master=self._frame, text="Username will appear in HG")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username = ttk.Entry(master=self._frame)

        password_label = ttk.Label(master=self._frame, text="Password")
        self._password = ttk.Entry(master=self._frame,show='*')

        register_button = ttk.Button(master=self._frame,text="Register",command=self._register_user)
        back_button = ttk.Button(master=self._frame,text="Back",command=self._handle_back)
        



        main_label.grid(row=0, column=0)
        main2_label.grid(row=0, column=1)
        username_label.grid(row=1, column=0)
        self._username.grid(row=1, column=1)
        password_label.grid(row=2, column=0)
        self._password.grid(row=2, column=1)
        register_button.grid(row=3, column=1)
        back_button.grid(row=3, column=0)
