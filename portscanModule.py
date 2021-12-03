#!/usr/bin/python3
#Author: Brayden Karnes
#Date: 11/19/21
#Descriptions: NMAP port scanner using python

import nmap
class portscanner:

    def scan(target, portRange):
        scanner = nmap.PortScanner()

        for i in range(portRange):
            result = scanner.scan(target, str(i))
            result = result['scan'][target]['tcp'][i]['state']

            print(f'port {i} is {result}.')
