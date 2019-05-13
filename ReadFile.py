import time, os

def reader(filename):
    with open(filename, "r") as file:
		for line in file:
  			print(line)

if __name__ == '__main__':
    filename = './chat.txt'
    size = 1;
    while size > 0:
    	s = os.path.getsize(filename)
    	if (s > size):
    		reader(filename)
    	time.sleep(3)
    	size = s
   