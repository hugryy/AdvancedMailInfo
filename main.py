import dns
import dns.resolver


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
        print(f'Host IP: {rdata.address}')