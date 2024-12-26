import dns
import dns.resolver
import socket
import requests
from ip2geotools.databases.noncommercial import DbIpCity
from geopy.distance import distance

def printDetails(ip):
    res = DbIpCity.get(ip, api_key="free")
    print(f"Location: {res.city}, {res.region}, {res.country}")

print('Get Advanced MailBox Info.\nType Mail Address here:')
mbox = input()
maildomain = mbox.split("@")[1]
print('Please wait')
answers = dns.resolver.resolve(maildomain, 'MX')
print(f'Searched by Mail: {mbox}\nMail Domain: {maildomain}\nInfo about MX Servers:')
for rdata in answers:
    answers = dns.resolver.resolve(rdata.exchange, 'A')
    print('Host', rdata.exchange, 'has preference', rdata.preference)
    for rdata in answers:
        response = requests.get(f'https://ipapi.co/{rdata.address}/json/').json()
        print(f'Host IP: {rdata.address}\nServer Geo Info:')
        printDetails(rdata.address)