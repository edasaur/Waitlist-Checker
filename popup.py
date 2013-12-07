from Tkinter import *

def showNotification(pausetime, textToDisplay):

    ## Create main window
    root = Tk()
    w = Button(root, text=textToDisplay, activebackground="blue", bg="red", command=lambda: root.destroy())
    w.pack(side=LEFT)
    w.flash()
    root.update_idletasks()
    # Remove window decorations
    root.overrideredirect(1)
    root.wm_attributes("-topmost", 1)
    
    timeOut = int(pausetime*1000) # Convert to ms from s
    ## Run appliction
    root.after(timeOut,root.destroy)
    root.mainloop()
