from tkinter import *
import tkinter.messagebox as msgbox

class Login():
    FILE_NAME = 'Member.txt'
    member={}
    cnt = 0

    def __init__(self, window):
        self.window = window
        self.readFile()
        self.initUi()

    def initUi(self):
        self.winLogin = Toplevel(self.window)
        self.winLogin.title("로그인")

        lblId=Label(self.winLogin, text="아이디")
        lblId.grid(row=0,column=0,padx=5, pady=10)

        self.txtboxId=Entry(self.winLogin)
        self.txtboxId.grid(row=0,column=1,padx=5)

        lblPw=Label(self.winLogin, text="비밀번호")
        lblPw.grid(row=1,column=0,padx=5, pady=10)

        self.txtboxPw=Entry(self.winLogin, show="*")
        self.txtboxPw.grid(row=1,column=1,padx=5)

        btnLogin = Button(self.winLogin, text = "로그인", command=lambda:self.onLogin())
        btnLogin.grid(row=0,column=2, rowspan=2, padx=5, pady=10)

        self.winLogin.mainloop()

    def readFile(self):
        try:
            f = open(Login.FILE_NAME, 'r', encoding='utf-8')
        except FileNotFoundError as e:
                print(e)
                f = open(Login.FILE_NAME, 'w', encoding='utf-8')
                f.close()
        else:
            while True:
                line = f.readline()
                if not line:
                    break
 
                line = line.replace('\n', '')
                id, pw = line.split(' ')
                self.member[id] = pw
            f.close()
 
    def onLogin(self):
        self.id = self.txtboxId.get()
        pw = self.txtboxPw.get()
 
        if self.id and pw:
            bFind = False
            for _id in self.member.keys():
                _pw = self.member.get(_id)
                if self.id == _id and pw == _pw:
                    bFind = True
                    break
 
            if bFind:
                msgbox.showinfo("환영합니다!", "로그인 성공")
                self.winLogin.quit()
                self.winLogin.destroy()
            else:
                self.cnt += 1
                txt = f'로그인 {self.cnt}회 실패'
                msgbox.showwarning("ID 또는 PW가 맞지 않습니다!", txt)
                if self.cnt>=3:
                    msgbox.showerror("로그인 실패", "3회 이상 오류")
                    self.winLogin.quit()
                    self.winLogin.destroy()
    
    def getId(self): return self.id




