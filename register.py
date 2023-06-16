from tkinter import *
import tkinter.messagebox as msgbox

class Register:
    FILE_NAME = 'Member.txt' 
    member = []
    
    def __init__(self,window):
        self.window = window
        self.readFile()
        self.initUi()

    def initUi(self):
        self.winRegister = Toplevel(self.window) # GUI 생성
        self.winRegister.title("회원가입")

        lblId=Label(self.winRegister, text="아이디")
        lblId.grid(row=0,column=0,padx=5, pady=10)

        self.txtboxId=Entry(self.winRegister)
        self.txtboxId.grid(row=0,column=1,padx=5)

        lblPw=Label(self.winRegister, text="비밀번호")
        lblPw.grid(row=1,column=0,padx=5, pady=10)

        self.txtboxPw=Entry(self.winRegister, show="*")
        self.txtboxPw.grid(row=1,column=1,padx=5)

        btnRegister = Button(self.winRegister, text = "회원가입", command=lambda:self.onRegister())
        btnRegister.grid(row=2,column=0, columnspan= 2, padx=5, pady=10)

        self.winRegister.mainloop()

    def readFile(self):
        try:
            f = open(Register.FILE_NAME, 'r', encoding='utf-8')
        except FileNotFoundError as e:
            print(e)
            f = open(Register.FILE_NAME, 'w', encoding='utf-8')
            f.close()

        else:
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.replace('\n', '')
                id, pw = line.split(' ')
                self.member.append(id)
            f.close()
 
    def writeFile(self, id, pw):
        with open(Register.FILE_NAME, 'a', encoding='utf-8') as f:
            member = f'{id} {pw}\n'
            f.write(member)
 
    def onRegister(self):
        id = self.txtboxId.get()
        pw = self.txtboxPw.get()

        
        if id == "guest":
            msgbox.showwarning("아이디 오류", "다른 아이디를 입력하세요.")
        elif id and pw and not self.findIDs(id):
            self.writeFile(id,pw)
            msgbox.showinfo("회원가입 완료", "회원가입되었습니다.")
            self.winRegister.destroy()
        else:
            msgbox.showerror("아이디 오류", "아이디가 중복입니다.")
        
    
    def findIDs(self, id):
        bOverlap = False
        for _id in self.member:
            if id==_id:
                bOverlap = True
                break
        return bOverlap
    