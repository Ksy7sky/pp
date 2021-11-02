from typing import List


csv = 'kSeNiYa|miKHAil|PoPa'

ListForCsv = csv.split('|')

ListForCsv = [a.capitalize() for a in ListForCsv]

print(ListForCsv)