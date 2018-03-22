import pyautogui
import sys

a = pyautogui
a.PAUSE = 2;

if (len(sys.argv) != 2):
	print("Correct usage: python auto-key-mouse [genre], where [genre] is a string")
	sys.exit(0)
genre = sys.argv[1]

def get(genre):
	#open browser (chrome)
	a.hotkey('ctrl', 'alt', 'a')
	
	#navigate to youtube
	a.typewrite('youtube.com')
	a.typewrite(['enter'])

	#search for genre
	a.typewrite(genre)
	a.typewrite(['enter'])

	#click first link
	a.moveTo(438, 326)
	a.click()

get(genre)
