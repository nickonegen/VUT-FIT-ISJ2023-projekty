# minitask 1
import re

# Replace the regular expression in the code below to match
# any string inside the slash brackets <...>
text = "</note> and <b>foo</b> and <i>so on</i> and 1 < 2"
print(re.findall(r"<(.*?)>", text))
