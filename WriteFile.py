from datetime import datetime

def wiriter(filename, user):
    message = raw_input("MSG: ")
    with open(filename, "w") as file:
  		file.write(datetime.now().strftime('%d-%m-%Y %H:%M:%S') + ":@" + user+ "-say: " + message)

def initChat(filename, msg):
    with open(filename, "w") as file:
  		file.write("join " + msg)

if __name__ == '__main__':
    filename = './chat.txt'
    user = raw_input('What is your name?')
    while True:
	    wiriter(filename, user)
