import matplotlib
import csv
import re

class ReadLog:
    def __init__(self):
        pass

    def wopen_file(self):
        with open('smic_log.csv','r') as f:
            for line in f:
                print(line)
    def exec(self):
        print('1')

ReadLog.wopen_file('smic_log.csv')