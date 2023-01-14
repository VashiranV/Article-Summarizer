
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd

import nltk
from newspaper import Article

folderName = ""

window = Tk()
window.title("Article Summarizer")
window.geometry("500x125")


window.columnconfigure(0,weight=1)

def downloadText():
    
    URL = entry.get()
    

    article = Article(URL)

    article.download()
    article.parse()
    article.nlp()
    
    fileName = fd.asksaveasfilename()
    f= open(fileName+".txt","w+")
    f.write(article.summary)
    f.close
    

label = Label(window,text="Article Summarizer",font=("jost",15))
label.grid(pady=5)

entry = StringVar()
entry = Entry(window, width=50,textvariable=entry)
entry.grid(pady=5)



download = Button(window, width=10,bg="purple",fg="white", text="Summarize",command=downloadText)
download.grid(pady=5)


window.mainloop()
