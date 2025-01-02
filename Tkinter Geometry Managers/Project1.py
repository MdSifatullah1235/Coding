from tkinter import *

window = Tk()
window.title("Number Pad")
window.geometry("250x300")

nums = [[9,8,7],[6,5,4],[3,2,1],["#",0,"*"]]

for i in range(4):
    window.columnconfigure(i,weight=1,minsize=83)
    window.rowconfigure(i,weight=1,minsize=50)

for i in range(4):
    for j in range(3):
        frame = Frame(master=window,relief=RIDGE,borderwidth=1,bg="#eda137")
        frame.grid(row=i,column=j,sticky="nsew")

        label = Label(master=frame,text=nums[i][j],bg="#eda137",font=("Arial",20))
        label.pack(expand=True,fill=BOTH,padx=5,pady=5)
    
window.mainloop()
