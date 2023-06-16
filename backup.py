class Backup:
    FILE_NAME = "Backup.txt"
    
    def Load(self, id):
        try:
            f = open(Backup.FILE_NAME, 'r', encoding='utf-8')
        except FileNotFoundError as e:
            print(e)
            f = open(Backup.FILE_NAME, 'w', encoding='utf-8')
            f.close()
        else:
            lines = f.readlines()
            for line in lines:
                savedData = line.split(" ", 1)
                savedId = savedData[0]
                if savedId == id:
                    savedText = savedData[1]
                    f.close()
                    return savedText
 
    def Save(self, id, text):
        with open(Backup.FILE_NAME, 'r') as f:
            lines = f.readlines()
        with open(Backup.FILE_NAME, 'w', encoding='utf-8') as f:
            for line in lines:
                if line.split(" ", 1)[0] != id:     # <= 이 문자열만 골라서 삭제
                    f.write(line)
            data = f'{id} {text[:-1]}\n'
            f.write(data)
            f.close()