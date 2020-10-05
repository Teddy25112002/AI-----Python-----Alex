def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=5)
        try:
            text = r.recognizer_google(audio, language="vi-VN")
            print(text)
            return text
        except:
            print('...')
            return 0
            