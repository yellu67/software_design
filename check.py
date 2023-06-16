from hanspell import spell_checker

class Check:
    def __init__(self,text):
        self.text = text
        self.check()

    def check(self):
        self.result = ""
        for i in range(0, 50):
            globals()['sent{}'.format(i)] = self.text[500*i:500*i+499]
            
            spelledSent = spell_checker.check(globals()['sent{}'.format(i)])
            checkedSent = spelledSent.checked
            self.result += checkedSent

    def putResult(self):
        return self.result

    
        










