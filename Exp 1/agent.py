import speech_recognition as sr
import sounddevice as sd
import numpy as np
import os
import webbrowser
from scipy.io.wavfile import write

globalFlag = 0

def DFS(node, searchItem):
	global globalFlag
	if searchItem in node.value:
		os.system(f"start vlc ./songs{node.value}")
		globalFlag = 1
		return
	if globalFlag == 0:		DFS(node.left, searchItem)
	if globalFlag == 0:		DFS(node.right, searchItem)

sd.default.dtype='int32', 'int32'
fs = 44100  # Sample rate
seconds = 5  # Duration of recording
print("Speak...")
myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('output.wav', fs, myrecording.astype(np.int32))  # Save as WAV file in 32-bit format
recognizer = sr.Recognizer()
sound = "output.wav"
songList = os.listdir(path="./songs")

with sr.AudioFile(sound) as source:
	print("Converting the answer to text...")
	audio = recognizer.listen(source)

	try:
		flag = 0
		text = recognizer.recognize_google(audio)
		textlst = text.split()
		if textlst[0].lower() == "jarvis":
			if " ".join(textlst[1:]).lower() == "show my weather":
				print("Check your browser")
				webbrowser.open_new_tab("https://www.accuweather.com/en/in/kalyan-dombivali/2771484/weather-forecast/2771484")
			elif textlst[1].lower() == "play":
				print("Searching song:" + " ".join(textlst[2:]).lower())
				for i in songList:
					if " ".join(textlst[2:]).lower() in i.lower():
						os.system(f"""start vlc "./songs/{i}" """)
						print("Playing song...")
						flag = 1
				if flag == 0:
					print("No such song is available with us...")
	except Exception as e:
		print('Exception',e)