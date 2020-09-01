from tkinter import *
import subprocess

root = Tk() 
root.wm_title("PT-Menu")
root.config(background = "#EEEEEE", borderwidth=0, relief=RAISED) # Hintergrundfarbe des Fensters
 
wwidth = 907 
wheight= 460
   
def center_window(width=wwidth, height=wheight):
    # get screen width and height 
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

center_window(wwidth, wheight)

mainFrame = Frame(root, width=wwidth, height = wheight,  background="#EEEEEE")
mainFrame.grid(row=0, column=0, padx=3, pady=3, sticky="NESW")

# each programm button need here below a Name to idetify and a command that will be excecuted to start the progamm
def execProg(ProgName):
    print(ProgName)
    mycmd = ""
    if (ProgName == "Exit") or (ProgName == "Ende") or (ProgName == "Fin") or (ProgName == "End"):
        exit()
    elif ProgName == "Notepad":
        mycmd = [r"notepad.exe"]
    elif ProgName == "Explorer":
        mycmd = [r"C:\Program Files\internet explorer\iexplore.exe"]
    elif ProgName == "Chrome":
        mycmd = [r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"]
    elif ProgName == "Google":
        mycmd = [r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe", "https://www.Google.de"]
    elif ProgName == "Firefox":
        mycmd = [r"C:\Program Files\Mozilla Firefox\firefox.exe"]
    elif (ProgName == "Rechner") or (ProgName == "Calc"):
         mycmd=[r"calc.exe"]
    elif ProgName == "Paint":
         mycmd = [r"mspaint.exe"]
    elif ProgName == "W10 Settings":
        mycmd = [r"start", "ms-settings:"]
    elif ProgName == "Outlook":
        mycmd = [r"start", "outlook"]
    elif ProgName == "Excel":
        mycmd = [r"start", "excel"]
    elif ProgName == "Word":
        mycmd = [r"start", "winword"]
    elif ProgName == "Powerpoint":
        mycmd = [r"start", "powerpnt"]
    elif ProgName == "Solitaire":
        mycmd = [r"start", "xboxliveapp-1297287741:"]
    elif ProgName == "Cmd":
        mycmd = [r"start", "cmd.exe"]
    elif ProgName == "Teamviewer":
        mycmd = [r"C:\Program Files (x86)\TeamViewer\TeamViewer.exe"]
    ### must be the last line here, to execute the mycmd ###
    if mycmd != "":
        ret = subprocess.Popen(mycmd, shell=True)

def prgaccess(ipid, prglst):
    execProg(prglst[ipid] )
    
def Create_btline(self, myrow, prglst):
    mybg="#6666FF"
    myfg="white"
    for i in range(0, 4):
        if (prglst[i] == "Ende") or (prglst[i] == "Exit"):
            mybg="#FF5555"
        self.newmessage = Button(self, text= prglst[i], command = lambda i=i: prgaccess(i, prglst),  font=("Arial",14), bg=mybg, fg=myfg, width=19, height=3)
        self.newmessage.config(height = 3, width = 19)
        self.newmessage.grid(row = myrow, column = i, padx=3, pady=3, sticky = NW)

prglst = ["Calc", "Notepad", "Solitaire", "Paint" ]
Create_btline(mainFrame, 1, prglst)

prglst = ["Outlook","Excel", "Word", "Powerpoint" ]
Create_btline(mainFrame, 2, prglst)

prglst = ["Chrome", "Explorer", "Firefox", "Google" ]
Create_btline(mainFrame, 3, prglst)

#prglst = ["Google", "-", "-", "-" ]
#Create_btline(mainFrame, 4, prglst)

prglst = ["Cmd", "W10 Settings", "Teamviewer", "Exit" ]
Create_btline(mainFrame, 5, prglst)
 
root.mainloop()
