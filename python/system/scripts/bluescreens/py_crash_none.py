import tkinter as tk
import tkinter.font as tkFont
import subprocess
error = "something happened and we couldnt get the error message! sorry!"
class App:
    def __init__(self, root):
        #setting title
        root.title("woops!")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        root.configure(bg="blue")
        GButton_145=tk.Button(root)
        GButton_145["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_145["font"] = ft
        GButton_145["bg"] = "blue"
        GButton_145["fg"] = "white"
        GButton_145["justify"] = "center"
        GButton_145["text"] = "restart"
        GButton_145.place(x=0,y=470,width=596,height=30)
        GButton_145["command"] = self.scat

        GLabel_688=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_688["font"] = ft
        GLabel_688["fg"] = "white"
        GLabel_688["bg"] = "blue"
        GLabel_688["justify"] = "center"
        GLabel_688["text"] = "well that doesnt seem too great!"
        GLabel_688["relief"] = "raised"
        GLabel_688.place(x=160,y=0,width=246,height=30)

        GLabel_735=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_735["font"] = ft
        GLabel_735["bg"] = "blue"
        GLabel_735["fg"] = "white"
        GLabel_735["justify"] = "center"
        GLabel_735["text"] = "so it seems like pythonicOS has crashed? or it just wanted to do this because it could?"
        GLabel_735.place(x=10,y=50,width=612,height=30)

        GLabel_544=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_544["font"] = ft
        GLabel_544["bg"] = "blue"
        GLabel_544["fg"] = "white"
        GLabel_544["justify"] = "center"
        GLabel_544["text"] = "here is the error message that you got, well if you got any?"
        GLabel_544.place(x=130,y=100,width=353,height=30)

        GLabel_42=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_42["font"] = ft
        GLabel_42["bg"] = "blue"
        GLabel_42["fg"] = "white"
        GLabel_42["justify"] = "center"
        GLabel_42["text"] = error
        GLabel_42.place(x=120,y=170,width=350 ,height=50)

        GLabel_508=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_508["font"] = ft
        GLabel_508["bg"] = "blue"
        GLabel_508["fg"] = "white"
        GLabel_508["justify"] = "center"
        GLabel_508["text"] = "if you could be so great and hit that button on the bottom for me, ill take care of the rest!"
        GLabel_508.place(x=0,y=240,width=594,height=30)

        GLabel_164=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_164["font"] = ft
        GLabel_164["bg"] = "blue"
        GLabel_164["fg"] = "white"
        GLabel_164["justify"] = "center"
        GLabel_164["text"] = "if you could before you go, could you please open a issue on "
        GLabel_164.place(x=0,y=340,width=550,height=30)

        GLabel_844=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_844["font"] = ft
        GLabel_844["bg"] = "blue"
        GLabel_844["fg"] = "white"
        GLabel_844["justify"] = "center"
        GLabel_844["text"] = "cheers!"
        GLabel_844.place(x=250,y=410,width=70,height=25)

        GLabel_4=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_4["font"] = ft
        GLabel_4["bg"] = "blue"
        GLabel_4["fg"] = "white"
        GLabel_4["justify"] = "center"
        GLabel_4["text"] = "github.com/OpenStudioCorp/PythonicOS with your error code please? that will help out alot!"
        GLabel_4.place(x=10,y=380,width=599,height=30)

    def scat(self):
        subprocess.Popen["python","../PythonicOS.py"]

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
