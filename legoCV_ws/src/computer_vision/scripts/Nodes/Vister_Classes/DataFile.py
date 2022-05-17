import csv
import os

class DataFile:
    def __init__(self, name, path, header):  
        self.file_name = name+ ".csv"
        self.path = path
        with open(os.path.join(self.path,self.file_name), 'w', encoding='UTF8', newline='') as f:      
            writer = csv.writer(f)

            # write the header
            writer.writerow(header)
            f.close()

    # def create_data_file(self, header):                                                         #NEEDS TO BE CHANGED
    #     # header = ['']
    #     # for r in range(self.nr_of_rois):
    #     #     header.append('Roi'+str(r))                                                                     
    #     #     header.append('x'+str(r))
    #     #     header.append('y'+str(r))
    #     #     header.append('w'+str(r))
    #     #     header.append('h'+str(r))
           
    #     with open((self.file_name+ ".csv"), 'w', encoding='UTF8', newline='') as f:      
    #         writer = csv.writer(f)

    #         # write the header
    #         writer.writerow(header)
    #         f.close()

    def save_data(self,data):
        with open(os.path.join(self.path,self.file_name), 'a', encoding='UTF8', newline='') as f:      
            writer = csv.writer(f)
            # write data row
            writer.writerow(data)
            f.close()