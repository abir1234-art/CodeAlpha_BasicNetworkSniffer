#!/usr/bin/env python
import scapy.all as scapy
from scapy.layers import http

def sniff(iface):
	scapy.sniff(iface=iface, store=False, prn=process_packet)
	
def process_packet(packet):
	if packet.haslayer(http.HTTPRequest):
		print(packet.show())
		
def main():
	sniff('eth0')
	
if __name__ == '__main__':
	main()
