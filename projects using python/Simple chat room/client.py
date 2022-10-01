import socket
import threading
import tkinter
from datetime import datetime
from tkinter import Tk, messagebox
import mysql.connector
import tkinter.scrolledtext
from tkinter import simpledialog

mydb = mysql.connector.connect(  # connecting to my database via xamp server
    host="127.0.0.1",
    user="root",
    password="",
    database="chat"
)

mycursor = mydb.cursor()

HOST = "127.0.0.1"
PORT = 9090


def insert_user(msg_from, msg):
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    sql = f"INSERT INTO `chat_system`(`msg_from`, `msg`, `time`) VALUES ('{msg_from}','{msg}','{current_time}')"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")
    return



class Client:
    
    def __init__(self, host, port): # constructor
        
        self.sock =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((host, port))

        msg = tkinter.Tk()
        msg.withdraw() #hides the window without destroying it internally.

        self.nickname = simpledialog.askstring("Nickname", "Please choose a nickname", parent=msg)
        print(self.nickname)

        # initialising flags
        self.gui_done = False
        self.running = True


        gui_thread = threading.Thread(target=self.gui_loop)
        recieve_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        recieve_thread.start()

    
    def gui_loop(self):
        self.win = tkinter.Tk()
        self.win.configure(bg="lightgray")

        self.chat_label = tkinter.Label(self.win, text="CHAT ROOM :- ", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state='disabled') # user must not be able to edit that text in the chat history(texty area) 

        self.msg_label = tkinter.Label(self.win, text="Message: ", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)

        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOWW" ,self.stop)
        self.win.mainloop()

    def write(self):
        input_text = self.input_area.get('1.0','end')
        message = f"{self.nickname}: {input_text}"

        insert_user(self.nickname, input_text)

        self.sock.send(message.encode('utf-8'))
        self.input_area.delete('1.0','end')

    def stop(self):
        self.running = False
        self.win.destroy()
        self.sock.close()
        exit(0)

    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode('utf-8')
                if message == 'NICK':
                    self.sock.send(self.nickname.encode('utf-8'))
                if message == 'Already there':
                    root = Tk()
                    root.geometry("300x200")
                    messagebox.showinfo("showinfo", "Information")
                    root.mainloop()

                else:
                    if self.gui_done:
                        self.text_area.config(state='normal')
                        self.text_area.insert('end', message)
                        self.text_area.yview('end')
                        self.text_area.config(state='disabled')
            except ConnectionAbortedError:
                break
            except:
                print("Error")
                self.sock.close()
                break


#creating instance of client
client = Client(HOST, PORT)




