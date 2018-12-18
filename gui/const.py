from colorama import Back, Fore, Style, init
init( convert = True )



# Extended ascii characters used to build frame elements
FRAME = {
   'boxH'	: '═',		#205
   'boxV'	: '║',		#186	
   'boxVH'	: '╬',		#206

   'boxDL'	: '╗',		#187
   'boxUL'	: '╝',		#188
   'boxDR'	: '╔',		#201
   'boxUR'	: '╚',		#200

   'boxVL'	: '╣',		#185
   'boxVR'	: '╠',		#204
   'boxHU'	: '╩',		#202
   'boxHD'	: '╦',		#203
}

# colors
COL_FRAME		= Fore.CYAN
COL_HEADER		= Fore.LIGHTRED_EX
COL_FOOTER		= Fore.RED
COL_NUMBER     = Fore.YELLOW
COL_TEXT       = Fore.WHITE
