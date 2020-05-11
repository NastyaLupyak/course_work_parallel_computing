from multiprocessing import Process
import os
from time import time

class NewProcess(Process):

    def __init__(self, folder):
        Process.__init__(self)
        self.folder = folder
        self.process_dictionary = {}

    def run(self):
        self.open_files()
        return self.process_dictionary

    def inverted_index(self):
        pass


 if __name__ == '__main__':

    folder = 'C:/Users/lupya/Desktop/test/'
    files = os.listdir(folder) 
    num_of_processes = 1
    processes = []

    for i in range(num_of_processes):
        p = NewProcess(folder)
        processes.append(p)


    for process in processes:
        process.start()



    