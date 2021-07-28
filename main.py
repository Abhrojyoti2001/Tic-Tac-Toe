from tkinter import *
from tkinter import messagebox
import random


class Game:
    D0 = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None}
    D1 = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None}
    D2 = {'Player_1': {'Name': "Player 1", 'Symbol': "X", 'Colour': "red", 'Total_win': 0}, 'Player_2': {'Name': "Player 2", 'Symbol': "O", 'Colour': "blue",  'Total_win': 0}}
    D3 = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None}
    D4 = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
    mode = None
    turn = None
    path = 0
    p_id = None
    draw = 0
    highlight_text = None
    background_colour_code = "#3498db"
    back_btn = 1

    def __init__(self):
        self.load_gui_window(self.load_1st_window)

    def load_gui_window(self, gui_type, bgc=None, top=1, btn=None):
        self.root = Tk()

        self.root.title("Tic Tac Toe")
        self.root.minsize(420, 500)
        self.root.maxsize(420, 500)

        if bgc is None:
            self.root.configure(background=self.background_colour_code)
        else:
            self.root.configure(background=bgc)
        # load gui window
        if gui_type == self.gaming_window:
            self.gaming_window(top=top)
        elif gui_type == self.symbol_change_gui:
            self.symbol_change_gui(btn=btn)
        elif gui_type == self.symbol_colour_change_gui:
            self.symbol_colour_change_gui(btn=btn)
        else:
            gui_type()
        self.root.mainloop()

    def load_new_gui(self, new_gui, top=1, btn=None):
        self.root.destroy()
        if new_gui == self.background_colour_change:
            self.back_btn = 2
            self.load_gui_window(new_gui, bgc="#fff", top=top)
        elif new_gui == self.symbol_change_gui:
            self.back_btn = 3
            self.load_gui_window(new_gui, bgc="#fff", btn=btn)
        elif new_gui == self.symbol_colour_change_gui:
            self.back_btn = 4
            self.load_gui_window(new_gui, bgc="#fff", btn=btn)
        else:
            self.load_gui_window(new_gui, top=top)

    def refresh_window(self, new_window, kyw=None):
        self.D0 = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None}
        self.D1 = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None}
        self.D3 = {'1': None, '2': None, '3': None, '4': None, '5': None, '6': None, '7': None, '8': None, '9': None}
        self.D4 = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0, '9': 0}
        self.path = 0
        self.p_id = None
        self.draw = 0
        if kyw == "SNG":
            self.D2['Player_1']['Total_win'] = 0
            self.D2['Player_2']['Total_win'] = 0
            self.load_new_gui(new_window)
        elif kyw == "RTG":
            self.gaming_mode(1)
        elif kyw == "TRUE":
            self.path = 0
            self.gaming_mode(1)
        else:
            self.mode = None
            self.turn = None
            self.back_btn = 1
            self.D2 = {'Player_1': {'Name': "Player 1", 'Symbol': "X", 'Colour': "red", 'Total_win': 0}, 'Player_2': {'Name': "Player 2", 'Symbol': "O", 'Colour': "blue", 'Total_win': 0}}
            self.load_new_gui(new_window)

    def header_menu1(self):
        menu = Menu(self.root)
        self.root.configure(menu=menu)
        file_menu = Menu(menu)
        menu.add_cascade(label="Home", menu=file_menu)
        file_menu.add_command(label="Restart This Game", command=lambda: self.refresh_window(self.gaming_window, "RTG"))
        file_menu.add_command(label="Start a New Game", command=lambda: self.refresh_window(self.gaming_window, "SNG"))
        file_menu.add_command(label="Exit and Back to First Page", command=lambda: self.refresh_window(self.load_1st_window, "EBFP"))

    def header_menu2(self):
        menu = Menu(self.root)
        self.root.configure(menu=menu)
        file_menu = Menu(menu)
        menu.add_command(label="Back", command=lambda: self.back_button_task())

    def header_menu3(self):
        menu = Menu(self.root)
        self.root.configure(menu=menu)
        file_menu = Menu(menu)
        menu.add_command(label="Back", command=lambda: self.back_button_task())
        menu.add_command(label="Change Background Colour", command=lambda: self.load_new_gui(self.background_colour_change))

    def back_button_task(self):
        if self.back_btn == 2:
            self.load_new_gui(self.gaming_window)
        elif self.back_btn == 3:
            self.D2['Player_1']['Symbol'] = "X"
            self.D2['Player_2']['Symbol'] = "O"
            self.load_new_gui(self.load_2nd_window)
        elif self.back_btn == 4:
            self.D2['Player_1']['Colour'] = "red"
            self.D2['Player_2']['Colour'] = "blue"
            self.load_new_gui(self.symbol_change_gui)
        else:
            self.refresh_window(self.background_colour_code, self.load_1st_window)

    def player_details(self):
        self.D2['Player_1']['Name'] = self.player_1.get()
        self.D2['Player_2']['Name'] = self.player_2.get()
        if self.D2['Player_1']['Symbol'] == self.D2['Player_2']['Symbol'] and self.D2['Player_1']['Colour'] == self.D2['Player_1']['Colour']:
            messagebox.showerror("Error!", "You cant use same symbol & colour")
            self.load_new_gui(self.load_2nd_window)
        else:
            data = messagebox.askquestion("Important Notice", "You cannot change name,symbol & colour in middle of game. Are you want to continue?")  # yes or no
            if data == 'yes':
                self.gaming_mode(1)
            else:
                self.load_new_gui(self.load_2nd_window)

    def gaming_mode(self, top):
        if self.mode == "Single Player":
            if self.path == 0:  # this is for first time
                if self.turn == "First Turn":
                    self.path = 11
                    self.load_new_gui(self.gaming_window, top)
                else:
                    self.path = 12
                    self.turn_of_cpu(top)
            elif self.path == 11:
                self.path = 12
                self.turn_of_cpu(top)
            elif self.path == 12:
                self.path = 11
                self.load_new_gui(self.gaming_window, top)
            else:
                b = self.path
                self.path = 12
                if top == 1:
                    top = 2
                else:
                    top = 1
                self.gaming_rule(top, b)
        else:
            self.load_new_gui(self.gaming_window, top)

    def intelligence_of_cup(self, top):
        if self.D3['1'] == self.D3['2'] and self.D3['2'] is not None and self.D3['3'] is None:
            self.path = 3
            self.gaming_mode(top)
        elif self.D3['2'] == self.D3['3'] and self.D3['3'] is not None and self.D3['1'] is None:
            self.path = 1
            self.gaming_mode(top)
        elif self.D3['1'] == self.D3['3'] and self.D3['3'] is not None and self.D3['2'] is None:
            self.path = 2
            self.gaming_mode(top)

        elif self.D3['1'] == self.D3['4'] and self.D3['4'] is not None and self.D3['7'] is None:
            self.path = 7
            self.gaming_mode(top)
        elif self.D3['4'] == self.D3['7'] and self.D3['7'] is not None and self.D3['1'] is None:
            self.path = 1
            self.gaming_mode(top)
        elif self.D3['1'] == self.D3['7'] and self.D3['7'] is not None and self.D3['4'] is None:
            self.path = 4
            self.gaming_mode(top)

        elif self.D3['1'] == self.D3['5'] and self.D3['5'] is not None and self.D3['9'] is None:
            self.path = 9
            self.gaming_mode(top)
        elif self.D3['5'] == self.D3['9'] and self.D3['9'] is not None and self.D3['1'] is None:
            self.path = 1
            self.gaming_mode(top)
        elif self.D3['1'] == self.D3['9'] and self.D3['9'] is not None and self.D3['5'] is None:
            self.path = 5
            self.gaming_mode(top)

        elif self.D3['2'] == self.D3['5'] and self.D3['5'] is not None and self.D3['8'] is None:
            self.path = 8
            self.gaming_mode(top)
        elif self.D3['5'] == self.D3['8'] and self.D3['8'] is not None and self.D3['2'] is None:
            self.path = 2
            self.gaming_mode(top)
        elif self.D3['2'] == self.D3['8'] and self.D3['8'] is not None and self.D3['5'] is None:
            self.path = 5
            self.gaming_mode(top)

        elif self.D3['3'] == self.D3['5'] and self.D3['5'] is not None and self.D3['7'] is None:
            self.path = 7
            self.gaming_mode(top)
        elif self.D3['5'] == self.D3['7'] and self.D3['7'] is not None and self.D3['3'] is None:
            self.path = 3
            self.gaming_mode(top)
        elif self.D3['3'] == self.D3['7'] and self.D3['7'] is not None and self.D3['5'] is None:
            self.path = 5
            self.gaming_mode(top)

        elif self.D3['3'] == self.D3['6'] and self.D3['6'] is not None and self.D3['9'] is None:
            self.path = 9
            self.gaming_mode(top)
        elif self.D3['6'] == self.D3['9'] and self.D3['9'] is not None and self.D3['3'] is None:
            self.path = 3
            self.gaming_mode(top)
        elif self.D3['3'] == self.D3['9'] and self.D3['9'] is not None and self.D3['6'] is None:
            self.path = 6
            self.gaming_mode(top)

        elif self.D3['4'] == self.D3['5'] and self.D3['5'] is not None and self.D3['6'] is None:
            self.path = 6
            self.gaming_mode(top)
        elif self.D3['5'] == self.D3['6'] and self.D3['6'] is not None and self.D3['4'] is None:
            self.path = 4
            self.gaming_mode(top)
        elif self.D3['4'] == self.D3['6'] and self.D3['6'] is not None and self.D3['5'] is None:
            self.path = 5
            self.gaming_mode(top)

        elif self.D3['7'] == self.D3['8'] and self.D3['8'] is not None and self.D3['9'] is None:
            self.path = 9
            self.gaming_mode(top)
        elif self.D3['8'] == self.D3['9'] and self.D3['9'] is not None and self.D3['7'] is None:
            self.path = 7
            self.gaming_mode(top)
        elif self.D3['7'] == self.D3['9'] and self.D3['9'] is not None and self.D3['8'] is None:
            self.path = 8
            self.gaming_mode(top)
        else:
            self.gaming_mode(top)

    def turn_of_cpu(self, top):
        b = random.randint(1, 9)
        if self.D1[str(b)] is not None:
            self.turn_of_cpu(top)
        if top == 1:
            top = 2
        else:
            top = 1
        self.gaming_rule(top, b)

    def gaming_rule(self, top, kyw=None):
        if top == 2:
            symbol = self.D2['Player_1']['Symbol']
            colour = self.D2['Player_1']['Colour']
            p_id = 1
        else:
            symbol = self.D2['Player_2']['Symbol']
            colour = self.D2['Player_2']['Colour']
            p_id = 2

        if kyw == 1:
            self.D0['1'] = colour
            self.D1['1'] = symbol
            self.D3['1'] = p_id
        elif kyw == 2:
            self.D0['2'] = colour
            self.D1['2'] = symbol
            self.D3['2'] = p_id
        elif kyw == 3:
            self.D0['3'] = colour
            self.D1['3'] = symbol
            self.D3['3'] = p_id
        elif kyw == 4:
            self.D0['4'] = colour
            self.D1['4'] = symbol
            self.D3['4'] = p_id
        elif kyw == 5:
            self.D0['5'] = colour
            self.D1['5'] = symbol
            self.D3['5'] = p_id
        elif kyw == 6:
            self.D0['6'] = colour
            self.D1['6'] = symbol
            self.D3['6'] = p_id
        elif kyw == 7:
            self.D0['7'] = colour
            self.D1['7'] = symbol
            self.D3['7'] = p_id
        elif kyw == 8:
            self.D0['8'] = colour
            self.D1['8'] = symbol
            self.D3['8'] = p_id
        else:
            self.D0['9'] = colour
            self.D1['9'] = symbol
            self.D3['9'] = p_id

        if self.D3['1'] == self.D3['2'] and self.D3['2'] == self.D3['3'] and self.D3['3'] is not None:
            self.wining_function(self.D3['1'])
            self.highlight_text = 1
        elif self.D3['1'] == self.D3['4'] and self.D3['4'] == self.D3['7'] and self.D3['7'] is not None:
            self.wining_function(self.D3['1'])
            self.highlight_text = 2
        elif self.D3['1'] == self.D3['5'] and self.D3['5'] == self.D3['9'] and self.D3['9'] is not None:
            self.wining_function(self.D3['1'])
            self.highlight_text = 3
        elif self.D3['2'] == self.D3['5'] and self.D3['5'] == self.D3['8'] and self.D3['8'] is not None:
            self.wining_function(self.D3['2'])
            self.highlight_text = 4
        elif self.D3['3'] == self.D3['5'] and self.D3['5'] == self.D3['7'] and self.D3['7'] is not None:
            self.wining_function(self.D3['3'])
            self.highlight_text = 5
        elif self.D3['3'] == self.D3['6'] and self.D3['6'] == self.D3['9'] and self.D3['9'] is not None:
            self.wining_function(self.D3['3'])
            self.highlight_text = 6
        elif self.D3['4'] == self.D3['5'] and self.D3['5'] == self.D3['6'] and self.D3['6'] is not None:
            self.wining_function(self.D3['4'])
            self.highlight_text = 7
        elif self.D3['7'] == self.D3['8'] and self.D3['8'] == self.D3['9'] and self.D3['9'] is not None:
            self.wining_function(self.D3['7'])
            self.highlight_text = 8
        elif self.draw == 8:
            self.wining_function(0)
        else:
            self.draw += 1
            if self.path == 11:
                self.intelligence_of_cup(top)
            else:
                self.gaming_mode(top)

    def wining_function(self, w_id):
        self.p_id = w_id
        if self.p_id == 1:
            self.D2['Player_1']['Total_win'] += 1
        elif self.p_id == 2:
            self.D2['Player_2']['Total_win'] += 1
        else:
            self.D2['Player_1']['Total_win'] += 0
            self.D2['Player_2']['Total_win'] += 0
        self.load_new_gui(self.wining_gui_window)

    def colour_code_change(self, cc=None):
        self.background_colour_code = cc
        self.load_new_gui(self.load_2nd_window)

    def load_1st_window(self):
        def show():
            m1 = mode1.get()
            m2 = mode2.get()
            if m1 == "Single Player":
                self.mode = m1
                self.load_new_gui(self.load_1st_window, self.background_colour_code)
            elif m1 == "Two Player":
                self.mode = m1
                self.load_new_gui(self.load_2nd_window, self.background_colour_code)
            elif m2 == "First Turn" or m2 == "Second Turn":
                self.turn = m2
                self.load_new_gui(self.load_2nd_window)
            else:
                messagebox.showerror("Error", "Please select the option")
        if self.mode == "Single Player":
            self.header_menu2()
        if self.background_colour_code == "#fff":
            fc = "black"
        else:
            fc = "#fff"
        self.label0 = Label(self.root, text="Tic Tac Toe", bg=self.background_colour_code, fg=fc, font=("Times", 32, "bold")).pack(pady=(20, 10))

        # Dropdown menu options
        options1 = ["Single Player", "Two Player"]
        mode1 = StringVar()
        mode1.set("Select the Mode")

        # Dropdown menu options
        options2 = ["First Turn", "Second Turn"]
        mode2 = StringVar()
        mode2.set("Select the Turn")

        # Create Dropdown menu
        self.frame1 = Frame(self.root, bg="#3498db")
        self.frame1.pack(pady=(30, 10))
        if self.mode is None:
            drop = OptionMenu(self.frame1, mode1, *options1)
            drop.configure(font=("Times", 20, "italic"))
            drop.pack()
            drop['width'] = 15
        else:
            self.label1 = Label(self.frame1, text=self.mode + " Mode", bg=self.background_colour_code, fg=fc, font=("Times", 20, "italic")).pack(side=LEFT)

        # Create Dropdown menu
        self.frame2 = Frame(self.root, bg="#3498db")
        self.frame2.pack(pady=(30, 10))
        if self.mode == "Single Player":
            drop = OptionMenu(self.frame2, mode2, *options2)
            drop.configure(font=("Times", 20, "italic"))
            drop.pack()
            drop['width'] = 15

        self.next_btn = Button(self.root, text="Next", bg="#fff", fg="#FF5357", font=("Times", 20, "bold"), command=show).pack(side=BOTTOM, pady=(10, 25))

    def load_2nd_window(self):
        self.header_menu3()

        if self.background_colour_code == "#fff":
            fc = "black"
        else:
            fc = "#fff"
        if self.background_colour_code == self.D2['Player_1']['Colour'] or self.background_colour_code == self.D2['Player_2']['Colour']:
            tc = "#fff"
        else:
            tc = self.background_colour_code
        self.label0 = Label(self.root, text="Tic Tac Toe", bg=self.background_colour_code, fg=fc, font=("Times", 32, "bold")).pack(pady=(20, 10))
        self.label1 = Label(self.root, text="First Player", bg=self.background_colour_code, fg=fc, font=("Times", 20, "italic")).pack(pady=(10, 2))

        v1 = StringVar()
        if self.turn == "Second Turn":
            v1.set("CPU")
        else:
            v1.set(self.D2['Player_1']['Name'])
        self.player_1 = Entry(self.root, textvariable=v1)
        self.player_1.pack(pady=(2, 10), ipady=7, ipadx=80)

        self.frame1 = Frame(self.root, bg="#3498db")
        self.frame1.pack()
        self.label2 = Label(self.frame1, text=self.D2['Player_1']['Symbol'], bg=tc, fg=self.D2['Player_1']['Colour'],  font=("Arial", 20)).pack(side=LEFT)
        self.sim1 = Button(self.frame1, text="Change symbol & colour", bg="#fff", fg="#FF5357", font=("Times", 14), command=lambda: self.load_new_gui(new_gui=self.symbol_change_gui, btn=1)).pack(side=LEFT)

        self.label3 = Label(self.root, text="Second Player", bg=self.background_colour_code, fg=fc, font=("Times", 20, "italic")).pack(pady=(20, 2))

        v2 = StringVar()
        if self.turn == "First Turn":
            v2.set("CPU")
        else:
            v2.set(self.D2['Player_2']['Name'])
        self.player_2 = Entry(self.root, textvariable=v2)
        self.player_2.pack(pady=(2, 10), ipady=7, ipadx=80)

        self.frame2 = Frame(self.root, bg="#3498db")
        self.frame2.pack()
        self.label4 = Label(self.frame2, text=self.D2['Player_2']['Symbol'], fg=self.D2['Player_2']['Colour'], bg=tc, font=("Arial", 20)).pack(side=LEFT)
        self.sim2 = Button(self.frame2, text="Change symbol & colour", bg="#fff", fg="#FF5357", font=("Times", 14), command=lambda: self.load_new_gui(new_gui=self.symbol_change_gui, btn=2)).pack(side=LEFT)

        self.start_btn = Button(self.root, text="Start Game", bg="#fff", fg="#FF5357", font=("Times", 20, "bold"), command=lambda: self.player_details()).pack(pady=(10, 10))

    def colour_code(self, code):
        self.code = code

    def background_colour_change(self):
        self.header_menu2()

        self.label0 = Label(self.root, text="Press the  Colour which you want", font=("Times", 20, "bold")).pack(pady=(20, 10))

        self.frame1 = Frame(self.root)
        self.frame1.pack()
        b1 = Button(self.frame1, text="\t", bg="#3498db", font=("Times", 20), command=lambda: self.colour_code("#3498db")).pack(side=LEFT)
        b2 = Button(self.frame1, text="\t", bg="red", font=("Times", 20), command=lambda: self.colour_code("red")).pack(side=LEFT)
        b3 = Button(self.frame1, text="\t", bg="blue", font=("Times", 20), command=lambda: self.colour_code("blue")).pack(side=LEFT)

        self.frame2 = Frame(self.root)
        self.frame2.pack()
        b4 = Button(self.frame2, text="\t", bg="#fff", font=("Times", 20), command=lambda: self.colour_code("#fff")).pack(side=LEFT)
        b5 = Button(self.frame2, text="\t", bg="yellow", font=("Times", 20), command=lambda: self.colour_code("yellow")).pack(side=LEFT)
        b6 = Button(self.frame2, text="\t", bg="green", font=("Times", 20), command=lambda: self.colour_code("green")).pack(side=LEFT)

        self.frame3 = Frame(self.root)
        self.frame3.pack()
        b7 = Button(self.frame3, text="\t", bg="brown", font=("Times", 20), command=lambda: self.colour_code("brown")).pack(side=LEFT)
        b8 = Button(self.frame3, text="\t", bg="#6F1E51", font=("Times", 20), command=lambda: self.colour_code("#6F1E51")).pack(side=LEFT)
        b9 = Button(self.frame3, text="\t", bg="#9980FA", font=("Times", 20), command=lambda: self.colour_code("#9980FA")).pack(side=LEFT)

        self.frame4 = Frame(self.root)
        self.frame4.pack()
        b10 = Button(self.frame4, text="\t", bg="#16a085", font=("Times", 20), command=lambda: self.colour_code("#16a085")).pack(side=LEFT)
        b11 = Button(self.frame4, text="\t", bg="#e67e22", font=("Times", 20), command=lambda: self.colour_code("#e67e22")).pack(side=LEFT)
        b12 = Button(self.frame4, text="\t", bg="#c0392b", font=("Times", 20), command=lambda: self.colour_code("#c0392b")).pack(side=LEFT)

        self.frame5 = Frame(self.root)
        self.frame5.pack()
        b13 = Button(self.frame5, text="\t", bg="#9b59b6", font=("Times", 20), command=lambda: self.colour_code("#9b59b6")).pack(side=LEFT)
        b14 = Button(self.frame5, text="\t", bg="#1B1464", font=("Times", 20), command=lambda: self.colour_code("#1B1464")).pack(side=LEFT)
        b15 = Button(self.frame5, text="\t", bg="black", font=("Times", 20), command=lambda: self.colour_code("black")).pack(side=LEFT)

        self.frame6 = Frame(self.root)
        self.frame6.pack()
        b16 = Button(self.frame6, text="\t", bg="#7f8c8d", font=("Times", 20), command=lambda: self.colour_code("#7f8c8d")).pack(side=LEFT)
        b17 = Button(self.frame6, text="\t", bg="#fdcb6e", font=("Times", 20), command=lambda: self.colour_code("#fdcb6e")).pack(side=LEFT)
        b18 = Button(self.frame6, text="\t", bg="#81ecec", font=("Times", 20), command=lambda: self.colour_code("#81ecec")).pack(side=LEFT)

        self.frame7 = Frame(self.root)
        self.frame7.pack()
        b19 = Button(self.frame7, text="\t", bg="#006266", font=("Times", 20), command=lambda: self.colour_code("#006266")).pack(side=LEFT)
        b20 = Button(self.frame7, text="\t", bg="#D980FA", font=("Times", 20), command=lambda: self.colour_code("#D980FA")).pack(side=LEFT)
        b21 = Button(self.frame7, text="\t", bg="#A3CB38", font=("Times", 20), command=lambda: self.colour_code("#A3CB38")).pack(side=LEFT)

        b22 = Button(self.root, text="OK", font=("Times", 20), command=lambda: self.colour_code_change(self.code)).pack()

    def gaming_window(self, top=1):
        bgc = self.background_colour_code
        self.header_menu1()

        self.frame1 = Frame(self.root)
        self.frame1.pack()
        l1 = Label(self.frame1, text=self.D2['Player_1']['Name'] + " - " + str(self.D2['Player_1']['Total_win']), fg=self.D2['Player_1']['Colour'], font=("Times", 17)).pack(side=LEFT)

        if top == 1:
            if bgc == self.D2['Player_1']['Colour']:
                l2 = Label(self.frame1, text=" Turn of " + self.D2['Player_1']['Name'] + " ", bg=bgc, fg="#fff", font=("Times", 20)).pack(side=LEFT)
            else:
                l2 = Label(self.frame1, text=" Turn of " + self.D2['Player_1']['Name'] + " ", bg=bgc, fg=self.D2['Player_1']['Colour'], font=("Times", 20)).pack(side=LEFT)
            top = 2
        else:
            if bgc == self.D2['Player_2']['Colour']:
                l2 = Label(self.frame1, text=" Turn of " + self.D2['Player_2']['Name'] + " ", bg=bgc, fg="#fff", font=("Times", 20)).pack(side=LEFT)
            else:
                l2 = Label(self.frame1, text=" Turn of " + self.D2['Player_2']['Name'] + " ", bg=bgc, fg=self.D2['Player_2']['Colour'], font=("Times", 20)).pack(side=LEFT)
            top = 1

        l3 = Label(self.frame1, text=self.D2['Player_2']['Name'] + " - " + str(self.D2['Player_2']['Total_win']), fg=self.D2['Player_2']['Colour'], font=("Times", 17)).pack(side=LEFT)

        self.frame2 = Frame(self.root)
        self.frame2.pack()
        if self.D1['1'] is None:
            b1 = Button(self.frame2, text="", font=("Times", 32), height=2, width=5, command=lambda: self.gaming_rule(top, 1)).pack(side=LEFT)
        else:
            b1 = Button(self.frame2, text=self.D1['1'], fg=self.D0['1'], height=2, width=5, font=("Times", 32)).pack(side=LEFT)
        if self.D1['2'] is None:
            b2 = Button(self.frame2, text="", height=2, width=5, font=("Times", 32), command=lambda: self.gaming_rule(top, 2)).pack(side=LEFT)
        else:
            b2 = Button(self.frame2, text=self.D1['2'], height=2, width=5, fg=self.D0['2'], font=("Times", 32)).pack(side=LEFT)
        if self.D1['3'] is None:
            b3 = Button(self.frame2, text="", width=5, height=2, font=("Times", 32), command=lambda: self.gaming_rule(top, 3)).pack(side=LEFT)
        else:
            b3 = Button(self.frame2, text=self.D1['3'], width=5, height=2, fg=self.D0['3'], font=("Times", 32)).pack(side=LEFT)

        self.frame3 = Frame(self.root)
        self.frame3.pack()
        if self.D1['4'] is None:
            b4 = Button(self.frame3, text="", width=5, font=("Times", 32), height=2, command=lambda: self.gaming_rule(top, 4)).pack(side=LEFT)
        else:
            b4 = Button(self.frame3, text=self.D1['4'], width=5, fg=self.D0['4'], height=2, font=("Times", 32)).pack(side=LEFT)
        if self.D1['5'] is None:
            b5 = Button(self.frame3, text="", width=5, font=("Times", 32), height=2, command=lambda: self.gaming_rule(top, 5)).pack(side=LEFT)
        else:
            b5 = Button(self.frame3, text=self.D1['5'], width=5, fg=self.D0['5'], height=2, font=("Times", 32)).pack(side=LEFT)
        if self.D1['6'] is None:
            b6 = Button(self.frame3, text="", width=5, height=2, font=("Times", 32), command=lambda: self.gaming_rule(top, 6)).pack(side=LEFT)
        else:
            b6 = Button(self.frame3, text=self.D1['6'], width=5, height=2, fg=self.D0['6'], font=("Times", 32)).pack(side=LEFT)

        self.frame4 = Frame(self.root)
        self.frame4.pack()
        if self.D1['7'] is None:
            b7 = Button(self.frame4, text="", width=5, font=("Times", 32), height=2,  command=lambda: self.gaming_rule(top, 7)).pack(side=LEFT)
        else:
            b7 = Button(self.frame4, text=self.D1['7'], width=5, fg=self.D0['7'], height=2, font=("Times", 32)).pack(side=LEFT)
        if self.D1['8'] is None:
            b8 = Button(self.frame4, text="", width=5, font=("Times", 32), height=2, command=lambda: self.gaming_rule(top, 8)).pack(side=LEFT)
        else:
            b8 = Button(self.frame4, text=self.D1['8'], height=2, width=5, fg=self.D0['8'], font=("Times", 32)).pack(side=LEFT)
        if self.D1['9'] is None:
            b9 = Button(self.frame4, text="", height=2,  width=5, font=("Times", 32), command=lambda: self.gaming_rule(top, 9)).pack(side=LEFT)
        else:
            b9 = Button(self.frame4, text=self.D1['9'], height=2, width=5, fg=self.D0['9'], font=("Times", 32)).pack(side=LEFT)

    def wining_gui_window(self):
        if self.highlight_text == 1:
            self.D4['1'] = 1
            self.D4['2'] = 1
            self.D4['3'] = 1
        elif self.highlight_text == 2:
            self.D4['1'] = 1
            self.D4['4'] = 1
            self.D4['7'] = 1
        elif self.highlight_text == 3:
            self.D4['1'] = 1
            self.D4['5'] = 1
            self.D4['9'] = 1
        elif self.highlight_text == 4:
            self.D4['2'] = 1
            self.D4['5'] = 1
            self.D4['8'] = 1
        elif self.highlight_text == 5:
            self.D4['3'] = 1
            self.D4['5'] = 1
            self.D4['7'] = 1
        elif self.highlight_text == 6:
            self.D4['3'] = 1
            self.D4['6'] = 1
            self.D4['9'] = 1
        elif self.highlight_text == 7:
            self.D4['4'] = 1
            self.D4['5'] = 1
            self.D4['6'] = 1
        elif self.highlight_text == 8:
            self.D4['7'] = 1
            self.D4['8'] = 1
            self.D4['9'] = 1

        self.frame1 = Frame(self.root)
        self.frame1.pack()
        l1 = Label(self.frame1, text=self.D2['Player_1']['Name'] + " - " + str(self.D2['Player_1']['Total_win']), fg=self.D2['Player_1']['Colour'], font=("Times", 17)).pack(side=LEFT)
        l2 = Label(self.frame1, text="\t", bg=self.background_colour_code, font=("Times", 19)).pack(side=LEFT)
        l3 = Label(self.frame1, text=self.D2['Player_2']['Name'] + " - " + str(self.D2['Player_2']['Total_win']), fg=self.D2['Player_2']['Colour'], font=("Times", 17)).pack(side=LEFT)

        self.frame2 = Frame(self.root)
        self.frame2.pack()
        if self.D4['1'] == 1:
            b1 = Button(self.frame2, text=self.D1['1'], fg=self.D0['1'], height=2, width=5, font=("Times", 32)).pack(side=LEFT)
        else:
            b1 = Button(self.frame2, text=self.D1['1'], bg=self.D0['1'], fg="#fff", height=2, width=5, font=("Times", 32)).pack(side=LEFT)
        if self.D4['2'] == 1:
            b2 = Button(self.frame2, text=self.D1['2'], fg=self.D0['2'], height=2, width=5, font=("Times", 32)).pack(side=LEFT)
        else:
            b2 = Button(self.frame2, text=self.D1['2'], bg=self.D0['2'], fg="#fff", height=2, width=5, font=("Times", 32)).pack(side=LEFT)
        if self.D4['3'] == 1:
            b3 = Button(self.frame2, text=self.D1['3'], fg=self.D0['3'], width=5, height=2, font=("Times", 32)).pack(side=LEFT)
        else:
            b3 = Button(self.frame2, text=self.D1['3'], bg=self.D0['3'], fg="#fff", width=5, height=2, font=("Times", 32)).pack(side=LEFT)

        self.frame3 = Frame(self.root)
        self.frame3.pack()
        if self.D4['4'] == 1:
            b4 = Button(self.frame3, text=self.D1['4'], fg=self.D0['4'], width=5, height=2, font=("Times", 32)).pack(side=LEFT)
        else:
            b4 = Button(self.frame3, text=self.D1['4'], bg=self.D0['4'], fg="#fff", width=5, height=2, font=("Times", 32)).pack(side=LEFT)
        if self.D4['5'] == 1:
            b5 = Button(self.frame3, text=self.D1['5'], fg=self.D0['5'], width=5, height=2, font=("Times", 32)).pack(side=LEFT)
        else:
            b5 = Button(self.frame3, text=self.D1['5'], bg=self.D0['5'], fg="#fff", width=5, height=2, font=("Times", 32)).pack(side=LEFT)
        if self.D4['6'] == 1:
            b6 = Button(self.frame3, text=self.D1['6'], fg=self.D0['6'], width=5, height=2, font=("Times", 32)).pack(side=LEFT)
        else:
            b6 = Button(self.frame3, text=self.D1['6'], bg=self.D0['6'], fg="#fff", width=5, height=2, font=("Times", 32)).pack(side=LEFT)

        self.frame4 = Frame(self.root)
        self.frame4.pack()
        if self.D4['7'] == 1:
            b7 = Button(self.frame4, text=self.D1['7'], fg=self.D0['7'], width=5, height=2, font=("Times", 32)).pack(side=LEFT)
        else:
            b7 = Button(self.frame4, text=self.D1['7'], bg=self.D0['7'], fg="#fff", width=5, height=2, font=("Times", 32)).pack(side=LEFT)
        if self.D4['8'] == 1:
            b8 = Button(self.frame4, text=self.D1['8'], fg=self.D0['8'], height=2, width=5, font=("Times", 32)).pack(side=LEFT)
        else:
            b8 = Button(self.frame4, text=self.D1['8'], bg=self.D0['8'], fg="#fff", height=2, width=5, font=("Times", 32)).pack(side=LEFT)
        if self.D4['9'] == 1:
            b9 = Button(self.frame4, text=self.D1['9'], fg=self.D0['9'], height=2, width=5, font=("Times", 32)).pack(side=LEFT)
        else:
            b9 = Button(self.frame4, text=self.D1['9'], bg=self.D0['9'], fg="#fff", height=2, width=5, font=("Times", 32)).pack(side=LEFT)

        if self.p_id == 1:
            data = messagebox.askyesno("Congrats!", self.D2['Player_1']['Name'] + " Win. Are you want to play again?")
        elif self.p_id == 2:
            data = messagebox.askyesno("Congrats!", self.D2['Player_2']['Name'] + " Win. Are you want to play again?")
        else:
            data = messagebox.askyesno("Congrats!", "Match draw. Are you want to play again?")
        if data is True:
            self.refresh_window(self.gaming_window, "TRUE")
        else:
            self.refresh_window(self.load_1st_window, "FALSE")

    def symbol_change(self, sym, btn):
        if btn == 1:
            self.D2['Player_1']['Symbol'] = sym
        else:
            self.D2['Player_2']['Symbol'] = sym

    def symbol_colour_change(self, colour, btn):
        if btn == 1:
            self.D2['Player_1']['Colour'] = colour
        else:
            self.D2['Player_2']['Colour'] = colour

    def symbol_change_gui(self, btn):
        self.header_menu2()

        self.label0 = Label(self.root, text="Press the symbol which you want", font=("Times", 20, "bold")).pack(pady=(20, 10))

        self.frame1 = Frame(self.root)
        self.frame1.pack()
        b1 = Button(self.frame1, text="α", font=("Times", 25), command=lambda: self.symbol_change("α", btn)).pack(side=LEFT)
        b2 = Button(self.frame1, text="β", font=("Times", 25), command=lambda: self.symbol_change("β", btn)).pack(side=LEFT)
        b3 = Button(self.frame1, text="µ", font=("Times", 25), command=lambda: self.symbol_change("µ", btn)).pack(side=LEFT)
        b4 = Button(self.frame1, text="π", font=("Times", 25), command=lambda: self.symbol_change("π", btn)).pack(side=LEFT)
        b5 = Button(self.frame1, text="Ω", font=("Times", 25), command=lambda: self.symbol_change("Ω", btn)).pack(side=LEFT)
        b6 = Button(self.frame1, text="∑", font=("Times", 25), command=lambda: self.symbol_change("∑", btn)).pack(side=LEFT)
        b7 = Button(self.frame1, text="∏", font=("Times", 25), command=lambda: self.symbol_change("∏", btn)).pack(side=LEFT)
        b8 = Button(self.frame1, text="£", font=("Times", 25), command=lambda: self.symbol_change("£", btn)).pack(side=LEFT)

        self.frame2 = Frame(self.root)
        self.frame2.pack()
        b9 = Button(self.frame2, text="!", font=("Times", 25), command=lambda: self.symbol_change("!", btn)).pack(side=LEFT)
        b10 = Button(self.frame2, text="@", font=("Times", 25), command=lambda: self.symbol_change("@", btn)).pack(side=LEFT)
        b11 = Button(self.frame2, text="#", font=("Times", 25), command=lambda: self.symbol_change("#", btn)).pack(side=LEFT)
        b12 = Button(self.frame2, text="$", font=("Times", 25), command=lambda: self.symbol_change("$", btn)).pack(side=LEFT)
        b13 = Button(self.frame2, text="%", font=("Times", 25), command=lambda: self.symbol_change("%", btn)).pack(side=LEFT)
        b14 = Button(self.frame2, text="€", font=("Times", 25), command=lambda: self.symbol_change("€", btn)).pack(side=LEFT)
        b15 = Button(self.frame2, text="&", font=("Times", 25), command=lambda: self.symbol_change("&", btn)).pack(side=LEFT)
        b16 = Button(self.frame2, text="*", font=("Times", 25), command=lambda: self.symbol_change("*", btn)).pack(side=LEFT)
        b17 = Button(self.frame2, text="/", font=("Times", 25), command=lambda: self.symbol_change("/", btn)).pack(side=LEFT)

        self.frame3 = Frame(self.root)
        self.frame3.pack()
        b18 = Button(self.frame3, text="+", font=("Times", 25), command=lambda: self.symbol_change("+", btn)).pack(side=LEFT)
        b19 = Button(self.frame3, text="-", font=("Times", 25), command=lambda: self.symbol_change("-", btn)).pack(side=LEFT)
        b20 = Button(self.frame3, text="^", font=("Times", 25), command=lambda: self.symbol_change("^", btn)).pack(side=LEFT)
        b21 = Button(self.frame3, text="=", font=("Times", 25), command=lambda: self.symbol_change("=", btn)).pack(side=LEFT)
        b22 = Button(self.frame3, text="≠", font=("Times", 25), command=lambda: self.symbol_change("≠", btn)).pack(side=LEFT)
        b23 = Button(self.frame3, text="~", font=("Times", 25), command=lambda: self.symbol_change("~", btn)).pack(side=LEFT)
        b24 = Button(self.frame3, text="<", font=("Times", 25), command=lambda: self.symbol_change("<", btn)).pack(side=LEFT)
        b25 = Button(self.frame3, text=">", font=("Times", 25), command=lambda: self.symbol_change(">", btn)).pack(side=LEFT)
        b26 = Button(self.frame3, text="?", font=("Times", 25), command=lambda: self.symbol_change("?", btn)).pack(side=LEFT)

        self.frame4 = Frame(self.root)
        self.frame4.pack()
        b27 = Button(self.frame4, text="a", font=("Times", 25), command=lambda: self.symbol_change("a", btn)).pack(side=LEFT)
        b28 = Button(self.frame4, text="b", font=("Times", 25), command=lambda: self.symbol_change("b", btn)).pack(side=LEFT)
        b29 = Button(self.frame4, text="c", font=("Times", 25), command=lambda: self.symbol_change("c", btn)).pack(side=LEFT)
        b30 = Button(self.frame4, text="d", font=("Times", 25), command=lambda: self.symbol_change("d", btn)).pack(side=LEFT)
        b31 = Button(self.frame4, text="e", font=("Times", 25), command=lambda: self.symbol_change("e", btn)).pack(side=LEFT)
        b32 = Button(self.frame4, text="f", font=("Times", 25), command=lambda: self.symbol_change("f", btn)).pack(side=LEFT)
        b33 = Button(self.frame4, text="g", font=("Times", 25), command=lambda: self.symbol_change("g", btn)).pack(side=LEFT)
        b34 = Button(self.frame4, text="h", font=("Times", 25), command=lambda: self.symbol_change("h", btn)).pack(side=LEFT)
        b35 = Button(self.frame4, text="i", font=("Times", 25), command=lambda: self.symbol_change("i", btn)).pack(side=LEFT)
        b36 = Button(self.frame4, text="j", font=("Times", 25), command=lambda: self.symbol_change("j", btn)).pack(side=LEFT)

        self.frame5 = Frame(self.root)
        self.frame5.pack()
        b37 = Button(self.frame5, text="k", font=("Times", 25), command=lambda: self.symbol_change("k", btn)).pack(side=LEFT)
        b38 = Button(self.frame5, text="l", font=("Times", 25), command=lambda: self.symbol_change("l", btn)).pack(side=LEFT)
        b39 = Button(self.frame5, text="m", font=("Times", 25), command=lambda: self.symbol_change("m", btn)).pack(side=LEFT)
        b40 = Button(self.frame5, text="n", font=("Times", 25), command=lambda: self.symbol_change("n", btn)).pack(side=LEFT)
        b41 = Button(self.frame5, text="o", font=("Times", 25), command=lambda: self.symbol_change("o", btn)).pack(side=LEFT)
        b42 = Button(self.frame5, text="p", font=("Times", 25), command=lambda: self.symbol_change("p", btn)).pack(side=LEFT)
        b43 = Button(self.frame5, text="q", font=("Times", 25), command=lambda: self.symbol_change("q", btn)).pack(side=LEFT)
        b44 = Button(self.frame5, text="r", font=("Times", 25), command=lambda: self.symbol_change("r", btn)).pack(side=LEFT)
        b45 = Button(self.frame5, text="s", font=("Times", 25), command=lambda: self.symbol_change("s", btn)).pack(side=LEFT)

        self.frame6 = Frame(self.root)
        self.frame6.pack()
        b46 = Button(self.frame6, text="t", font=("Times", 25), command=lambda: self.symbol_change("t", btn)).pack(side=LEFT)
        b47 = Button(self.frame6, text="u", font=("Times", 25), command=lambda: self.symbol_change("u", btn)).pack(side=LEFT)
        b48 = Button(self.frame6, text="v", font=("Times", 25), command=lambda: self.symbol_change("v", btn)).pack(side=LEFT)
        b49 = Button(self.frame6, text="w", font=("Times", 25), command=lambda: self.symbol_change("w", btn)).pack(side=LEFT)
        b50 = Button(self.frame6, text="x", font=("Times", 25), command=lambda: self.symbol_change("x", btn)).pack(side=LEFT)
        b51 = Button(self.frame6, text="y", font=("Times", 25), command=lambda: self.symbol_change("y", btn)).pack(side=LEFT)
        b52 = Button(self.frame6, text="z", font=("Times", 25), command=lambda: self.symbol_change("z", btn)).pack(side=LEFT)
        b53 = Button(self.frame6, text="X", font=("Times", 25), command=lambda: self.symbol_change("X", btn)).pack(side=LEFT)
        b53 = Button(self.frame6, text="O", font=("Times", 25), command=lambda: self.symbol_change("O", btn)).pack(side=LEFT)

        self.frame7 = Frame(self.root)
        self.frame7.pack()

        b54 = Button(self.root, text="Colour change", fg="#FF5357", font=("Times", 20), command=lambda: self.load_new_gui(new_gui=self.symbol_colour_change_gui, btn=btn)).pack()

    def symbol_colour_change_gui(self, btn):
        self.header_menu2()

        self.label0 = Label(self.root, text="Press the  Colour which you want", font=("Times", 20, "bold")).pack(pady=(20, 10))

        self.frame1 = Frame(self.root)
        self.frame1.pack()
        b1 = Button(self.frame1, text="\t", bg="#3498db", font=("Times", 20), command=lambda: self.symbol_colour_change("#3498db", btn)).pack(side=LEFT)
        b2 = Button(self.frame1, text="\t", bg="red", font=("Times", 20), command=lambda: self.symbol_colour_change("red", btn)).pack(side=LEFT)
        b3 = Button(self.frame1, text="\t", bg="blue", font=("Times", 20), command=lambda: self.symbol_colour_change("blue", btn)).pack(side=LEFT)

        self.frame2 = Frame(self.root)
        self.frame2.pack()
        b4 = Button(self.frame2, text="\t", bg="yellow", font=("Times", 20), command=lambda: self.symbol_colour_change("yellow", btn)).pack(side=LEFT)
        b5 = Button(self.frame2, text="\t", bg="green", font=("Times", 20), command=lambda: self.symbol_colour_change("green", btn)).pack(side=LEFT)
        b6 = Button(self.frame2, text="\t", bg="#A3CB38", font=("Times", 20), command=lambda: self.symbol_colour_change("#A3CB38", btn)).pack(side=LEFT)

        self.frame3 = Frame(self.root)
        self.frame3.pack()
        b7 = Button(self.frame3, text="\t", bg="brown", font=("Times", 20), command=lambda: self.symbol_colour_change("brown", btn)).pack(side=LEFT)
        b8 = Button(self.frame3, text="\t", bg="#6F1E51", font=("Times", 20), command=lambda: self.symbol_colour_change("#6F1E51", btn)).pack(side=LEFT)
        b9 = Button(self.frame3, text="\t", bg="#9980FA", font=("Times", 20), command=lambda: self.symbol_colour_change("#9980FA", btn)).pack(side=LEFT)

        self.frame4 = Frame(self.root)
        self.frame4.pack()
        b10 = Button(self.frame4, text="\t", bg="#16a085", font=("Times", 20), command=lambda: self.symbol_colour_change("#16a085", btn)).pack(side=LEFT)
        b11 = Button(self.frame4, text="\t", bg="#e67e22", font=("Times", 20), command=lambda: self.symbol_colour_change("#e67e22", btn)).pack(side=LEFT)
        b12 = Button(self.frame4, text="\t", bg="#c0392b", font=("Times", 20), command=lambda: self.symbol_colour_change("#c0392b", btn)).pack(side=LEFT)

        self.frame5 = Frame(self.root)
        self.frame5.pack()
        b13 = Button(self.frame5, text="\t", bg="#9b59b6", font=("Times", 20), command=lambda: self.symbol_colour_change("#9b59b6", btn)).pack(side=LEFT)
        b14 = Button(self.frame5, text="\t", bg="#1B1464", font=("Times", 20), command=lambda: self.symbol_colour_change("#1B1464", btn)).pack(side=LEFT)
        b15 = Button(self.frame5, text="\t", bg="black", font=("Times", 20), command=lambda: self.symbol_colour_change("black", btn)).pack(side=LEFT)

        self.frame6 = Frame(self.root)
        self.frame6.pack()
        b16 = Button(self.frame6, text="\t", bg="#7f8c8d", font=("Times", 20), command=lambda: self.symbol_colour_change("#7f8c8d", btn)).pack(side=LEFT)
        b17 = Button(self.frame6, text="\t", bg="#fdcb6e", font=("Times", 20), command=lambda: self.symbol_colour_change("#fdcb6e", btn)).pack(side=LEFT)
        b18 = Button(self.frame6, text="\t", bg="#81ecec", font=("Times", 20), command=lambda: self.symbol_colour_change("#81ecec", btn)).pack(side=LEFT)

        self.frame7 = Frame(self.root)
        self.frame7.pack()
        b19 = Button(self.frame7, text="\t", bg="#006266", font=("Times", 20), command=lambda: self.symbol_colour_change("#006266", btn)).pack(side=LEFT)
        b20 = Button(self.frame7, text="\t", bg="#D980FA", font=("Times", 20), command=lambda: self.symbol_colour_change("#D980FA", btn)).pack(side=LEFT)
        b21 = Button(self.frame7, text="\t", bg="#FF5357", font=("Times", 20), command=lambda: self.symbol_colour_change("#FF5357", btn)).pack(side=LEFT)

        b22 = Button(self.root, text="OK", fg="#FF5357", font=("Times", 20), command=lambda: self.load_new_gui(self.load_2nd_window, self.background_colour_code)).pack()


Game()
