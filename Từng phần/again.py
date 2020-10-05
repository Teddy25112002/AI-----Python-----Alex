def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Bot chưa hiểu ý của bạn. Bạn nói lại được không ?")
    time.sleep(2)
    stop()
    return 0