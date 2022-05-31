import csv
import os

class DataFile:
    def __init__(self, name, path, header):  
        self.file_name = name+ ".csv"
        self.path = path
        with open(os.path.join(self.path,self.file_name), 'w', encoding='UTF8', newline='') as f:      
            writer = csv.writer(f)
            writer.writerow(header)
            f.close()

    def saveData(self,data):
        with open(os.path.join(self.path,self.file_name), 'a', encoding='UTF8', newline='') as f:      
            writer = csv.writer(f)
            writer.writerow(data)
            f.close()
