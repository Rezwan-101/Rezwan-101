import sys
import random
import pyfiglet

fonts = pyfiglet.FigletFont.getFonts()
if len(sys.argv) == 1:
    font = random.choice(fonts)

elif len(sys.argv) == 3 and sys.argv[1] in ["-f", "--font"]:
    font = sys.argv[2]

    if font not in fonts:
        sys.exit("Invalid Usage")
else:
    sys.exit("Invalid Usage")

text = input("input: ")

figlet = pyfiglet.Figlet(font=font)
print(figlet.renderText(text))



