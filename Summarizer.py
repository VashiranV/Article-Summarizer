
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


#def location():
    #folderName = fd.asksaveasfilename()
    #if(len(folderName)>0):
       # locationError.config(text=folderName,fg="green")
   # else:
       # locationError.config(text="Invalid Directory",fg="red")

def downloadVid():
    
    URL = entry.get()
    

    article = Article(URL)

    article.download()
    article.parse()
    nltk.download("punkt")
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


#save = Button(window, width=10,bg="purple",fg="white", text="Choose Path",command=location)
#save.grid()



download = Button(window, width=10,bg="purple",fg="white", text="Summarize",command=downloadVid)
download.grid(pady=5)


window.mainloop()