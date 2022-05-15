from tkinter import ttk, constants, messagebox
from src.GUI import main_gui
from src.repot.yatzyrepo import Loginrepo
from src.data.database_connection import get_database_connection

class Login:
    def __init__(self, root, handle_play):
        self._root = root
        self._handle_play = handle_play
        self._frame = None
        self._username_entry = None
        self._initialize()

    def pack(self):
        self._frame.pack(fill=constants.X)

    def destroy(self):
        self._frame.destroy()

    def _initialize(self):
        self._frame = ttk.Frame(master=self._root)
        main_label = ttk.Label(master=self._frame, text="Login or Create Account")

        username_label = ttk.Label(master=self._frame, text="Username")
        self._username_entry = ttk.Entry(master=self._frame)

        passw_label = ttk.Label(master=self._frame, text="Password")
        self._passw_entry = ttk.Entry(master=self._frame, show='*')

        login_button = ttk.Button(
            master=self._frame, text="Login", command=self._handle_play1)

        register_button = ttk.Button(
            master=self._frame, text="Register", command=self._handle_play2)

        hg_button = ttk.Button(
            master=self._frame, text="Highscores", command=self._handle_hg)

        help_button = ttk.Button(
            master=self._frame, text="Help!", command=self._handle_help)

        main_label.grid(row=0, column=0)
        username_label.grid(row=1, column=0)
        self._username_entry.grid(row=1, column=1)
        passw_label.grid(row=2, column=0)
        self._passw_entry.grid(row=2, column=1)
        login_button.grid(row=3, column=1)
        register_button.grid(row=3, column=0)
        hg_button.grid(row=4, column=0)
        help_button.grid(row=4, column=1)


    def _handle_play2(self):
        name_help = self._username_entry.get()
        passw_help = self._passw_entry.get()
        if len(name_help) == 0 or len(passw_help) == 0:
            messagebox.showerror("error", "Invalid input")
            return
        if len(name_help) >= 8:
            messagebox.showerror('error', 'Max name lenght is 7!')
            return
        main_gui.GUI.handle_register(self, name_help,passw_help)


    def _handle_play1(self):
        name_help = self._username_entry.get()
        passw_help = self._passw_entry.get()
        if len(name_help) == 0:
            messagebox.showerror("error", "Insert username first")
            return
        main_gui.GUI.handle_play(self, name_help,passw_help)

    def _handle_hg(self):
        cool_list = 'NAME                 BEST_SCORE\n'
        connection = get_database_connection()
        helper_1 = Loginrepo(connection)
        a = helper_1.print_all()
        for i in a:
            if i[1] > 0:
                cool_list += (f'{i[0]:15} <-> {i[1]:>15} \n')
        messagebox.showinfo('HIGHSCORES',f'{cool_list}')

    def _handle_help(self):
        messagebox.showinfo('INFO/HELP/WTF',f'Your expected to put max 7 char lenght username \n \nPassword does not have any conditions but it needs to exists \n \nThe login system is not secured so its adviced not to use any password that is used in somekind of real system \n \nThese are some recomended passwords \n \n "." "," "a" "!"')