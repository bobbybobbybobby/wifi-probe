from wifi import Cell, Scheme

networks = list(Cell.all('wlan0'))

print(networks)
