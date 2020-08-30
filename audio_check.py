import speech_recognition as sr
import pyautogui, time

print('connecting to database .....')
def yes_sir():
    pyautogui.keyDown('winleft')
    pyautogui.press('r')
    pyautogui.keyUp('winleft')
    pyautogui.write('C:\\Users\\Asus\\Desktop\\yes_sir.m4a')
    pyautogui.press('enter')
time.sleep(0.5)
print('Starting Audio recogniser ')
def audio():
    print('collecting audio.......')
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ''
        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print('Exception: '+ str(e))

    return said
text = audio()


while True:
    if 'understand' in text or 'respond' in text or 'jai patidar' in text or 'jai' in text or 'jay patidar' in text or 'response' in text:
        print('Found a key word here')
        yes_sir()
        text = audio()
    else:
        print('key word didn\'t match ')
        print('trying again.........')
        text = audio()