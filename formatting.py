from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont


class Formatting():

    def __init__(self, window, txtbox1, txtbox2, ckbtnValue0, ckbtnValue1, ckbtnValue2,ckbtnValue3):
        self.window = window
        self.txtbox1 = txtbox1
        self.txtbox2 = txtbox2
        self.ckbtnBoldValue = ckbtnValue0
        self.ckbtnItalicValue = ckbtnValue1
        self.ckbtnTxtbox1Value = ckbtnValue2
        self.ckbtnTxtbox2Value = ckbtnValue3
        self.initUi()

    def initUi(self):
        self.winFormat = Toplevel(self.window)

        self.winFormat.title("서식 지정")

        lblFont=Label(self.winFormat, text="글꼴 모양")
        lblFont.grid(row=0,column=0,padx=5, pady=10)

        self.cmbboxFont=ttk.Combobox(self.winFormat, values=list(tkFont.families()))
        self.cmbboxFont.grid(row=0,column=1, columnspan=4 ,padx=5)

        lblFontsize=Label(self.winFormat, text="글꼴 크기")
        lblFontsize.grid(row=1,column=0,padx=5, pady=10)

        self.txtboxFontsize=Entry(self.winFormat)
        self.txtboxFontsize.grid(row=1,column=1, columnspan=4 ,padx=5)

        lblFontstyle=Label(self.winFormat, text="글꼴 스타일")
        lblFontstyle.grid(row=2,column=0,padx=5, pady=10)

        self.ckbtnBold=Checkbutton(self.winFormat, text="굵게", variable=self.ckbtnBoldValue)
        self.ckbtnBold.grid(row=2,column=1, columnspan=2 ,padx=5)

        self.ckbtnItalic=Checkbutton(self.winFormat, text="기울임", variable=self.ckbtnItalicValue)
        self.ckbtnItalic.grid(row=2,column=3, columnspan=1 ,padx=5)

        lblTxtbox=Label(self.winFormat, text="적용할 텍스트 상자")
        lblTxtbox.grid(row=3,column=0,padx=5, pady=10)

        self.ckbtnTxtbox1=Checkbutton(self.winFormat, text="변경 전", variable=self.ckbtnTxtbox1Value)
        self.ckbtnTxtbox1.grid(row=3,column=1, columnspan=2, padx=5, pady=10)

        self.ckbtnTxtbox2=Checkbutton(self.winFormat, text="변경 후", variable=self.ckbtnTxtbox2Value)
        self.ckbtnTxtbox2.grid(row=3,column=3, columnspan=2, padx=5, pady=10)

        btnFormat = Button(self.winFormat, text = "적용", command=lambda:self.setFormat())
        btnFormat.grid(row=4,column=0, columnspan=5, padx=5, pady=10)

        self.winFormat.mainloop()

    def setFormat(self):
        if self.ckbtnBoldValue.get() == 1:
            bold = "bold"
        else:
            bold = "normal"

        if self.ckbtnItalicValue.get() == 1:
            italic = "italic"
        else:
            italic = "roman"

        if self.ckbtnTxtbox1Value.get() == 1:
            self.txtbox1.configure(font=tkFont.Font(family=self.cmbboxFont.get(), size=(int)(self.txtboxFontsize.get()), weight=bold, slant=italic))

        if self.ckbtnTxtbox2Value.get() == 1:
            self.txtbox2.configure(font=tkFont.Font(family=self.cmbboxFont.get(), size=(int)(self.txtboxFontsize.get()), weight=bold, slant=italic))