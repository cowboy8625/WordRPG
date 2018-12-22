""" CONSTANTS for gui module """



TITLE = 'WASTELANDS'
VERSION = 1.0
CHAR_SIZE = (8, 16)
# size of terminal for printable characters
FIELD_SIZE = (80,30)
# size of screen for terminal window. Includes padding and extra room for input field
SCREEN_SIZE = (FIELD_SIZE[0], FIELD_SIZE[1] + 1)
# screen resolution in pixels
SCREEN_RES = (SCREEN_SIZE[0] * CHAR_SIZE[0], SCREEN_SIZE[1] * CHAR_SIZE[1])
# 1 space of padding inside of frame
    
HEADER = f'{TITLE} - {VERSION}'
FOOTER = 'COWBOY GAMING - 2018'  # © can cause problems with encoding
# This constant sets color/style formatting on or off
FORMAT_TEXT = False

# # Extended ascii characters used to build frame elements
# FRAME = {
#    'boxH' : '═',		#205
#    'boxV' : '║',		#186
#    'boxVH' : '╬',		#206

#    'boxDL' : '╗',		#187
#    'boxUL' : '╝',		#188
#    'boxDR' : '╔',		#201
#    'boxUR' : '╚',		#200

#    'boxVL' : '╣',		#185
#    'boxVR' : '╠',		#204
#    'boxHU' : '╩',		#202
#    'boxHD' : '╦',		#203
# }

# # colors
# COL_FRAME		= Fore.CYAN
# COL_HEADER		= Fore.LIGHTRED_EX
# COL_FOOTER		= Fore.RED
# COL_NUMBER     = Fore.YELLOW
# COL_TEXT       = Fore.WHITE
