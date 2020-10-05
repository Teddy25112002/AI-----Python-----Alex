def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe') # Trong ngoặc là đường dẫn đến App của máy mình, các bạn tự tìm lại theo đúng máy của các bạn nha, chép theo tui mở hông được ráng chịu à nhen ^^
    elif "word" in text:
        speak("Mở Microsoft Word")
        os.startfile('C:\Program Files\Microsoft Office\Office15\WINWORD.EXE') # Ở đây cũng thế
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        os.startfile('C:\Program Files\Microsoft Office\Office15\EXCEL.EXE') # Chỗ này y xì bên trên :3
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")