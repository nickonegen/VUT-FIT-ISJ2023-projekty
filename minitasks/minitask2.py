# minitask 2
import re

# Change the regular expression in the code to replace the last
# occurrence of the string du with DU.
pattern = re.compile(r"du(?!.*du)")
text = [
    "du du du",
    "du po ledu",
    "dopředu du",
    "i dozadu du",
    "dudu dupl",
    "Rammstein du hast",
]

for row in text:
    print(re.sub(pattern, "DU", row))
