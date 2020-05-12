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


if __name__ == '__main__':

    folder = 'C:/Users/lupya/Desktop/test/'
    files = os.listdir(folder)
    num_of_processes = 1
    processes = []

    for i in range(num_of_processes):
        p = NewProcess(folder, files)
        processes.append(p)

    for process in processes:
        process.start()
