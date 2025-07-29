
banner = (

    '''
 _______  __   __  ______   _______  __   __  ___   __    _  _______  ______   
|       ||  | |  ||      | |  _    ||  |_|  ||   | |  |  | ||       ||    _ |  
|    ___||  |_|  ||  _    || |_|   ||       ||   | |   |_| ||    ___||   | ||  
|   | __ |       || | |   ||       ||       ||   | |       ||   |___ |   |_||_ 
|   ||  ||       || |_|   ||  _   | |       ||   | |  _    ||    ___||    __  |
|   |_| ||   _   ||       || |_|   || ||_|| ||   | | | |   ||   |___ |   |  | |
|_______||__| |__||______| |_______||_|   |_||___| |_|  |__||_______||___|  |_|
                                                                @incoggeek v1.0
    '''
)

# ANSI escape codes for text colors
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLACK = '\033[30m'
WHITE = '\033[97m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
RESET = '\033[0m'
# Reset to default color

# ANSI escape codes for text styles
BOLD = '\033[1m'
ITALIC = '\033[3m'
UNDERLINE = '\033[4m'
STRIKETHROUGH = '\033[9m'

# Emoji

MAGNI = "\U0001F50E"   # Magnify
CROSS = "\U0000274C"   # Cross Mark
LAUGH = "\U0001F639"   # Laughing Cat Face
FOUND = "\U0001F64C"   # Person Raising Both Hands
NOPE = "\U0001F645"    # Person Gesturing No
BYE = "\U0000270C"     # Victory Hand
SUCCESS = "\U00002705"  # Check Mark
TOOL = "\U0001F527"    # Tool
GLOBE = "\U0001F30D"   # Globe
FIRE = "\U0001F525"    # Fire
INTE = "\U0001F616"    # Interrupt
SLEEP = "\U0001F634"   # Sleep
SAD = "\U0001F613"   # Sad
FILE = "\U0001F4C1"  # File
HRT = "\U00002764"  # Heart


def color_style_text(color, text, style=''):
    print((color + style + text + RESET))


def red_text(text):
    print((RED + text + RESET))


def green_text(text):
    print((GREEN + text + RESET))


def yellow_text(text):
    print(YELLOW + text + RESET)


def cyan_text(text):
    print(CYAN + text + RESET)


category = {
    1: "Footholds",
    2: "Files Containing Usernames",
    3: "Sensitive Directories",
    4: "Web Server Detection",
    5: "Vulnerable Files",
    6: "Vulnerable Servers",
    7: "Error Messages",
    8: "Files Containing Juicy Info",
    9: "Files Containing Passwords",
    10: "Sensitive Online Shopping Info",
    11: "Network or Vulnerability Data",
    12: "Pages Containing Login Portals",
    13: "Various Online Devices",
    14: "Advisories and Vulnerabilities"
}
