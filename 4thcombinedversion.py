import tkinter as tk
from tkinter import *
from tkinter import ttk
import calendar
from datetime import date

"""This opens up a screen with entry boxes to allow for users to input their name and player number.
   Help class provides information to help user. The Team class prints and displays the players 
   information so it can be viewed. Save_names function appends information to list that is then used in Team class
   The calendar is also included in this version but does not have a back button."""


# the first class that is called from the main
# Coded by Sarah
class GamePlay(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        # calls the method and switches the frame to the start page
        self.switch_frame(StartPage)

    def switch_frame(self, frame_class):
        # Destroys current frame and replaces it with a new one
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()


# Coded by Sarah
class StartPage(tk.Frame):
    def __init__(self, partner):
        background_color = "#00cc00"
        # creates new frame that replaces the previous one to switch frames rather than opening new GUIs
        tk.Frame.__init__(self, partner, bg=background_color)

        tk.Label(self, text="Selection Page", font="Garamond 34 bold", bg=background_color, height=10,
                 pady=15, padx=15).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Menu", pady=10, padx=10, width=20,
                  command=lambda: partner.switch_frame(MenuPage)).pack()
        tk.Button(self, text="Coach", padx=10, pady=10, width=20,
                  command=lambda: partner.switch_frame(CoachPage)).pack()
        tk.Button(self, text="Player", padx=10, pady=10, width=20,
                  command=lambda: partner.switch_frame(EnterList)).pack()


# Main menu for user with options they can pick that lead them to different pages
# Coded by Bella
class MenuPage(tk.Frame):
    def __init__(self, master):
        background_color = "#00cc00"
        # creates new frame that replaces the previous one to switch frames rather than opening new GUIs
        tk.Frame.__init__(self, master, bg=background_color)

        # Screen Label
        tk.Label(self, text="Menu Screen", bg=background_color, font="Garamond 20 bold").pack(side="top", fill="x", pady=10)

        # Buttons for menu list
        tk.Button(self, text="Return to start page", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(StartPage)).pack()
        tk.Button(self, text="Player Information", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(EnterList)).pack()
        tk.Button(self, text="Positions", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(PreSetNames)).pack()
        tk.Button(self, text="Calendar", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(CalendarPage)).pack()
        tk.Button(self, text="Music", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(FuturePage)).pack()
        tk.Button(self, text="Help!", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(Help)).pack()


# For our next steps, provides users with information on what we have planned without breaking the code
# Coded by Bella
class FuturePage(tk.Frame):
    def __init__(self, master):
        background_color = "#00cc00"
        tk.Frame.__init__(self, master, bg=background_color)

        # Screen Label
        tk.Label(self, text="This page is under construction", bg=background_color).pack(side="top", fill="x", pady=10)

        # Return to menu button so user can go backwards
        tk.Button(self, text="Return to menu page", pady=10, padx=10, width=20,
                  command=lambda: master.switch_frame(MenuPage)).pack()


# Coded by Sarah
class CoachPage(tk.Frame):
    def __init__(self, partner):
        background_color = "#00cc00"
        tk.Frame.__init__(self, partner, bg=background_color)
        tk.Label(self, text="Coach Screen", font="arial 20 bold", bg=background_color).pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page", padx=10, pady=10, width=20,
                  command=lambda: partner.switch_frame(StartPage)).pack()
        tk.Button(self, text="Players Positions", padx=10, pady=10, width=20,
                  command=lambda: partner.switch_frame(PreSetNames)).pack()


# Coded by Sarah
class PlayerPage(tk.Frame):
    def __init__(self, partner):
        background_color = "#00cc00"
        tk.Frame.__init__(self, partner, bg=background_color)
        tk.Label(self, text="Player Screen", font="arial 20 bold").pack(side="top", fill="x", pady=10)
        tk.Button(self, text="Return to start page", pady=10, padx=10,
                  command=lambda: partner.switch_frame(StartPage)).pack()


# Coded by Paige
class CalendarPage(tk.Frame):
    def __init__(self, partner):
        def reset():
            # using the delete method to delete the output
            calendar_field.delete(1.0, 'end')

            # setting the values of the IntVar objects to current month and year
            month_var.set(current_month)
            year_var.set(current_year)

            # using the config() method and assigning the text variable parameter to different IntVar objects
            month_box.config(textvariable=month_var)
            year_box.config(textvariable=year_var)

        def display_calendar():
            # get the month and year data from the spin boxes
            month = int(month_box.get())
            year = int(year_box.get())

            # using the month method from the calendar module to get the month info and storing in the variable
            output_calendar = calendar.month(year, month)

            # using the delete method to delete the output
            calendar_field.delete(1.0, 'end')

            # displaying the resultant calendar
            calendar_field.insert('end', output_calendar)

        # setting the header frame and its position using pack
        header_frame = Frame(bg="#00cc00")
        header_frame.pack(expand=True, fill="both")

        # setting the entry frame and its position using pack
        entry_frame = Frame(bg="#00cc00")
        entry_frame.pack(expand=True, fill="both")

        # setting the result frame and its position using pack
        result_frame = Frame(bg="#00cc00")
        result_frame.pack(expand=True, fill="both")

        # setting the button frame and its position using pack
        button_frame = Frame(bg="#00cc00")
        button_frame.pack(expand=True, fill="both")

        # creating the label to display the heading
        header_label = Label(header_frame, text="CALENDAR", font=('verdana', '25', 'bold'), bg="#00cc00", fg="black")
        header_label.pack(expand=True, fill="both")

        # creating the label to display the details for the month
        month_label = Label(entry_frame, text="Month:", font=("consolas", "10", "bold"),
                            bg="#00cc00", fg="#000000")
        month_label.place(x=120, y=0)

        # creating the label to display the details for the year
        year_label = Label(entry_frame, text="Year:", font=("consolas", "10", "bold"),
                           bg="#00cc00", fg="#000000")
        year_label.place(x=268, y=0)

        # creating the objects of the IntVar class
        month_var = IntVar(entry_frame)
        year_var = IntVar(entry_frame)

        # storing the current month and year information
        current_month = date.today().month
        current_year = date.today().year

        # setting the current month and year to the IntVar objects
        month_var.set(current_month)
        year_var.set(current_year)

        # creating the spin boxes to enter the month and position the spinbox
        month_box = Spinbox(entry_frame, from_=1, to=12, width=5, textvariable=month_var)
        month_box.place(x=180, y=0)

        # creating the spin box to enter the year and to position the spinbox
        year_box = Spinbox(entry_frame, from_=0000, to=3000, width=5, textvariable=year_var)
        year_box.place(x=320, y=0)

        # creating a textbox to display calendar
        calendar_field = Text(result_frame, width=20, height=8, font=("consolas", "14"), relief=RIDGE, borderwidth=2)
        calendar_field.pack(expand=False, fill="none")

        # creating the buttons for the application
        # DISPLAY BUTTON
        display_button = Button(button_frame, text="DISPLAY", bg="#00cc00", fg="#000000", command=display_calendar)
        display_button.place(x=150, y=0)

        # RESET BUTTON
        reset_button = Button(button_frame, text="RESET", bg="#00cc00", fg="#000000", command=reset)
        reset_button.place(x=300, y=0)

# EnterList class allows users to enter information and submit it where it is then appended to a list
# Coded by Bella


class EnterList(tk.Frame):
    def __init__(self, partner):
        tk.Frame.__init__(self, bg="#00cc00")
        # set background colour format for GUI
        background_color = "#00cc00"

        # Game Play Heading (Row 0)
        tk.Label(self,
                 text="Game Play",
                 font=("Arial", "16", "bold"),
                 bg=background_color,
                 padx=10, pady=10).pack()

        # User instructions(row 1)
        tk.Label(self,
                 text="Enter your name:",
                 font=("Arial", "14"), wrap=250,
                 justify=LEFT,
                 padx=10, pady=10, bg=background_color).pack()
        # Player name entry box
        self.entry = Entry(self, width=20,
                           font="Arial 14 bold")
        self.entry.pack()

        # Label for user to see when they have successfully submitted information (row 4)
        self.submitted_label = tk.Label(self,
                                        font="Arial 14 bold",
                                        fg="purple", bg=background_color,
                                        pady=10, text="--")
        self.submitted_label.pack()

        # Set up enter player's number  heading, providing user with instructions
        tk.Label(self, text="Enter your Player Number:",
                 font="Arial 14", bg=background_color).pack()

        # Second entry box, for user to enter their number
        self.entry2 = tk.Entry(self, width=20,
                               font="Arial 14 bold")
        self.entry2.pack()

        # numbers that are submitted are shown to the user when submitted in the form of a label
        self.submitted_number_text = tk.Label(self, text="--",
                                              justify=LEFT, font="Arial 14 bold", width=40, bg=background_color)
        self.submitted_number_text.pack()

        # This button submits the user's information from both entry boxes and links to the 'save names' function
        self.submit_button = tk.Button(self,
                                       highlightbackground='light blue',
                                       text="Submit", font="Arial 12",
                                       padx=10, pady=10, width=10,
                                       command=lambda: self.save_names(partner))
        self.submit_button.pack()

        # Opens the team list for the user where the two lists of information are printed
        tk.Button(self, font="Arial 12",
                  text="Team List", width=10,
                  padx=10, pady=10, command=lambda: partner.switch_frame(Team)).pack()

        # Help button frame
        self.help_frame = tk.Frame(self)
        self.help_frame.pack()
        tk.Button(self, font="Arial 12",
                  text="Help", pady=10, padx=10, width=10,
                  command=lambda: partner.switch_frame(Help)).pack()

        tk.Button(self, text="Back to start", font="Arial 12", pady=10, padx=10, width=10,
                  command=lambda: partner.switch_frame(StartPage)).pack()

    # appends players names to list and changed the submitted label to reflect the users entered name
    def save_names(self, partner):
        name = self.entry.get()
        number = self.entry2.get()

        # error handling for approved numbers only
        while True:
            try:
                # changes string to an int for error handling of approved numbers
                int_number = int(number)
                if int_number <= 21 and int_number > 0 and name != "":
                    player_number_list.append(number)
                    print(player_number_list)
                    self.submitted_number_text.configure(text=number, fg="blue")
                    player_info_list.append(name)
                    print(player_info_list)
                    self.submitted_label.configure(text=name, fg="blue")
                    break

                elif name == "":
                    print("You must enter a name")
                    self.submitted_label.configure(text="You must enter a name:", fg="blue")
                    break

                else:
                    print("You must enter a approved player number")
                    self.submitted_number_text.configure(text="Enter a approved player number (1-21)", fg="blue")
                    break

            except ValueError:
                self.submitted_number_text.configure(text="You must enter a valid number", fg="blue")
                break

        self.entry.delete(0, 'end')
        self.entry2.delete(0, 'end')
        return player_number_list
        return player_info_list


# Team class prints the list of team members entered and their numbers
# Coded by Bella
class Team(tk.Frame):
    def __init__(self, partner):
        tk.Frame.__init__(self, partner, bg="#00cc00")
        background_color = "#00cc00"
        print(player_info_list)
        print(player_number_list)

        # Set up team name heading
        self.main_heading = tk.Label(self, text="PNGHS 2022 Football Team",
                                     font="Arial 19 bold", bg=background_color)
        self.main_heading.pack()

        # Team text where the list is printed
        self.team_text = tk.Label(self, text="",
                                  justify=LEFT, width=40, bg=background_color,
                                  wrap=250)
        self.team_text.pack()

        # Informational text for user
        self.team_text = tk.Label(self,
                                  text="Here are your "
                                  " player names.",
                                  wrap=250, font="arial 10 italic", justify=LEFT, bg=background_color,
                                  fg="maroon", padx=10, pady=10)
        self.team_text.pack()

        # Combines the two lists into one and prints them together matching up with each other
        print_lists = "\n".join("{} {}".format(x, y) for x, y in zip(player_info_list, player_number_list))
        print(print_lists)

        # prints the names and numbers in side by side lists
        tk.Label(self, text=print_lists,
                 bg=background_color, font="Arial 12", justify=LEFT).pack()

        # back button that allows user to go backwards in the code (functionality implication met)
        tk.Button(self, font="Arial 12 bold",
                  text="Back", width=15,
                  padx=5, pady=5, command=lambda: partner.switch_frame(EnterList)).pack()


# help class provides information for the user in case they need help
# Coded by Bella
class Help(tk.Frame):
    def __init__(self, partner):
        background = "#00cc00"
        tk.Frame.__init__(self, partner, bg=background)

        # set up the help heading (row 0)
        tk.Label(self, text="Help / Instructions",
                 font="arial 14 bold", bg=background).pack()

        # Help Text (label, row 1)
        tk.Label(self, text="Enter your player name and number.\n"
                            "Ensure that the number you enter is an approved \n"
                            "player number.",
                 justify=LEFT, width=40, bg=background).pack()

        tk.Button(self, text="Back", padx=10, pady=10,
                  command=lambda: partner.switch_frame(EnterList)).pack()


# Coded by Sarah
class PreSetNames(tk.Frame):
    def __init__(self, partner):
        background_color = "#00cc00"
        tk.Frame.__init__(self, partner)
        # tk.Button(self, text="Return to Coach page", padx=10, pady=10,
        # command=lambda: partner.switch_frame(CoachPage)).pack()

        def players():
            player_names["values"] = ["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)",
                                      "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)",
                                      "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)",
                                      "Natalia (22)", "Brooke (23)"]

        player_names = ttk.Combobox(values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)",
                                            "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)",
                                            "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)",
                                            "Natalia (22)", "Brooke (23)"],
                                    postcommand=players)

        # coach page frame
        self.coach_page_frame = tk.Frame(background=background_color, pady=10,
                                         padx=10)
        self.coach_page_frame.pack()

        # coach page heading (row 0)
        self.coach_page_label = Label(self.coach_page_frame, text="Coach Page",
                                      font="Arial 20 bold", padx=5, pady=5, bg=background_color)
        self.coach_page_label.grid(row=0)

        self.coach_label = Label(self.coach_page_frame, text="The team list on this page has been pre-set",
                                 font="Arial 12", padx=5, pady=5, bg=background_color)
        self.coach_label.grid(row=1)

        self.field_frame = tk.Frame(self.coach_page_frame, bg=background_color, highlightbackground="white",
                                    highlightthickness=5, padx=0, pady=0)
        self.field_frame.grid(row=2)

        self.draw_field1 = tk.Frame(self.field_frame, padx=10, pady=10, bg=background_color)
        self.draw_field1.grid(row=2, column=1)

        self.select_pos2 = tk.StringVar(value="-")
        self.left1_dropdown = ttk.Combobox(self.draw_field1,
                                           values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)", "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)", "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)", "Natalia (22)", "Brooke (23)"],
                                           postcommand=players, state="readonly", width=10, textvariable=self.select_pos2)
        self.left1_dropdown.grid(row=1, column=1)

        self.draw_field2 = tk.Frame(self.field_frame, padx=10, pady=10, bg=background_color,
                                    highlightbackground="black", highlightthickness=5)
        self.draw_field2.grid(row=2, column=2)

        # GOAL BOX
        self.select_pos1 = tk.StringVar(value="-")
        self.middle1_dropdown = ttk.Combobox(self.draw_field2,
                                             values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)", "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)", "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)", "Natalia (22)", "Brooke (23)"],
                                             postcommand=players, state="readonly", width=10, textvariable=self.select_pos1)
        self.middle1_dropdown.grid(row=1, column=1)

        self.draw_field3 = tk.Frame(self.field_frame, padx=10, pady=10, bg=background_color)
        self.draw_field3.grid(row=2, column=3)

        self.select_pos3 = tk.StringVar(value="-")
        self.right1_dropdown = ttk.Combobox(self.draw_field3,
                                            values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)", "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)", "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)", "Natalia (22)", "Brooke (23)"],
                                            postcommand=players, state="readonly", width=10, textvariable=self.select_pos3)
        self.right1_dropdown.grid(row=1, column=1)

        # second row
        self.draw_field1 = tk.Frame(self.field_frame, padx=10, pady=10, bg=background_color,
                                    highlightbackground="#00cc00", highlightthickness=5)
        self.draw_field1.grid(row=3, column=1)

        self.select_pos4 = tk.StringVar(value="-")
        self.left2_dropdown = ttk.Combobox(self.draw_field1,
                                           values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)", "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)", "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)", "Natalia (22)", "Brooke (23)"],
                                           postcommand=players, state="readonly", width=10, textvariable=self.select_pos4)
        self.left2_dropdown.grid(row=1, column=1)

        self.draw_field2 = tk.Frame(self.field_frame, padx=10, pady=10, bg=background_color,
                                    highlightbackground="#00cc00", highlightthickness=5)
        self.draw_field2.grid(row=3, column=2)

        self.select_pos5 = tk.StringVar(value="-")
        self.middle2_dropdown = ttk.Combobox(self.draw_field2,
                                             values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)", "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)", "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)", "Natalia (22)", "Brooke (23)"],
                                             postcommand=players, state="readonly", width=10, textvariable=self.select_pos5)
        self.middle2_dropdown.grid(row=1, column=1)

        self.draw_field3 = tk.Frame(self.field_frame, padx=10, pady=10, bg=background_color, highlightbackground="#00cc00", highlightthickness=5)
        self.draw_field3.grid(row=3, column=3)

        self.select_pos6 = tk.StringVar(value="-")
        self.right2_dropdown = ttk.Combobox(self.draw_field3,
                                            values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)", "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)", "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)", "Natalia (22)", "Brooke (23)"],
                                            postcommand=players, state="readonly", width=10, textvariable=self.select_pos6)
        self.right2_dropdown.grid(row=1, column=1)

        # third row
        self.draw_field1 = tk.Frame(self.field_frame, padx=10, pady=10, bg=background_color,
                                    highlightbackground="#00cc00", highlightthickness=5)
        self.draw_field1.grid(row=4, column=1)

        self.select_pos7 = tk.StringVar(value="-")
        self.left3_dropdown = ttk.Combobox(self.draw_field1,
                                           values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)", "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)", "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)", "Natalia (22)", "Brooke (23)"],
                                           postcommand=players, state="readonly", width=10, textvariable=self.select_pos7)
        self.left3_dropdown.grid(row=1, column=1)

        self.draw_field2 = tk.Frame(self.field_frame, padx=10, pady=10, bg=background_color,
                                    highlightbackground="#00cc00", highlightthickness=5)
        self.draw_field2.grid(row=4, column=2)

        self.select_pos8 = tk.StringVar(value="-")
        self.middle3_dropdown = ttk.Combobox(self.draw_field2,
                                             values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)", "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)", "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)", "Natalia (22)", "Brooke (23)"],
                                             postcommand=players, state="readonly", width=10, textvariable=self.select_pos8)
        self.middle3_dropdown.grid(row=1, column=1)

        self.draw_field3 = tk.Frame(self.field_frame, padx=10, pady=10, bg=background_color, highlightbackground="#00cc00", highlightthickness=5)
        self.draw_field3.grid(row=4, column=3)

        self.select_pos9 = tk.StringVar(value="-")
        self.right3_dropdown = ttk.Combobox(self.draw_field3,
                                            values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)", "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)", "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)", "Natalia (22)", "Brooke (23)"],
                                            postcommand=players, state="readonly", width=10, textvariable=self.select_pos9)
        self.right3_dropdown.grid(row=1, column=1)

        # fourth row
        self.draw_field1 = tk.Frame(self.field_frame, padx=10, pady=10, bg=background_color,
                                    highlightbackground="#00cc00", highlightthickness=5)
        self.draw_field1.grid(row=5, column=1)

        self.select_pos10 = tk.StringVar(value="-")
        self.left4_dropdown = ttk.Combobox(self.draw_field1,
                                           values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)", "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)", "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)", "Natalia (22)", "Brooke (23)"],
                                           postcommand=players, state="readonly", width=10, textvariable=self.select_pos10)
        self.left4_dropdown.grid(row=1, column=1)

        self.draw_field2 = tk.Frame(self.field_frame, padx=10, pady=10, bg=background_color,
                                    highlightbackground="#00cc00", highlightthickness=5)
        self.draw_field2.grid(row=5, column=2)

        self.select_pos11 = tk.StringVar(value="-")
        self.middle4_dropdown = ttk.Combobox(self.draw_field2,
                                             values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)", "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)", "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)", "Natalia (22)", "Brooke (23)"],
                                             postcommand=players, state="readonly", width=10, textvariable=self.select_pos11)
        self.middle4_dropdown.grid(row=1, column=1)

        self.draw_field3 = tk.Frame(self.field_frame, padx=10, pady=10, bg=background_color, highlightbackground="#00cc00", highlightthickness=5)
        self.draw_field3.grid(row=5, column=3)

        self.select_pos12 = tk.StringVar(value="-")
        self.right4_dropdown = ttk.Combobox(self.draw_field3,
                                            values=["Sarah (1)", "Georgie (2)", "Maire (3)", "Jordan (5)", "Chloe (6)", "Ella (7)", "Stevie (8)", "Anisha (9)", "Bella (11)", "Penny (12)", "Lucea (14)", "Anne (17)", "Ruby (18)", "Paige (19)", "Georgia (21)", "Natalia (22)", "Brooke (23)"],
                                            postcommand=players, state="readonly", width=10, textvariable=self.select_pos12)
        self.right4_dropdown.grid(row=1, column=1)

        team_pos_list = ["not used", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty", "empty"]

        self.select_team_button = Button(self.coach_page_frame, text="UPDATE", command=lambda: self.export(team_pos_list))
        self.select_team_button.grid(row=3)

        def update_positions(event):
            # could make a list for this or loop to simplify
            team_pos_list[1] = self.select_pos1.get()
            team_pos_list[2] = self.select_pos2.get()
            team_pos_list[3] = self.select_pos3.get()
            team_pos_list[4] = self.select_pos4.get()
            team_pos_list[5] = self.select_pos5.get()
            team_pos_list[6] = self.select_pos6.get()
            team_pos_list[7] = self.select_pos7.get()
            team_pos_list[8] = self.select_pos8.get()
            team_pos_list[9] = self.select_pos9.get()
            team_pos_list[10] = self.select_pos10.get()
            team_pos_list[11] = self.select_pos11.get()
            team_pos_list[12] = self.select_pos12.get()
            # teamliststring = ""
            # teamliststring = team_pos_list[1], team_pos_list[2], team_pos_list[3], team_pos_list[4], team_pos_list[5], team_pos_list[6], team_pos_list[7], team_pos_list[8],team_pos_list[1]

            # print('Updated')
            # print(f"list:{team_pos_list}")

        self.middle1_dropdown.bind('<<ComboboxSelected>>', update_positions)
        self.left1_dropdown.bind('<<ComboboxSelected>>', update_positions)
        self.right1_dropdown.bind('<<ComboboxSelected>>', update_positions)
        self.left2_dropdown.bind('<<ComboboxSelected>>', update_positions)
        self.middle2_dropdown.bind('<<ComboboxSelected>>', update_positions)
        self.right2_dropdown.bind('<<ComboboxSelected>>', update_positions)
        self.left3_dropdown.bind('<<ComboboxSelected>>', update_positions)
        self.middle3_dropdown.bind('<<ComboboxSelected>>', update_positions)
        self.right3_dropdown.bind('<<ComboboxSelected>>', update_positions)
        self.left4_dropdown.bind('<<ComboboxSelected>>', update_positions)
        self.middle4_dropdown.bind('<<ComboboxSelected>>', update_positions)
        self.right4_dropdown.bind('<<ComboboxSelected>>', update_positions)

    # if any = " " then error = team is not completed
    def export(self, team_pos_list):
        contmessage = "The positions are listed below"

        for item in team_pos_list:
            if item == "-":
                contmessage = "Your team is not complete!"
                print("NO")
            else:
                print("YES")

        Export(self, contmessage, team_pos_list)


# Coded by Sarah
class Export:
    def __init__(self, partner, contmessage, team_pos_list):
        background = "orange"
        # disable export button
        # partner.select_team_button.config(state=DISABLED)

        # set up child window (i.e. export box)
        self.export_box = Toplevel()

        # set up GUI frame
        self.export_frame = Frame(self.export_box, width=300, bg=background)
        self.export_frame.grid()

        # set up export heading (row 0)
        self.how_heading = Label(self.export_frame, text="Team Selected",
                                 font="Garamond 14 bold", bg=background)
        self.how_heading.grid(row=0)

        n = 0
        for itemlist in team_pos_list:
            teamtext = f'Position {n}: {team_pos_list[n]}'
            print(teamtext)
            # names text (label, row 1)
            self.teamplay_text = Label(self.export_frame, text=teamtext,
                                       justify=LEFT, bg="#00cc00",
                                       fg="white",
                                       font="arial 10 italic", width=25)
            self.teamplay_text.grid(rowspan=13)
            n += 1

        # export text (label, row 1)
        self.export_text = Label(self.export_frame, text=contmessage,
                                 justify=LEFT, bg="white",
                                 fg="red", wrap=225, padx=10, pady=10,
                                 font="arial 10 italic", width=50)
        self.export_text.grid(row=1)


if __name__ == "__main__":
    gameplay = GamePlay()
    player_info_list = []
    player_number_list = []
    background_color = "#00cc00"
    gameplay.geometry("500x900")
    gameplay.config(background="#00cc00")
    gameplay.title("GamePlay")
    gameplay.mainloop()
