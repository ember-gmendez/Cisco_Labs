#refer to link https://github.com/ktbyers/netmiko/issues/2095 for setting textfsm path 
from netmiko import ConnectHandler
import getpass
#import json

#prompt user for username and password
username = input('Enter username: ')
p=getpass.getpass('Enter password: ')
#prompt for device ip
ip = input('Please type the IP of the device you need to reach: ')

#define device dictionary based on entered info
cisco_dev = {
    'device_type': 'cisco_ios',
    'ip': ip,
    'username': username,
    'password': p,
}

try:
    # using **variable unpacks a python dictionary
    c = ConnectHandler(**cisco_dev)
    # Enter enable mode, issue command, and disconnect
    c.enable()
    interfaces = c.send_command('show ip int brief', use_textfsm=True)
    #print(json.dumps(interfaces, indent=2))
    for interface in interfaces:
        print(f"{interface['intf']} is currently {interface['status']}")
    c.disconnect()
except Exception as e:
    print(e)