from Tkinter import *

def showNotification(notificationTimeout, textToDisplay):

    ## Create main window
    root = Tk()
    Button(root, text=textToDisplay, activebackground="white", bg="white", command=lambda: root.destroy()).pack(side=LEFT)

    root.update_idletasks()
    # Remove window decorations
    root.overrideredirect(1)
    root.wm_attributes("-topmost", 1)
    timeOut = int(notificationTimeout*1000) # Convert to ms from s

    ## Run appliction
    root.after(timeOut,root.destroy)
    root.mainloop()
