from tkinter import *
from tkinter import ttk
from method import MyTranslator

app = Tk()
app.geometry('350x520')
app.title('Google Translator')
app.resizable(0,0)
app.config(bg='blue')
app.wm_iconbitmap('icon.ico')

def get():
    s = srcLangs.get()
    d = destLangs.get()
    message = sourceText.get(1.0,END)
    translator = MyTranslator()
    text = translator.run(txt=message, src=s, dest=d)
    destText.delete(1.0,END)
    destText.insert(END,text)

appName = Label(app,text ='Google Translator',font =('arial',20),bg='green',fg='goldenrod1',height=2)
appName.pack(side=TOP,fill=BOTH,pady=0)
version = Label(app, text='2.0',font=('algerian',13),bg='green').place(x=250,y=45)

frame = Frame(app).pack(side=BOTTOM)
sourceText = Text(frame,font=('arial',10),height=11,wrap=WORD)
sourceText.pack(side=TOP,padx=5,pady=5)

transbtn = Button(frame,text='Translate',font=('arial',13,'bold'),fg='red',bg='blue',activebackground='green',
                  relief=GROOVE,command=get)
transbtn.pack(side=TOP,pady=15)

langs = MyTranslator().langs

srcLangs = ttk.Combobox(frame,values=langs,width=10)
srcLangs.place(x=30,y=280)
srcLangs.set('english')

destLangs = ttk.Combobox(frame,values=langs,width=10)
destLangs.place(x=240,y=280)
destLangs.set('hindi')

destText = Text(frame,font=('arial',10),height=11,wrap=WORD)
destText.pack(side=TOP,padx=5,pady=5)


app.mainloop()

