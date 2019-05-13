import time, os
from os import system

def reader(filename):
    with open(filename, "r") as file:
		for line in file:
  			print(line)

if __name__ == '__main__':
    filename = './chat.txt'
    while True:
    	system('clear')
    	reader(filename)
    	time.sleep(2)
   