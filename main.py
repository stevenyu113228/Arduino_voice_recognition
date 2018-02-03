import pyaudio
import numpy as np
import speech_recognition
import time
import arduino_ctrl


print("系統初始化中...")
time.sleep(3)

r = speech_recognition.Recognizer()

CHUNK = 2**10
RATE = 44100

p=pyaudio.PyAudio()
stream=p.open(format=pyaudio.paInt16,channels=1,rate=RATE,input=True,frames_per_buffer=CHUNK)



def record():
    print("開始錄音")
    with speech_recognition.Microphone() as source:
        audio = r.listen(source)
    print("錄音結束，開始辨識")
    try:
        result = r.recognize_google(audio,language = 'zh-TW')
    except:
        result = '辨識失敗'
    print("辨識結果: " + result)
    arduino_ctrl.arduino_do(result)



print("開始執行")
while True:
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=RATE,
                input=True, frames_per_buffer=CHUNK)
    data = np.fromstring(stream.read(CHUNK),dtype=np.int16)
    peak = np.average(np.abs(data))
    #print(peak)
    if peak > 400:  #音量過大才算是有效內容
        record()
        time.sleep(1)
    
    
    
