# ISJ mini-úloha 1
# @author Onegen Something <xonege99@vutbr.cz>

# Téma: Regulárne výrazy
# Zadanie: Nahraďte regulárny výraz v nasledujúcom kóde tak, aby zodpovedal 
# akémukoľvek reťazcu vo vnútri lomených zátvoriek.
# Očekávaný výstup: seznam ['/note', b', '/b', 'i', '/i']

import re
text = '</note> and <b>foo</b> and <i>so on</i> and 1 < 2'
print(re.findall(r'<(.*?)>', text))
