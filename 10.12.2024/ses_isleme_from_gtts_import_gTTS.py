from gtts import gTTS
text='Merhaba ben sizin yapay zeka asistanı, size nasıl yardımcı olabilirim'
kayit=gTTS(text=text, lang='tr')
kayit.save('asistan.mp3')