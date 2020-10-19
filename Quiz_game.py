try:
    import tkinter as tk                # python 3
    from tkinter import font as tkfont  # python 3
except ImportError:
    import Tkinter as tk     # python 2
    import tkFont as tkfont  # python 2
    import time
    from tkinter.messagebox import showinfo



class SampleApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family='Helvetica', size=18, weight="bold", slant="italic")

        # the container is where we'll stack a bunch of frames
        # on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (Login_Page, Register_page, Home_Page, Level_Window, Level_One, Level_Two, Level_Three, Level_four):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame

            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Login_Page")

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class Login_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Bold_lebel = tk.Label(self, text = "LOGIN FORM", font = ('', 30, 'bold')).place(x = 230, y = 30)


        # label of user
        username_label = tk.Label(self,text = "Username :- ", font = 18, fg = "black").place(x = 100, y = 130)
        # username entry
        username_entry = tk.Entry(self, width = 25, font = 6).place(x = 235, y = 134)

        # label of pass
        password_label = tk.Label(self,text = "Password :- ", font = 18, fg = "black").place(x = 100, y = 180)
        # password entry
        password_entry = tk.Entry(self, width = 25, font = 6, show="*").place(x = 235, y = 184)

        button_submit = tk.Button(self,text = "Login", width = 15, height = 2, bd = 2, bg = "green", activebackground = "green",
                           command=lambda: controller.show_frame("Home_Page")).place(x = 210, y = 240)

        button_register = tk.Button(self,text = "SignUp", width = 15, height = 2, bd = 2, bg = "orange", activebackground = "orange",
                           command=lambda: controller.show_frame("Register_page")).place(x = 350, y = 240)


class Register_page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        Bold_lebel = tk.Label(self, text = "REGISTRATION FORM", font = ('', 30, 'bold')).place(x = 150, y = 30)

        username_label = tk.Label(self,text = "Username :- ", font = 18, fg = "black").place(x = 120, y = 110)
        # username entry
        username_entry = tk.Entry(self, width = 25, font = 6).place(x = 295, y = 110)

        fullname_label = tk.Label(self,text = "Full-Name :- ", font = 18, fg = "black").place(x = 120, y = 150)
        # username entry
        fullname_entry = tk.Entry(self, width = 25, font = 6).place(x = 295, y = 150)

        email_label = tk.Label(self,text = "E-Mail Address :- ", font = 18, fg = "black").place(x = 120, y = 190)
        # username entry
        email_entry = tk.Entry(self, width = 25, font = 6).place(x = 295, y = 190)

        password_label = tk.Label(self,text = "Password :- ", font = 18, fg = "black").place(x = 120, y = 230)
        # username entry
        password_entry = tk.Entry(self, width = 25, font = 6, show="*").place(x = 295, y = 230)

        # label of pass
        password = tk.Label(self,text = "Re-enter Password :- ", font = 18, fg = "black").place(x = 120, y = 270)
        # password entry
        password_entry = tk.Entry(self, width = 25, font = 6, show="*").place(x = 295, y = 270)

        register_button = tk.Button(self,text = "REGISTER", width = 15, height = 2, bd = 2, bg = "green", activebackground = "green",
                           command=lambda: controller.show_frame("Login_Page")).place(x = 210, y = 330)
        
        Back_to_Login = tk.Button(self,text = "Back", width = 15, height = 2, bd = 2, bg = "red", activebackground = "red",
                           command=lambda: controller.show_frame("Login_Page")).place(x = 350, y = 330)

        


class Home_Page(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        Bold_lebel = tk.Label(self, text = "----::INSTRUCTIONS::----", font = ('', 30, 'bold')).place(x = 120, y = 30)

        message = tk.Label(self, text = "\t***********************************************************************\n\t1. Total Quiz Time is : 5:00 Min\n 2. Total Questions : 15\n\t""   3. Total Score : 15 X 20 = 300\n\t\t" "    4. Please select appropriate option at once\n\t\t\tas you have only one chance to select.\n\t\t Good Luck !\n\t***********************************************************************").place(x = 130, y = 100)

        Back_to_Login = tk.Button(self,text = "START QUIZ", width = 20, height = 2, bd = 2, bg = "green", activebackground = "green", font =('', 15, 'bold'),
                           command=lambda: controller.show_frame("Level_Window")).place(x = 250, y = 250)


class Level_Window(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        quiz_name = tk.Label(self, text = "----::CHOOSE LEVEL::----", font = ('', 20, 'bold')).place(x = 200, y = 30)


        Back_to_Login = tk.Button(self,text = "BEGINNER", width = 11, height = 1, bd = 2, bg = "green", activebackground = "green", font =('', 15, 'bold'),
                           command=lambda: controller.show_frame("Level_One")).place(x = 50, y = 250)

        Back_to_Login = tk.Button(self,text = "MODERATE", width = 11, height = 1, bd = 2, bg = "yellow", activebackground = "yellow", font =('', 15, 'bold'),
                           command=lambda: controller.show_frame("Level_Two")).place(x = 200, y = 250)

        Back_to_Login = tk.Button(self,text = "ADVANCE", width = 11, height = 1, bd = 2, bg = "orange", activebackground = "orange", font =('', 15, 'bold'),
                           command=lambda: controller.show_frame("Level_Three")).place(x = 350, y = 250)

        Back_to_Login = tk.Button(self,text = "LEGENDS", width = 11, height = 1, bd = 2, bg = "red", activebackground = "red", font =('', 15, 'bold'),
                           command=lambda: controller.show_frame("Level_four")).place(x = 500, y = 250)


class Level_One(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        ques_frame = tk.Frame(self, height = 120, width = 600, bg = "yellow").place(x = 50, y = 50)
        label_ques1 = tk.Label(self, text = "1. Who discovered New Caledonia and when? ", bg = "yellow",anchor="center").place(x = 50, y = 50)

        Back_to_Login = tk.Button(self,text = "James Cook, 1774", width = 19, height = 1, bd = 2, bg = "white", activebackground = "white", font =('', 15, 'bold'),
                           command=lambda: controller.show_frame("")).place(x = 80, y = 250)

        Back_to_Login = tk.Button(self,text = "James Watson, 1779", width = 19, height = 1, bd = 2, bg = "white", activebackground = "white", font =('', 15, 'bold'),
                           command=lambda: controller.show_frame("")).place(x = 390, y = 250)

        Back_to_Login = tk.Button(self,text = "Benjamin Cabrera, 1776", width = 19, height = 1, bd = 2, bg = "white", activebackground = "white", font =('', 15, 'bold'),
                           command=lambda: controller.show_frame("")).place(x = 80, y = 320)

        Back_to_Login = tk.Button(self,text = "John Dalton, 1770", width = 19, height = 1, bd = 2, bg = "white", activebackground = "white", font =('', 15, 'bold'),
                           command=lambda: controller.show_frame("")).place(x = 390, y = 320)

        Back_to_Login = tk.Button(self,text = "NEXT", width = 20, height = 2, bd = 2, bg = "green", activebackground = "green", font =('', 15, 'bold'),
                           command=lambda: controller.show_frame("")).place(x = 230, y = 380)

class Level_Two(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


class Level_Three(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


class Level_four(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller



        
    
    



if __name__ == "__main__":
    app = SampleApp()
    app.title("REGISTER")
    app.geometry("700x500+200+150")
    app.mainloop()