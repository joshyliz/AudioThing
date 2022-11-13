from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume, ISimpleAudioVolume
import keyboard
from time import sleep
from winsound import Beep

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)

volume = cast(interface, POINTER(IAudioEndpointVolume))

sessions = AudioUtilities.GetAllSessions()

def LowerVolume(sessions):
    Beep(1500, 250)
    for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and session.Process.name() == "Discord.exe":
                volume.SetMasterVolume(0.15, None) 

def IncreaseVolume(sessions):
    Beep(500, 250)
    for session in sessions:
            volume = session._ctl.QueryInterface(ISimpleAudioVolume)
            if session.Process and session.Process.name() == "Discord.exe":
                volume.SetMasterVolume(1, None) 


#huh
lowered = False
pressed = False
key = 'l'

while(True):
        if keyboard.is_pressed(key) != True:
            pressed = False
        elif keyboard.is_pressed(key) == True and lowered == False and pressed == False:
            LowerVolume(sessions)
            lowered = True
            pressed = True
        elif keyboard.is_pressed(key) == True and lowered == True and pressed == False:
            IncreaseVolume(sessions)
            lowered = False
            pressed = True 
        print("Volume Lowered =" ,lowered)


       