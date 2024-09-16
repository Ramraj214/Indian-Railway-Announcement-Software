import os
import pandas as pd 
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    mytext=str(text)
    language='hi'
    myobj=gTTS(text=mytext,lang=language,slow=True)
    myobj.save(filename)

#this function return pydub audio segment
def mergeAudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)

    return combined

def generateSkeleton():
    audio=AudioSegment.from_mp3("railway.mp3")

    # 0 - is to generate music
    start=18500
    finish=19500
    audioProcessed=audio[start:finish]
    audioProcessed.export("0_hindi.mp3",format="mp3")
    
    start=41000
    finish=42000
    audioProcessed=audio[start:finish]
    audioProcessed.export("12_en.mp3",format="mp3")

    # 1 is generate kripya dhyan digiye
    start=88000
    finish=90200
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_hindi.mp3",format="mp3")

    # 2 is from-city

    # 3 is generate se chalkar 
    start=91000
    finish=92200
    audioProcessed=audio[start:finish]
    audioProcessed.export("3_hindi.mp3",format="mp3")

    # 4 is via city

    # 5 is Generate ke raste
    start=94000
    finish=95000
    audioProcessed=audio[start:finish]
    audioProcessed.export("5_hindi.mp3",format="mp3")

    # is 6 to city
    
    # 7 is Generate ko jane Wali gadi sankhya
    start=96000
    finish=98900
    audioProcessed=audio[start:finish]
    audioProcessed.export("7_hindi.mp3",format="mp3")

    # 8 is generate train number and name

    # 9 is Generate kuch hi samay me platform sankhya 
    start=105500
    finish=108200
    audioProcessed=audio[start:finish]
    audioProcessed.export("9_hindi.mp3",format="mp3")

    # 10 is generate platform number

    # 11 is generate par aa rahi hai
    start=109000
    finish=110500
    audioProcessed=audio[start:finish]
    audioProcessed.export("11_hindi.mp3",format="mp3")

    # 12 - to generate Music
    start=41000
    finish=42000
    audioProcessed=audio[start:finish]
    audioProcessed.export("12_hindi.mp3",format="mp3")


def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 - Generate from city
        textToSpeech(item['from'],'2_hindi.mp3')

        # 4 - Generate via city
        textToSpeech(item['via'],'4_hindi.mp3')

        # 6 - Generate to city
        textToSpeech(item['to'],'6_hindi.mp3')

        # 8 - Generate train number and name
        textToSpeech(item['train_no']+" "+item['train_name'],'8_hindi.mp3')

        # 10 - Generate platform number
        textToSpeech(item['platform'],'10_hindi.mp3')

        audios=[f"{i}_hindi.mp3" for i in range(0,13)]

        announcement=mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format="mp3")


if __name__ =="__main__":
    print("Generating skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...") 
    generateAnnouncement("announce_hindi.xlsx")   
    