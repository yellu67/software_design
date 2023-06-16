from login import Login
from register import Register
from check import Check
from backup import Backup
from formatting import Formatting
from tkinter import *
import tkinter.messagebox as msgbox

class Main:
    id = "guest"

    winMain = Tk() # GUI 생성 
    winMain.title("맞춤법 검사기") #상단의 타이틀 지정
    ckbtnValue0 = IntVar()
    ckbtnValue1 = IntVar()
    ckbtnValue2 = IntVar()
    ckbtnValue3 = IntVar()

    def __init__(self):
        self.initUi()
        self.id = "guest"

    def runLogin(self):
        log = Login(self.winMain)
        self.id = log.getId()
    def runRegister(self): Register(self.winMain)
    def runCheck(self):
        chk = Check(self.textbox.get("0.0","end"))
        self.txtboxResult.delete("0.0","end")
        self.txtboxResult.insert(0.0, chk.putResult())

    def runSave(self):
        if self.id == "guest":
            msgbox.showerror("로그인 전용 기능", "로그인해야 이용가능한 기능입니다.")
        else:
            Backup().Save(self.id, self.textbox.get("0.0","end"))
    def runLoad(self):
        if self.id == "guest":
            msgbox.showerror("로그인 전용 기능", "로그인해야 이용가능한 기능입니다.")
        else:
            self.textbox.delete("0.0","end")
            self.textbox.insert(0.0, Backup().Load(self.id))
    def runFormat(self): Formatting(self.winMain, self.textbox, self.txtboxResult, self.ckbtnValue0, self.ckbtnValue1, self.ckbtnValue2, self.ckbtnValue3)

    def initUi(self):
        self.btnLogin = Button(self.winMain, text = "로그인", command=lambda:self.runLogin())
        self.btnLogin.grid(row=0,column=15,padx=5, pady=10)

        self.btnRegister = Button(self.winMain, text = "회원가입", command=lambda:self.runRegister())
        self.btnRegister.grid(row=0,column=16,padx=5, pady=10)

        self.textbox=Text(self.winMain, width=63, height=35)
        self.textbox.grid(row=1,column=0,columnspan=8,padx=7)

        self.btnCheck = Button(self.winMain, text="맞춤법 검사", command=lambda:self.runCheck())
        self.btnCheck.grid(row=1,column=8,padx=5)

        self.txtboxResult=Text(self.winMain, width=63,height=35)
        self.txtboxResult.grid(row=1,column=9,columnspan=8,padx=5)

        self.lblCount=Label(self.winMain, text="글자수")
        self.lblCount.grid(row=2,column=0,padx=5, pady=10)

        self.lblCheckcount=Label(self.winMain, text="글자수")
        self.lblCheckcount.grid(row=2,column=9,padx=5, pady=10)

        self.btnClean = Button(self.winMain, text = "모두 지우기", command=lambda:self.textbox.delete("0.0","end"))
        self.btnClean.grid(row=3,column=0,padx=5, pady=10)

        self.btnSave = Button(self.winMain, text = "저장하기", command=lambda:self.runSave())
        self.btnSave.grid(row=3,column=15,padx=5, pady=10)

        self.btnLoad = Button(self.winMain, text = "불러오기", command=lambda:self.runLoad())
        self.btnLoad.grid(row=3,column=16,padx=5, pady=10)

        self.btnFormat = Button(self.winMain, text = "서식", command=lambda:self.runFormat())
        self.btnFormat.grid(row=0,column=0,padx=5, pady=10)

        self.winMain.mainloop() # GUI가 보이고 종료될때까지 실행함

main=Main()
