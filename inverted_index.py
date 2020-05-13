#!/usr/bin/python
# -*- coding: utf-8 -*-
from multiprocessing import Process
import os
from time import time


class NewProcess(Process):

    def __init__(self, folder, files):
        Process.__init__(self)
        self.folder = folder
        self.process_dictionary = {}
        self.files = files

    def run(self):
        for file in self.files:
            with open(self.folder + file) as file_handler:
                for text in file_handler:
                    text = text.split(' ')
                    text = [self.edit(x) for x in text]
                    self.inverted_index(text, file)
        return self.process_dictionary

    def edit(self, word):
        symb = [
            ',',
            '!',
            '/',
            '?',
            '.',
            '(',
            ')',
            "'",
            '"',
            ]
        word = word.lower()
        if word:
            for s in symb:
                if s in word:
                    word = word.replace(s, '')
        return word

    def inverted_index(self, string, doc_name):
        index = 0
        for i in string:
            if i not in self.process_dictionary.keys():
                self.process_dictionary[i] = [(doc_name, index)]
            else:
                self.process_dictionary[i] += [(doc_name, index)]
            index += 1

def calculate_index(files, N):
    
    size = int(len(files) / N)
    list_index = []
    for x in range(N):
        list_index.append(x*size)
    list_index.append(None)

    return list_index

if __name__ == '__main__':

    folder = 'C:/Users/lupya/Desktop/test/'
    files = os.listdir(folder)
    N = 1
    processes = []
    list_index = calculate_index(files, N)

    for i in range(N):
        p = NewProcess(folder, files[list_index[i]:list_index[i+1]])

        processes.append(p)
    inv_index = []
    for process in processes:
        inv_index.append(process.run())

    main_dict = inv_index[-1]
    for el in inv_index[0:]:
        for key in el.keys():
            if key in main_dict.keys():
                main_dict[key] += el[key]
            else:
                main_dict[key] = el[key]