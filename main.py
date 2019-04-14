# start import statements
from scapy.all import *
# end import statements
print("This is pi-Andromenda project")
def get_choice(help_text="Choose(1/2/3): "):
    return int(input(help_text))
def get_dst(help_text="Podaj Adres docelowy: "):
    return input(help_text)
def net_tools():
    ans, unans = sr(IP(dst=get_dst())/ICMP())
    ans[0][0].sprintf("Host %IP.src% is alive.")

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