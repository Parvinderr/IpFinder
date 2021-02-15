import socket as s 
import getmac
from sys import exit
import requests as r


print("1- Find IP Address Of Any Website ")
print("2- Find Your Host Name And Ip Address")
print("3- Find Service Name by Port Number ")
print("4- Find Port Number by Service Name ")
print("5- Find Your Mac Address ")
print("6- Get Location and Other Information of Website/Host")
print("7- Quit ")

answer = int(input('Enter Your Choice: '))
if answer>7 and answer<0:
    print('Invalid Choice')

if answer ==1:
    website = input('Enter Host/Website Name for Finding IP(Internet Protocol) Address: ')
    ip = s.gethostbyname(website)
    hostaddr = s.gethostbyaddr(ip)
    print(f'IP Address of {website} is {ip} and \nHost Address is {hostaddr[0]}')
elif answer ==2:
    urhostname = s.gethostname()
    urip = s.gethostbyname(urhostname)
    print(f'Your HostName is {urhostname} and your Ip Address is {urip}')
elif answer ==3:
    PortNum = int(input('Enter a Port Number: '))
    ServiceName = s.getservbyport(PortNum)
    print(f'Service Name For Port Number {PortNum} is {ServiceName}')
elif answer ==4:
    ServName = input('Enter a Service Name: ')
    portNum = s.getservbyname(ServName)
    print(f'Port Number for {ServName} is {portNum}')
elif answer ==5:
    mac = getmac.get_mac_address()
    print(f'Your Mac Address is {mac}')
elif answer ==6:
    api ='9fd44e699f9abccf23fc8c2a9a1d610e'
    webSite = input('Enter Website/Host Name: ')
    ipaddr = s.gethostbyname(webSite)
    req = r.get(f'http://api.ipapi.com/{ipaddr}?access_key={api}')
    j = req.json()
    ip,country_name,city,zip,lat,lon= j['ip'],j['country_name'],j['city'],j['zip'],j['latitude'],j['longitude']
    print(f'Ip Address is {ip}, Country Name is {country_name}\nCity Name is {city},Zip Code is {zip} \nLongitude is {lon} and Latitude is {lat}')

elif answer ==7:
    exit
