# ISJ mini-úloha 2
# @author Onegen Something <xonege99@vutbr.cz>

# Téma: Regulárne výrazy
# Zadanie: Nahraďte posledné 'du' na 'DU'
# Očekávaný výstup:
#                   du du DU
#                   du po leDU
#                   dopředu DU
#                   i dozadu DU
#                   dudu DUpl
#                   Rammstein DU hast

import re
pattern = re.compile(r'du(?!.*du)')
text = ['du du du',
        'du po ledu',
        'dopĹedu du',
        'i dozadu du',
        'dudu dupl',
        'Rammstein du hast']

for row in text:
    print(re.sub(pattern, 'DU', row))
