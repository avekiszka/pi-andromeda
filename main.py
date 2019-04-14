# start import statements
from scapy.all import *
import os
# end import statements
os.system("clear")
print("This is pi-Andromenda project")
def get_choice(help_text="Choose(1/2/3): "):
    return int(input(help_text))
def get_dst(help_text="Podaj Adres docelowy: "):
    return input(help_text)
def get_dp(help_text="Podaj numer portu docelowego: "):
    return int(input(help_text))
def net_tools():
    print("Wybierz narzedzie, ktore chcesz uruchomic: \n1) ICMP Ping\n2) Traceroute\n3) TCP Ping\n4) UDP Ping")
    ch1 = get_choice("(1/2/3/4): ")
    if ch1 == 1:
        os.system("clear")
        print("---ICMP-Ping---")
        p = IP(dst=get_dst())/ICMP()
        ans, unans = sr(p)
        print(ans[0][1].sprintf("Host %IP.src% is alive."))
    elif ch1 == 2:
        os.system("clear")
        print("---Traceroute---")
    elif ch1 == 3:
        os.system("clear")
        print("---TCP-Ping---")
        ans,uans =sr(IP(dst=get_dst())/TCP(dport=get_dp(), flags="S"))
        print(ans[0][1].sprintf("Host %IP.src% is alive"))
    elif ch1 == 4:
        os.system("clear")
        print("---UDP-Ping---")
        ans, uans = sr(IP(dst=get_dst())/UDP(dport=0))
        print(ans[0][1].sprintf("Host %IP.src% is alive"))

print("Wybierz Kategorie: \n1) Network Tools\n2) Network Scans\n3) Network Attacks")
cho1 = get_choice()
if cho1 == 1:
    print("Network Tools available")
    net_tools()
elif cho1 == 2:
    print("Network Scans available")
elif cho1 == 3:
    print("Network Attacks available")
else:
    print("Kategoria nie znaleziona.")