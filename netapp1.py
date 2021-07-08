#ref link: https://github.com/ktbyers/netmiko/blob/develop/EXAMPLES.md#executing-show-command
from netmiko import ConnectHandler
import getpass

#prompt user for username and password
username = input('Enter username: ')
p=getpass.getpass('Enter password: ')
#prompts for ip of device
ip = input('Please type the IP of the device you need to reach: ')

#define device dictionary based on info entered
cisco_dev = {
    'device_type': 'cisco_ios',
    'ip': ip,
    'username': username,
    'password': p,
}

c = ConnectHandler(**cisco_dev) 
# Show command that we execute.
command = input("Enter the command you would like to enter: ")

#runs ssh session and issues command
try:
    c.enable()
    output = c.send_command(command)
    # Automatically cleans-up the output so that only the show output is returned
    print()
    print(output)
    print()
    #disconnects ssh session 
    c.disconnect()
except Exception as e:
    print(e)