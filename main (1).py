from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import csv

class Management:
    def __init__(self, file, parent):
        self.file = file
        self.parent = parent
        
        self.IDs = []
        self.data = []
        if len(self.data) == 0:
            self.load()
        
        self.parent.geometry("330x350")
        self.parent.configure(bg="#56CCF2")
        self.parent.title("Student Information System")
        self.parent.resizable(False, False)
        
        self.school = Image.open("university.png")
        self.resizedSchool = self.school.resize((60, 60), Image.ANTIALIAS)
        self.newSchool = ImageTk.PhotoImage(self.resizedSchool)
        
        self.male = Image.open("graduate.png")
        self.resizedMale = self.male.resize((50, 50), Image.ANTIALIAS)
        self.newMale = ImageTk.PhotoImage(self.resizedMale)
        
        self.female = Image.open("graduatetwo.png")
        self.resizedFemale = self.female.resize((50, 50), Image.ANTIALIAS)
        self.newFemale = ImageTk.PhotoImage(self.resizedFemale)
        
        self.frame = LabelFrame(self.parent, padx=10, pady=10, bg="#FFFFFF", relief=FLAT)
        self.frame.pack(pady=20)
        
        self.frameForPicture = LabelFrame(self.frame, bg="#FFFFFF", relief=FLAT)
        self.frameForPicture.grid(row=0, column=0, rowspan=2, columnspan=2, pady=(0, 20))
        
        Label(self.frameForPicture, image=self.newSchool, bg="#FFFFFF").pack()
        
        self.entryForID = Entry(self.frame, font="Helvetica 8 italic", width=11, justify=RIGHT, relief=FLAT)
        self.entryForID.insert(0, "ID Number: ")
        self.entryForID.configure(state=DISABLED, disabledbackground="#FFFFFF",
                                 disabledforeground="#000000")
        self.id = Entry(self.frame, font="Helvetica 8", width=35, relief=SOLID)
        self.entryForID.grid(row=2, column=0)
        self.id.grid(row=2, column=1)
        
        self.id.insert(0, " 2019-0014")
        self.id.configure(state=DISABLED, disabledbackground="#FFFFFF")
        self.onClickID = self.id.bind("<Button-1>", self.click)
        
        self.entryForName = Entry(self.frame, font="Helvetica 8 italic", width=11, justify=RIGHT, relief=FLAT)
        self.entryForName.insert(0, "Name: ")
        self.entryForName.configure(state=DISABLED, disabledbackground="#FFFFFF",
                                 disabledforeground="#000000")
        self.name = Entry(self.frame, font="Helvetica 8", width=35, relief=SOLID)
        self.entryForName.grid(row=3, column=0, pady=5)
        self.name.grid(row=3, column=1, pady=5)
        
        self.name.insert(0, " Russel Gian")
        self.name.configure(state=DISABLED, disabledbackground="#FFFFFF")
        self.onClickName = self.name.bind("<Button-1>", self.click)
        
        self.entryForSex = Entry(self.frame, font="Helvetica 8 italic", width=11, justify=RIGHT, relief=FLAT)
        self.entryForSex.insert(0, "Sex: ")
        self.entryForSex.configure(state=DISABLED, disabledbackground="#FFFFFF",
                                 disabledforeground="#000000")
        self.sex = Entry(self.frame, font="Helvetica 8", width=35, relief=SOLID)
        self.entryForSex.grid(row=4, column=0)
        self.sex.grid(row=4, column=1)
        
        self.sex.insert(0, " Male")
        self.sex.configure(state=DISABLED, disabledbackground="#FFFFFF")
        self.onClickSex = self.sex.bind("<Button-1>", self.click)
        
        self.entryForCourse = Entry(self.frame, font="Helvetica 8 italic", width=11, justify=RIGHT, relief=FLAT)
        self.entryForCourse.insert(0, "Course: ")
        self.entryForCourse.configure(state=DISABLED, disabledbackground="#FFFFFF",
                                 disabledforeground="#000000")
        self.course = Entry(self.frame, font="Helvetica 8", width=35, relief=SOLID)
        self.entryForCourse.grid(row=5, column=0, pady=5)
        self.course.grid(row=5, column=1, pady=5)
        
        self.course.insert(0, " BSBA")
        self.course.configure(state=DISABLED, disabledbackground="#FFFFFF")
        self.onClickCourse = self.course.bind("<Button-1>", self.click)
        
        self.entryForYearLevel = Entry(self.frame, font="Helvetica 8 italic", width=11, justify=RIGHT, relief=FLAT)
        self.entryForYearLevel.insert(0, "Year Level: ")
        self.entryForYearLevel.configure(state=DISABLED, disabledbackground="#FFFFFF",
                                 disabledforeground="#000000")
        self.yearLevel = Entry(self.frame, font="Helvetica 8", width=35, relief=SOLID)
        self.entryForYearLevel.grid(row=6, column=0)
        self.yearLevel.grid(row=6, column=1)
        
        self.yearLevel.insert(0, " Second Year")
        self.yearLevel.configure(state=DISABLED, disabledbackground="#FFFFFF")
        self.onClickYearLevel = self.yearLevel.bind("<Button-1>", self.click)
        
        self.frameForAddButton = LabelFrame(self.frame, bg="#FFFFFF", relief=FLAT)
        self.frameForAddButton.grid(row=7, column=0, columnspan=2)
        self.addButton = Button(self.frameForAddButton, text="+  Add",  \
                            font="Helvetica 8 bold", foreground="#FFFFFF", activeforeground="#FFFFFF", \
                            command=self.add, bg="#F2994A", activebackground="#F2994A", width=20, relief=FLAT)
        self.addButton.pack(pady=(20, 0))
        
        self.frameForDisplayButton = LabelFrame(self.frame, bg="#FFFFFF", relief=FLAT)
        self.frameForDisplayButton.grid(row=8, column=0, columnspan=2)
        self.displayButton = Button(self.frameForDisplayButton, text="Display", \
                            font="Helvetica 8 bold", foreground="#FFFFFF", activeforeground="#FFFFFF", \
                            command=self.display, bg="#56CCF2", activebackground="#56CCF2", width=20, relief=FLAT)
        self.displayButton.pack(pady=5)

    def add(self):
        self.added = False
        self.inputs = [self.id.get() == "", self.name.get() == "", self.sex.get() == "",
                    self.course.get() == "", self.yearLevel.get() == ""]
        
        self.list = [self.id, self.name, self.course, self.yearLevel]
        self.states = [attribute["state"] == DISABLED for attribute in self.list]
        
        if self.id.get() in self.IDs:
            messagebox.showerror("Information", "ID already exists.")
        
        elif all(self.inputs) or any(self.inputs) or all(self.states) or any(self.states): 
            messagebox.showerror("Information", "All Fields are required.")
            
        else:
            with open(self.file, "a") as csvFile:
                attributes = ["id", "name", "sex", "course", "yearLevel"]
                writer = csv.DictWriter(csvFile, fieldnames=attributes)
                writer.writerow({
                    "id" : self.id.get() ,
                    "name" : self.name.get(),
                    "sex" : self.sex.get(),
                    "course" : self.course.get(),
                    "yearLevel" : self.yearLevel.get()         
                })
            self.load()
            self.added = True
            messagebox.showinfo("Information", "Added Successfully.")
        
        if self.added:
            self.frame.destroy()
            self.frame = LabelFrame(self.parent, padx=10, pady=10, bg="#FFFFFF", relief=FLAT)
            Management.__init__(self, self.file, self.parent)
            
    def load(self):
        with open(self.file, "r") as csvFile:
            reader = csv.DictReader(csvFile)
            for student in reader:
                self.data.append((student["id"], student))
                self.IDs.append(student["id"])
            
    def click(self, event):
        self.list = [self.id, self.name, self.sex, self.course, self.yearLevel]
        self.on_clicks = [self.onClickID, self.onClickName , self.onClickSex, \
                          self.onClickCourse, self.onClickYearLevel]
        self.index = 0
        for attribute in self.list:
          if attribute is event.widget:
            attribute.configure(state=NORMAL)
            attribute.unbind('<Button-1>', self.on_clicks[self.index])
            attribute.delete(0, END)
          self.index += 1
    
    def display(self):
        self.window = Toplevel()
        self.window.geometry("900x600")
        self.window.configure(bg="#FFFFFF")
        self.window.title("Student Records")
        self.window.resizable(False, False)
        self.show()
        
    def show(self):
        self.school = LabelFrame(self.window, bg="#FFFFFF", relief=FLAT)
        self.school.pack(pady=(0, 20))
        Label(self.school, image=self.newSchool, bg="#FFFFFF").pack()
        self.Frame = LabelFrame(self.window, bg="#FFFFFF", relief=FLAT)
        self.Frame.pack()
        self.new = LabelFrame(self.window, bg="#FFFFFF", relief=FLAT)
        self.new.pack()
        self.dropdown = LabelFrame(self.window, bg="#FFFFFF", relief=FLAT)
        self.dropdown.pack(anchor=W, padx=135)
        self.read = LabelFrame(self.window, bg="#FFFFFF", relief=FLAT)
        self.read.pack(anchor=W, padx=260)
        
        self.attributes = ["Picture", "ID Number", "Full Name", "Sex", "Course", "Year Level", "Actions"]
        for i in range(1):
            for j in range(7):
                self.entry = Entry(self.Frame, font="Helvetica 8 bold", justify=CENTER, relief=FLAT)
                self.entry.insert(0, self.attributes[j])
                self.entry.configure(state=DISABLED, disabledbackground="#56CCF2", \
                                     disabledforeground="#FFFFFF")
                self.entry.grid(row=i, column=j, ipady=2)
            
        self.students = [[data for data in student[1].values()] for student in self.data]
        for i in range(len(self.students)):
            self.color = "#FFFFFF"
            if i % 2 == 0:
                self.color = "#F2F2F2"
            for j in range(5):
                self.foreground = "#000000"
                if j == 0:
                    self.foreground = "#F2994A"
                    self.picture = LabelFrame(self.new, bg=self.color, relief=FLAT)
                    self.picture.grid(row=i, column=0)
                    if self.students[i][2] == "Male":
                        Label(self.picture, image=self.newMale, bg=self.color).pack(padx=33)
                    else:
                        Label(self.picture, image=self.newFemale, bg=self.color).pack(padx=33) 
                self.entry = Entry(self.new, justify=CENTER, font="Helvetica 8", relief=FLAT)
                self.entry.insert(0, self.students[i][j])
                self.entry.configure(state=DISABLED, disabledbackground=self.color, \
                                     disabledforeground=self.foreground)
                self.entry.grid(row=i, column=j + 1, ipady=20)
        
        self.counter = 0
        for i in range(len(self.students)):
            self.actions = LabelFrame(self.new, bg="#FFFFFF", relief=FLAT)
            self.actions.grid(row=i, column=8)
            
            self.updateButton = Button(self.actions, text="Update", \
                                command=(lambda ID=self.IDs[self.counter]: self.update(ID)), \
                                font="Helvetica 8 bold", foreground="#FFFFFF", activeforeground="#FFFFFF", \
                                bg="#27AE60", activebackground="#27AE60", relief=FLAT)
            
            self.updateButton.pack(side=LEFT, padx=6)
            self.deleteButton = Button(self.actions, text="Delete", \
                                command=(lambda ID=self.IDs[self.counter]: self.delete(ID)), \
                                font="Helvetica 8 bold", foreground="#FFFFFF", activeforeground="#FFFFFF", \
                                bg="#EB5757", activebackground="#EB5757", relief=FLAT)
            self.deleteButton.pack(side=LEFT, padx=6)
            self.counter += 1
            
        self.options = ["ID Number", "Name", "Sex", "Course", "Year Level"]
        self.hold = StringVar()
        self.hold.set("Read by")
        self.optionMenu = OptionMenu(self.dropdown, self.hold, *self.options)
        self.optionMenu.configure(width=14, highlightbackground="#FFFFFF", font="Helvetica 8 bold", \
                                  foreground="#FFFFFF", activeforeground="#FFFFFF", bg="#56CCF2", \
                                  activebackground="#56CCF2", relief=FLAT)
    
        self.optionMenu.pack(pady=(20, 0), anchor=E)
        self.hold.trace('w', self.present)
        
    def present(self, *args):
        self.read.destroy()
        self.read = LabelFrame(self.window, bg="#FFFFFF", relief=FLAT)
        self.read.pack(anchor=W, padx=260)
        
        self.pairs = {
            "ID Number" : "id",
            "Name" : "name",
            "Sex" : "sex",
            "Course" : "course",
            "Year Level" : "yearLevel"   
        }
        
        self.index = 1
        self.row = [student[1][self.pairs[self.hold.get()]] for student in self.data]
        for row in self.row:
            color = "#FFFFFF"
            if self.index % 2 == 0:
                color = "#F2F2F2"
            self.box = Entry(self.read, width=21, font="Helvetica 8", justify=CENTER, relief=FLAT)
            self.box.insert(0, row)
            self.box.configure(state=DISABLED, disabledbackground=color, disabledforeground="#F2994A")
            self.box.pack()
            self.index += 1

    def delete(self, ID):
        self.response = messagebox.askyesno("Information", \
                        "Deleted entries are not retrievable. Do you wish to continue?", parent=self.window)
        if self.response:
            self.position = self.IDs.index(ID)
            print(self.position)
            del(self.data[self.position])
            del(self.IDs[self.position])
            
            self.save()
            self.reload()
    
    def reload(self):
        self.frame.destroy()
        self.frame = LabelFrame(self.parent, padx=10, pady=10, bg="#FFFFFF", relief=FLAT)
        Management.__init__(self, self.file, self.parent)
        self.window.destroy()
        self.Frame.destroy()
        self.new.destroy()
        self.display()
        
    def save(self):
        with open(self.file, "w") as csvFile:
            attributes = ["id", "name", "sex", "course", "yearLevel"]
            writer = csv.DictWriter(csvFile, fieldnames=attributes)
            writer.writeheader()
            for w, student in self.data:
                writer.writerow(student)   
        self.load()   
        
    def update(self, ID):
        self.updationWindow = Toplevel()
        self.updationWindow.geometry("330x350")
        self.updationWindow.title("Student Records Updation")
        self.updationWindow.configure(bg="#56CCF2")
        self.updationWindow.resizable(False, False)
        
        self.position = self.IDs.index(ID)
        self.student = self.data[self.position][1]
        
        self.university = Image.open("university.png")
        self.resizedUniversity = self.university.resize((60, 60), Image.ANTIALIAS)
        self.newUniversity = ImageTk.PhotoImage(self.resizedUniversity)
        
        self.newFrame = LabelFrame(self.updationWindow, padx=10, pady=10, bg="#FFFFFF", relief=FLAT)
        self.newFrame.pack(pady=20)
        
        self.frameForPictureNew = LabelFrame(self.newFrame, bg="#FFFFFF", relief=FLAT)
        self.frameForPictureNew.grid(row=0, column=0, rowspan=2, columnspan=2, pady=(0, 20))
        
        Label(self.frameForPictureNew, image=self.newUniversity, bg="#FFFFFF").pack()
        
        self.newEntryForID = Entry(self.newFrame, font="Helvetica 8 italic", width=11, justify=RIGHT, relief=FLAT)
        self.newEntryForID.insert(0, "ID Number: ")
        self.newEntryForID.configure(state=DISABLED, disabledbackground="#FFFFFF",
                                 disabledforeground="#000000")
        self.newId = Entry(self.newFrame, font="Helvetica 8", width=35, foreground="#F2994A", relief=SOLID)
        self.newEntryForID.grid(row=2, column=0)
        self.newId.grid(row=2, column=1)
        
        self.newId.insert(0, "{}".format(self.student["id"]))
        
        self.newEntryForName = Entry(self.newFrame, font="Helvetica 8 italic", width=11, justify=RIGHT, relief=FLAT)
        self.newEntryForName.insert(0, "Name: ")
        self.newEntryForName.configure(state=DISABLED, disabledbackground="#FFFFFF",
                                 disabledforeground="#000000")
        self.newName = Entry(self.newFrame, font="Helvetica 8", width=35, foreground="#F2994A", relief=SOLID)
        self.newEntryForName.grid(row=3, column=0, pady=5)
        self.newName.grid(row=3, column=1, pady=5)
        
        self.newName.insert(0, "{}".format(self.student["name"]))
        
        self.newEntryForSex = Entry(self.newFrame, font="Helvetica 8 italic",width=11, justify=RIGHT, relief=FLAT)
        self.newEntryForSex.insert(0, "Sex: ")
        self.newEntryForSex.configure(state=DISABLED, disabledbackground="#FFFFFF",
                                 disabledforeground="#000000")
        self.newSex = Entry(self.newFrame, font="Helvetica 8", width=35, foreground="#F2994A", relief=SOLID)
        self.newEntryForSex.grid(row=4, column=0)
        self.newSex.grid(row=4, column=1)
        
        self.newSex.insert(0, "{}".format(self.student["sex"]))
        
        self.newEntryForCourse = Entry(self.newFrame, font="Helvetica 8 italic", width=11, justify=RIGHT, relief=FLAT)
        self.newEntryForCourse.insert(0, "Course: ")
        self.newEntryForCourse.configure(state=DISABLED, disabledbackground="#FFFFFF",
                                 disabledforeground="#000000")
        self.newCourse = Entry(self.newFrame, font="Helvetica 8", width=35, foreground="#F2994A", relief=SOLID)
        self.newEntryForCourse.grid(row=5, column=0, pady=5)
        self.newCourse.grid(row=5, column=1, pady=5)
        
        self.newCourse.insert(0, "{}".format(self.student["course"]))
        
        self.newEntryForYearLevel = Entry(self.newFrame, font="Helvetica 8 italic", width=11, \
                                          justify=RIGHT, relief=FLAT)
        self.newEntryForYearLevel.insert(0, "Year Level: ")
        self.newEntryForYearLevel.configure(state=DISABLED, disabledbackground="#FFFFFF",
                                 disabledforeground="#000000")
        self.newYearLevel = Entry(self.newFrame, font="Helvetica 8", width=35, foreground="#F2994A", relief=SOLID)
        self.newEntryForYearLevel.grid(row=6, column=0)
        self.newYearLevel.grid(row=6, column=1)
        
        self.newYearLevel.insert(0, "{}".format(self.student["yearLevel"]))
        
        self.newFrameForAddButton = LabelFrame(self.newFrame, bg="#FFFFFF", relief=FLAT)
        self.newFrameForAddButton.grid(row=7, column=0, columnspan=2)
        self.newAddButton = Button(self.newFrameForAddButton, text="Update", \
                            font="Helvetica 8 bold", foreground="#FFFFFF", activeforeground="#FFFFFF", \
                            command=self.submit, bg="#F2994A", activebackground="#F2994A", width=20, relief=FLAT)
        self.newAddButton.pack(pady=(20, 0))
        
        self.newFrameForDisplayButton = LabelFrame(self.newFrame, bg="#FFFFFF", relief=FLAT)
        self.newFrameForDisplayButton.grid(row=8, column=0, columnspan=2)
        self.newDisplayButton = Button(self.newFrameForDisplayButton, text="Clear", \
                            font="Helvetica 8 bold", foreground="#FFFFFF", activeforeground="#FFFFFF", \
                            command=self.clear, bg="#56CCF2", activebackground="#56CCF2", width=20, relief=FLAT)
        self.newDisplayButton.pack(pady=5)
    
    def clear(self):
        self.newId.delete(0, END)
        self.newName.delete(0, END)
        self.newSex.delete(0, END)
        self.newCourse.delete(0, END)
        self.newYearLevel.delete(0, END)

    def submit(self):
        self.data[self.position][1]["id"] = self.newId.get()
        self.data[self.position][1]["name"] = self.newName.get()
        self.data[self.position][1]["sex"] = self.newSex.get()
        self.data[self.position][1]["course"] = self.newCourse.get()
        self.data[self.position][1]["yearLevel"] = self.newYearLevel.get()
        self.save()
        messagebox.showinfo("Information", "Update Completed.", parent=self.updationWindow)
        
        self.updationWindow.destroy()
        self.reload()
   
if __name__ == "__main__":
    root = Tk()
    file = Management("data.csv", root)
    root.mainloop()