def assistant():
    speak("Xin chào, bạn tên là gì nhỉ?")
    name = get_text()
    if name:
        speak("Chào bạn {}".format(name))
        speak("Bạn cần Bot Alex có thể giúp gì ạ?")
        while True:
            text = get_text()
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "ngủ thôi" in text:
                stop()
                break
            elif "có thể làm gì" in text:
                help_me()
            elif "chào trợ lý ảo" in text:
                hello(name)
            elif "hiện tại" in text:
                get_time(text)
            elif "mở" in text:
                if 'mở google và tìm kiếm' in text:
                    open_google_and_search(text)
                elif "." in text:
                    open_website(text)
                else:
                    open_application(text)
            elif "email" in text or "mail" in text or "gmail" in text:
                send_email(text)
            elif "thời tiết" in text:
                current_weather()
            elif "chơi nhạc" in text:
                play_song()
            elif "hình nền" in text:
                change_wallpaper()
            elif "đọc báo" in text:
                read_news()
            elif "định nghĩa" in text:
                tell_me_about()
            elif "giới thiệu" in text:
                introduce()
    else:
        speak("Bạn cần Bot giúp gì ạ?")