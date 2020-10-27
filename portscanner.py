import sys
import socket
import pyfiglet

banner=pyfiglet.figlet_format("PORT SCANNER")
print(banner)
print(" "*30)
target=input("Enter The host to be scan : ")
print("-"*50)
print("Scanning Target : ",target)
print("-"*50)
try:
    for port in range(1, 65535):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((target, port))
        if result == 0:
            print("[+] Port {} is open".format(port))
        s.close()

except KeyboardInterrupt:
    print("\n Exitting Program !!!!")
    sys.exit()
except socket.gaierror:
    print("\n Hostname Could Not Be Resolved !!!!")
    sys.exit()
except socket.error:
    print("\ Server not responding !!!!")
    sys.exit()