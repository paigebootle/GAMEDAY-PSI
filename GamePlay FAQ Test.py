import tkinter as tk
from tkinter import ttk


class ToggledFrame(tk.Frame):

    def __init__(self, parent, text="", *args, **options):
        tk.Frame.__init__(self, parent, *args, **options)

        self.show = tk.IntVar()
        self.show.set(0)

        self.title_frame = ttk.Frame(self)
        self.title_frame.pack(fill="x", expand=1)

        ttk.Label(self.title_frame, text=text).pack(side="left", fill="x", expand=1)

        self.toggle_button = ttk.Checkbutton(self.title_frame, width=2, text='+', command=self.toggle,
                                            variable=self.show, style='Toolbutton')
        self.toggle_button.pack(side="left")

        self.sub_frame = tk.Frame(self, relief="sunken", borderwidth=1)

    def toggle(self):
        if bool(self.show.get()):
            self.sub_frame.pack(fill="x", expand=1)
            self.toggle_button.configure(text='-')
        else:
            self.sub_frame.forget()
            self.toggle_button.configure(text='+')


if __name__ == "__main__":
    root = tk.Tk()

    t = ToggledFrame(root, text='What can parents view?', relief="raised", borderwidth=1)
    t.pack(fill="x", expand=2, pady=2, padx=2, anchor="n")
    ttk.Label(t.sub_frame, text='Parents are able to view the group chat \n'
                                ' and player profiles as well as the game calendar.').pack(side="left", fill="x", expand=1)
    ttk.Entry(t.sub_frame).pack(side="left")

    t2 = ToggledFrame(root, text='How do I find my player position?', relief="raised", borderwidth=1)
    ttk.Label(t2.sub_frame, text='They player position is set by the coach before each game. \n'
                                 ' This will be sent by the goach as a file to the group chat to be viewed \n'
                                 'by players and parents.').pack(side="left", fill="x", expand=1)
    t2.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    t3 = ToggledFrame(root, text='What does Game Play do?', relief="raised", borderwidth=1)
    ttk.Label(t3.sub_frame, text='The gameplay app is designed to encourage better communication \n'
                                 ' and team bonding within sports teams. \n'
                                 'We want to encourage easy communication and collaboration for sports teams.').pack(side="left", fill="x", expand=1)
    t3.pack(fill="x", expand=1, pady=2, padx=2, anchor="n")

    root.mainloop()
