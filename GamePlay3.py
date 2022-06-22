import tkinter as tk
from tkinter import *


class GamePlay(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        """Destroys current frame and replaces it with a new one."""
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


class StartPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Selection Page").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Menu", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(MenuPage)).pack()


class MenuPage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Screen Label
        tk.Label(self, text="Menu Screen").pack(side="top", fill="x", pady=10)

        # Buttons for menu list
        tk.Button(self, text="Return to start page", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="My Profile", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(FuturePage)).pack()
        tk.Button(self, text="Team Group Chat", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(FuturePage)).pack()
        tk.Button(self, text="Positions", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(FuturePage)).pack()
        tk.Button(self, text="Music", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(FuturePage)).pack()
        tk.Button(self, text="Team Members", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(FuturePage)).pack()
        tk.Button(self, text="Individual Messages", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(FuturePage)).pack()
        tk.Button(self, text="Help!", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(FuturePage)).pack()


class FuturePage(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)

        # Screen Label
        tk.Label(self, text="This page is under construction").pack(side="top", fill="x", pady=10)

        # Return to menu button so user can go backwards
        tk.Button(self, text="Return to menu page", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(MenuPage)).pack()


if __name__ == "__main__":
    gameplay = GamePlay()
    gameplay.geometry("414x736")
    gameplay.title("GamePlay")
    gameplay.mainloop()
