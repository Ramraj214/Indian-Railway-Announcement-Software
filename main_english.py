import os
import pandas as pd 
from pydub import AudioSegment
from gtts import gTTS

def textToSpeech(text,filename):
    mytext=str(text)
    language='en-in'
    myobj=gTTS(text=mytext,lang=language,slow=False)
    myobj.save(filename)

def generateSkeleton():
    audio=AudioSegment.from_mp3("railway.mp3")
    # 1 is to generate Music
    start=18500
    finish=19500
    audioProcessed=audio[start:finish]
    audioProcessed.export("1_en.mp3",format="mp3")

    # 9 - is to generate music
    start=41000
    finish=42000
    audioProcessed=audio[start:finish]
    audioProcessed.export("9_en.mp3",format="mp3")

#this function return pydub audio segment
def mergeAudios(audios):
    combined=AudioSegment.empty()
    for audio in audios:
        combined+=AudioSegment.from_mp3(audio)

    return combined


def generateAnnouncement(filename):
    df=pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():
        # 2 is generate kripya dhyan digiye
        textToSpeech(item['request'],'2_en.mp3')

        # 3 - Generate train number
        textToSpeech(item['train_no'],'3_en.mp3')

        # 4 - is generate se chalkar 
        textToSpeech(item['from'],'4_en.mp3')

        # 5 - Generate to city
        textToSpeech(item['to'],'5_en.mp3')

        # 6 - Generate train name
        textToSpeech(item['train_name'],'6_en.mp3')

        # 7 - Generate via city
        textToSpeech(item['via'],'7_en.mp3')

        # 8 - Generate platform number
        textToSpeech(item['platform'],'8_en.mp3')

        audios=[f"{i}_en.mp3" for i in range(1,10)]

        announcement=mergeAudios(audios)
        announcement.export(f"announcement_{item['train_no']}_{index+1}.mp3",format="mp3")


if __name__ =="__main__":
    print("Generating skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...") 
    generateAnnouncement("english_announcement.xlsx")   
    