# Implement a GUI-based Scrabbler Helper
from tkinter import *
from Scrabbler import Scrabbler


# Start by creating a class that inherits from Frame
class Application(Frame):
    def __init__(self, rootWindow, scrabbler):
        super().__init__(rootWindow)
        self.grid()

        # Make an Entry for users to type their tiles
        self.__entry = Entry(self)
        self.__entry.insert(0, "Type your tiles.")
        self.__entry.config(fg='grey')
        self.__entry.bind("<Button-1>", self.OnMouseDown)
        self.__entry.bind("<FocusOut>", self.OnMouseUp)
        self.__entry.grid()

        # Make an Label to tell users to choose an option
        self.__label = Label(self, text="Choose an option:")
        self.__label.grid(row=1, sticky=W)

        # A list of Radiobuttons that provide the options for users
        self.__option = IntVar()
        self.__option1 = Radiobutton(self, text="show the word with the most points", variable=self.__option, value=1)
        self.__option2 = Radiobutton(self, text="show all possible words", variable=self.__option, value=2)
        self.__option3 = Radiobutton(self, text="show all anagrams", variable=self.__option, value=3)
        self.__option4 = Radiobutton(self, text="show List all words that start with a Q but are not followed by a u", variable=self.__option, value=4)
        self.__option5 = Radiobutton(self, text="show all 2-letter words", variable=self.__option, value=5)
        self.__option6 = Radiobutton(self, text="show all the 3-letter words containing that given input tile", variable=self.__option, value=6)
        self.__option7 = Radiobutton(self, text="Word verifier", variable=self.__option, value=7)
        self.__option8 = Radiobutton(self, text="Show all words that end with that group of letters.", variable=self.__option, value=8)
        self.__option9 = Radiobutton(self, text="show all words that begin with that group of letters", variable=self.__option, value=9)
        self.__option10 = Radiobutton(self, text="show all words containing the letters “X” or “Z” and the input tile", variable=self.__option, value=10)

        self.__option1.grid(row=2, sticky=W)
        self.__option2.grid(row=3, sticky=W)
        self.__option3.grid(row=4, sticky=W)
        self.__option4.grid(row=5, sticky=W)
        self.__option5.grid(row=6, sticky=W)
        self.__option6.grid(row=7, sticky=W)
        self.__option7.grid(row=8, sticky=W)
        self.__option8.grid(row=9, sticky=W)
        self.__option9.grid(row=10, sticky=W)
        self.__option10.grid(row=11, sticky=W)

        # Make a Button so that users can click to see the answers
        self.__button = Button(self, text="See the answers", command=lambda: self.controller(scrabbler))
        self.__button.grid(row=12, sticky=W)
        
        # Make a Large Text field for users to see the answers
        self.__text = Text(self, width=50, height=80)
        self.__text.config(state="disabled")
        self.__text.grid(row=13)

        # Make a scrollbar so that users can scroll to see the answers
        self.scrollbar = Scrollbar(self.__text, orient="vertical")
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.listbox = Listbox(self.__text, width=50, height=10, yscrollcommand=self.scrollbar.set)
        self.listbox.pack(side=LEFT, fill=BOTH)
        self.scrollbar.config(command=self.listbox.yview)

    # when users choose different options by selecting the radiobutton and clicking the button,
    # the button leads to different functions from Scrabbler and perform different tasks
    def controller(self, scrabbler):
        tiles = self.__entry.get()
        answerList = []
        valueList = []

        if self.__option.get() == 1:
            answerList,valueList = scrabbler.mostPoints(tiles)
            for i in range(len(answerList)):
                self.__text.config(state="normal")
                self.listbox.insert(END, answerList[i] + ": " + str(valueList[i]) + "\n")
                self.__text.config(state="disabled")
        elif self.__option.get() == 2:
            answerList, valueList = scrabbler.allResults(tiles)
            for i in range(len(answerList)):
                self.__text.config(state="normal")
                self.listbox.insert(END, answerList[i]+": "+str(valueList[i])+"\n")
                self.__text.config(state="disabled")
        elif self.__option.get() == 3:
            answerList, valueList = scrabbler.anagrams(tiles)
            for i in range(len(answerList)):
                self.__text.config(state="normal")
                self.listbox.insert(END, answerList[i] + ": " + str(valueList[i]) + "\n")
                self.__text.config(state="disabled")
        elif self.__option.get() ==4:
            answerList, valueList = scrabbler.qWithoutU()
            for i in range(len(answerList)):
                self.__text.config(state="normal")
                self.listbox.insert(END, answerList[i] + ": " + str(valueList[i]) + "\n")
                self.__text.config(state="disabled")
        elif self.__option.get() == 5:
            answerList, valueList = scrabbler.twoLetter()
            for i in range(len(answerList)):
                self.__text.config(state="normal")
                self.listbox.insert(END, answerList[i] + ": " + str(valueList[i]) + "\n")
                self.__text.config(state="disabled")
        elif self.__option.get() == 6:
            answerList, valueList = scrabbler.threeLetter(tiles)
            for i in range(len(answerList)):
                self.__text.config(state="normal")
                self.listbox.insert(END, answerList[i] + ": " + str(valueList[i]) + "\n")
                self.__text.config(state="disabled")
        elif self.__option.get() == 7:
            answer = scrabbler.verifier(tiles)
            self.__text.config(state="normal")
            self.listbox.insert(END, answer+"\n")
            self.__text.config(state="disabled")
        elif self.__option.get() == 8:
            answerList, valueList = scrabbler.ending(tiles)
            for i in range(len(answerList)):
                self.__text.config(state="normal")
                self.listbox.insert(END, answerList[i] + ": " + str(valueList[i]) + "\n")
                self.__text.config(state="disabled")
        elif self.__option.get() == 9:
            answerList, valueList = scrabbler.beginning(tiles)
            for i in range(len(answerList)):
                self.__text.config(state="normal")
                self.listbox.insert(END, answerList[i] + ": " + str(valueList[i]) + "\n")
                self.__text.config(state="disabled")
        elif self.__option.get() == 10:
            answerList, valueList = scrabbler.xorz(tiles)
            for i in range(len(answerList)):
                self.__text.config(state="normal")
                self.listbox.insert(END, answerList[i] + ": " + str(valueList[i]) + "\n")
                self.__text.config(state="disabled")

    # special features add to Entry
    def OnMouseDown(self, event):
        if self.__entry.get() == "Type your tiles.":
            self.__entry.delete(0, END)
            self.__entry.icursor(0)
            self.__entry.focus_set()
            self.__entry.config(fg='black')

    def OnMouseUp(self, event):
        if len(self.__entry.get()) == 0:
            self.__entry.insert(0, "Type your tiles.")
            self.__entry.config(fg='grey')


def main():
    root = Tk()
    root.title("Scrabble Helper")
    root.geometry("900x600")
    scrabbler = Scrabbler()
    Application(root, scrabbler)
    root.mainloop()


main()
