from datetime import datetime

def wiriter(filename, user):
    message = raw_input("MSG: ")
    with open(filename, "a") as file:
  		file.write(datetime.now().strftime('%d-%m-%Y %H:%M:%S') + ":@" + user+ "-say: " + message + '\n')
  		file.close()

def initChat(filename, msg):
    with open(filename, "a") as file:
  		file.write("========= " + msg + " JOIN CHAT ==============="  + '\n')

if __name__ == '__main__':
    filename = './chat.txt'
    user = raw_input('What is your name?')
    initChat(filename, user)
    while True:
	    wiriter(filename, user)
