from tkinter import*
from tkinter import ttk # stylish
from PIL import Image,ImageTk # for images # pip install pillow




class Chatbot:
    def __init__(self,root):
        self.root=root
        self.root.title("Chatbot")
        self.root.geometry("730x620+0+0")
        self.root.bind('<Return>',self.enter_fun)

        main_frame= Frame(self.root,bd=4,bg="darkblue",width=610)
        main_frame.pack()

        img_chat =Image.open('chat.jpg') # it is in this folder only 
        img_chat=img_chat.resize((200,70),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img_chat)

        title_label = Label(main_frame,bd=3,relief=RAISED,anchor='nw',width=730,compound=LEFT,image=self.photoimg,text="CHAT WITH ME",font=('new time roman',30,'bold'),fg='blue',bg='white')
        title_label.pack(side=TOP)

        self.scroll_y=ttk.Scrollbar(main_frame,orient=VERTICAL)
        self.text = Text(main_frame,width=65,height=20,bd=3,relief=RAISED,font=('arial',14),yscrollcommand=self.scroll_y.set)
        self.scroll_y.pack(side=RIGHT,fill=Y)
        self.text.pack()

        btn_frame=Button(self.root,bd=5,bg="white")
        btn_frame.pack()

        label=Label(btn_frame,text="Type something",font=('times new roman',14,'bold'),fg='blue',bg='white')
        label.grid(row=0,column=0,padx=5,sticky=W)

        self.entry=StringVar()    
        self.entry1=ttk.Entry(btn_frame,textvariable=self.entry,width=40,font=('times new roman',16,'bold'))
        self.entry1.grid(row=0,column=1,padx=5,sticky=W)

        self.send=Button(btn_frame,text="Send",command=self.sended,font=('times new roman',15,'bold'),width=8,bg="blue",)
        self.send.grid(row=0,column=2,padx=5,sticky=W)

        self.clear=Button(btn_frame,text="Clear",command=self.clear,font=('times new roman',15,'bold'),width=8,bg="blue")
        self.clear.grid(row=1,column=0,padx=5,sticky=W)

        self.msg=''
        self.label_1=Label(btn_frame,text=self.msg,font=('times new roman',14,'bold'),fg='blue',bg='white')
        self.label_1.grid(row=1,column=1,padx=5,sticky=W)


#============================ Function declaration ===========================================        
    def enter_fun(self,event):
        self.send.invoke()
        self.entry.set('')

    def clear(self):
        self.text.delete('1.0',END)
        self.entry.set('')

    def sended(self):
        send='\t\t\t' + ' You :' + self.entry.get()
        self.text.insert(END,'\n'+send)
        self.text.yview(END)

        if (self.entry.get()==''):
            self.msg = "Please enter some input"
            self.label_1.config(text=self.msg,fg="red")

        else:
            self.msg=''
            self.label_1.config(text=self.msg,fg="red")

        if self.entry.get() == "Hello":
            self.text.insert(END, '\n\n' + 'Bot: Hey there! How can I assist you today?')

        elif self.entry.get() == "Hi":
            self.text.insert(END, '\n\n' + 'Bot: Hello! How can I help you?')

        elif self.entry.get() == "Good morning":
            self.text.insert(END, '\n\n' + 'Bot: Good morning! How can I assist you today?')

        elif self.entry.get() == "Good evening":
            self.text.insert(END, '\n\n' + 'Bot: Good evening! How can I help you?')

        elif self.entry.get() == "How are you?":
            self.text.insert(END, '\n\n' + 'Bot: I am just a bot, but thanks for asking! How can I help you today?')

        elif self.entry.get() == "What is face recognition?":
            self.text.insert(END, '\n\n' + 'Bot: Face recognition is a technology that can identify or verify a person\'s identity using their face. It uses biometric data and compares it to a database of known faces.')

        elif self.entry.get() == "How does face recognition work?":
            self.text.insert(END, '\n\n' + 'Bot: Face recognition works by capturing an image of a face, extracting unique facial features, and comparing them to a database of stored faces to find a match.')

        elif self.entry.get() == "What is the accuracy of face recognition?":
            self.text.insert(END, '\n\n' + 'Bot: The accuracy of face recognition can vary depending on the system and the quality of the data. It can range from 90% to 99% or higher in some cases, though errors can still occur.')

        elif self.entry.get() == "What are the applications of face recognition?":
            self.text.insert(END, '\n\n' + 'Bot: Face recognition is used in various applications like security (e.g., unlocking devices), surveillance, identity verification, and even customer experience enhancement in retail.')

        elif self.entry.get() == "Can face recognition be fooled?":
            self.text.insert(END, '\n\n' + 'Bot: Yes, face recognition systems can be fooled by photos, videos, or 3D models, although many modern systems incorporate advanced algorithms to prevent such spoofing.')

        elif self.entry.get() == "Is face recognition legal?":
            self.text.insert(END, '\n\n' + 'Bot: The legality of face recognition varies by country and jurisdiction. Some places have regulations to protect privacy, while others allow its widespread use, particularly in security applications.')

        elif self.entry.get() == "What are the challenges of face recognition?":
            self.text.insert(END, '\n\n' + 'Bot: Some challenges of face recognition include privacy concerns, the ability to work in various lighting conditions, dealing with occlusions (e.g., glasses, hats), and ensuring accuracy in diverse populations.')

        elif self.entry.get() == "What is your name?":
            self.text.insert(END, '\n\n' + 'Bot: I am a bot created to assist you with face recognition queries.')

        elif self.entry.get() == "Who created you?":
            self.text.insert(END, '\n\n' + 'Bot: I was created by developers working on this face recognition project.')

        elif self.entry.get() == "Tell me a joke":
            self.text.insert(END, '\n\n' + 'Bot: Why don’t skeletons fight each other? They don’t have the guts!')

        elif self.entry.get() == "What is AI?":
            self.text.insert(END, '\n\n' + 'Bot: AI, or Artificial Intelligence, is the simulation of human intelligence in machines that are programmed to think and learn from experience.')

        elif self.entry.get() == "Can you help with coding?":
            self.text.insert(END, '\n\n' + 'Bot: Yes! I can help with coding questions, especially related to face recognition and machine learning. What do you need help with?')

        else:
            self.text.insert(END, '\n\n' + 'Bot: Sorry, I did not understand your question. Can you please ask about face recognition or related topics?')


if __name__ == '__main__':
    root = Tk()
    obj=Chatbot(root)
    root.mainloop()       