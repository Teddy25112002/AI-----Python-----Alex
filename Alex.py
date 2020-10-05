# Ở bước này, các bạn import các thư viện cần thiết cho quá trình tạo nên con trợ lý ảo nhá. Các bạn nào chạy mà bị lỗi thì lên Google search cách tải thư viện cho python nha.
import os
import playsound
import speech_recognition as sr
import time
import sys
import ctypes
import wikipedia
import datetime
import json
import re
import webbrowser
import smtplib
import requests
import urllib
import urllib.request as urllib2
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from time import strftime
from gtts import gTTS
from youtube_search import YoutubeSearch

# Khúc này là khai báo các biến cho quá trình làm con Alex
wikipedia.set_lang('vi')
language = 'vi'
path = ChromeDriverManager().install()


# Text - to - speech: Chuyển đổi văn bản thành giọng nói
def speak(text):
    print("Bot: {}".format(text))
    tts = gTTS(text=text, lang=language, slow=False)
    tts.save("sound.mp3")
    playsound.playsound("sound.mp3", False)
    os.remove("sound.mp3")


# Speech - to - text: Chuyển đổi giọng nói bạn yêu cầu vào thành văn bản hiện ra khi máy trả lại kết quả đã nghe
def get_audio():
    print("\nBot: \tĐang nghe \t --__-- \n")
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tôi: ", end='')
        audio = r.listen(source, phrase_time_limit=8)
        try:
            text = r.recognize_google(audio, language="vi-VN")
            print(text)
            return text.lower()
        except:
            print("...")
            return 0


# Ở dòng này, Bot sẽ chào tạm biệt bạn khi bạn tạm biệt nó ^^ 
def stop():
    speak("Hẹn gặp lại bạn sau!")
    time.sleep(2)


# Khúc này Alex sẽ hỏi lại những gì mà bạn nói vào nhưng Alex không nghe rõ do bị dính tạp âm
def get_text():
    for i in range(3):
        text = get_audio()
        if text:
            return text.lower()
        elif i < 2:
            speak("Máy không nghe rõ. Bạn nói lại được không!")
            time.sleep(3)
    time.sleep(2)
    stop()
    return 0


# Ở đây là bước chào hỏi. Alex sẽ phân vùng thời gian để trò chuyện với bạn cho hợp lý nha ^^
def hello(name):
    day_time = int(strftime('%H'))
    if day_time < 12:
        speak("Chào buổi sáng bạn {}. Chúc bạn một ngày tốt lành.".format(name))
    elif 12 <= day_time < 18:
        speak("Chào buổi chiều bạn {}. Bạn đã dự định gì cho chiều nay chưa.".format(name))
    else:
        speak("Chào buổi tối bạn {}. Bạn đã ăn tối chưa nhỉ.".format(name))
    time.sleep(5)


#Alex đang trả lời bạn về thời gian và ngày tháng nè.
def get_time(text):
    now = datetime.datetime.now()
    if "giờ" in text:
        speak('Bây giờ là %d giờ %d phút %d giây' % (now.hour, now.minute, now.second))
    elif "ngày" in text:
        speak("Hôm nay là ngày %d tháng %d năm %d" %
              (now.day, now.month, now.year))
    else:
        speak("Bot chưa hiểu ý của bạn. Bạn nói lại được không?")
    time.sleep(4)


# Ai mà lười kích đúp chuột để mở ứng dụng thì gọi Alex lên nhoa :3
def open_application(text):
    if "google" in text:
        speak("Mở Google Chrome")
        time.sleep(2)
        os.startfile('C:\Program Files\Google\Chrome\Application\chrome.exe') # Trong ngoặc là đường dẫn đến ứng dụng trong máy mình, các bạn tự tìm trong máy mình sao cho đúng nha
    elif "word" in text:
        speak("Mở Microsoft Word") 
        time.sleep(2)
        os.startfile('C:\Program Files\Microsoft Office\Office15\WINWORD.EXE') # Ở đây cũng như ở trên
    elif "excel" in text:
        speak("Mở Microsoft Excel")
        time.sleep(2)
        os.startfile('C:\Program Files\Microsoft Office\Office15\EXCEL.EXE') # Ở trển cũng giống dưới này =))
    else:
        speak("Ứng dụng chưa được cài đặt. Bạn hãy thử lại!")
        time.sleep(3)


# Alex mở web cho bạn được luôn nè
def open_website(text):
    reg_ex = re.search('mở (.+)', text)
    if reg_ex:
        domain = reg_ex.group(1)
        url = 'https://www.' + domain
        webbrowser.open(url)
        speak("Trang web bạn yêu cầu đã được mở.")
        time.sleep(3)
        return True
    else:
        return False


# Muốn kiếm chị Google mà ngại tiếp xúc với chị ấy thì nhờ Alex nói giùm ha ^^
def open_google_and_search(text):
    search_for = text.split("kiếm", 1)[1]
    speak('Okay!')
    driver = webdriver.Chrome(path)
    driver.get("http://www.google.com")
    que = driver.find_element_by_xpath("//input[@name='q']")
    que.send_keys(str(search_for))
    que.send_keys(Keys.RETURN)
    time.sleep(10)


# Alex còn biết gửi mail mà không cần bật gmail á, thấy giỏi hôn nè ^^
def send_email(text):
    speak('Bạn gửi email cho ai nhỉ')
    recipient = get_text()
    if 'nghĩa' in recipient: # 'nghĩa' ở đây là keywords để máy tiếp tục gửi email cho bạn. Bạn có thể thay cái keywords này
        speak('Nội dung bạn muốn gửi là gì')
        content = get_text()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('xyz', 'abc') # Ở khúc này, 'xyz' là địa chỉ email của bạn, 'abc' là mật khẩu của email đó
        mail.sendmail('xyz', 
                      '123', content.encode('utf-8')) # 'xyz' vẫn như cũ như 'abc' là địa chỉ email của người mà bạn muốn họ nhận thư nha 
        mail.close()
        speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
    else:
        speak('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không')


# Muốn đi chơi mà sợ trời mưa thì hãy xem dự báo thời tiết nha, nhớ gọi Alex đó
def current_weather():
    speak("Bạn muốn xem thời tiết ở đâu ạ.")
    time.sleep(3)
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = get_text()
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        current_temperature = city_res["temp"]
        current_pressure = city_res["pressure"]
        current_humidity = city_res["humidity"]
        suntime = data["sys"]
        sunrise = datetime.datetime.fromtimestamp(suntime["sunrise"])
        sunset = datetime.datetime.fromtimestamp(suntime["sunset"])
        wthr = data["weather"]
        weather_description = wthr[0]["description"]
        now = datetime.datetime.now()
        content = """
        Hôm nay là ngày {day} tháng {month} năm {year}
        Mặt trời mọc vào {hourrise} giờ {minrise} phút
        Mặt trời lặn vào {hourset} giờ {minset} phút
        Nhiệt độ trung bình là {temp} độ C
        Áp suất không khí là {pressure} héc tơ Pascal
        Độ ẩm là {humidity}%
        Trời hôm nay quang mây. Dự báo mưa rải rác ở một số nơi.""".format(day = now.day,month = now.month, year= now.year, hourrise = sunrise.hour, minrise = sunrise.minute,
                                                                           hourset = sunset.hour, minset = sunset.minute, 
                                                                           temp = current_temperature, pressure = current_pressure, humidity = current_humidity)
        speak(content)
        time.sleep(28)
    else:
        speak("Không tìm thấy địa chỉ của bạn")
        time.sleep(2)


#Relax hôn, nghe nhạc trên Youtube nè ^^
def play_song():
    speak('Xin mời bạn chọn tên bài hát')
    time.sleep(2)
    mysong = get_text()
    while True:
        result = YoutubeSearch(mysong, max_results=10).to_dict()
        if result:
            break
    url = 'https://www.youtube.com' + result[0]['url_suffix']
    webbrowser.open(url)
    speak("Bài hát bạn yêu cầu đã được mở.")
    time.sleep(3)


# Không biết dạo này tình hình Cô Vy như thế nào rồi nhỉ, đọc báo phát xem thử nào :)
def read_news():
    speak("Bạn muốn đọc báo về gì")
    
    queue = get_text()
    params = {
        'apiKey': '30d02d187f7140faacf9ccd27a1441ad',
        "q": queue,
    }
    api_result = requests.get('http://newsapi.org/v2/top-headlines?', params)
    api_response = api_result.json()
    print("Tin tức")

    for number, result in enumerate(api_response['articles'], start=1):
        print(f"""Tin {number}:\nTiêu đề: {result['title']}\nTrích dẫn: {result['description']}\nLink: {result['url']}
    """)
        if number <= 3:
            webbrowser.open(result['url'])


# Hình nền máy tính bạn liệu có quá nhàm chán, hãy đổi ngay với Alex nhá
def change_wallpaper():
    api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
    url = 'https://api.unsplash.com/photos/random?client_id=' + \
    # Bạn có thể truy cập trang web unsplash.com để tải những ảnh nền đẹp nha
        api_key  
    f = urllib2.urlopen(url)
    json_string = f.read()
    f.close()
    parsed_json = json.loads(json_string)
    photo = parsed_json['urls']['full']
    # Nhớ đưa cái đường dẫn của mấy tấm ảnh nền mà bạn muốn thay đổi vào nha ^^
    urllib2.urlretrieve(photo, "C:\\Users\\PC\\b.jpg")
    image=os.path.join("C:\\Users\\PC\\b.jpg")
    ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
    speak('Hình nền máy tính vừa được thay đổi')
    time.sleep(3)


# Bật mí là con Bot này rất rất là "nhiều chuyện". Nên hổng biết cái gì cứ hỏi nó nha ^^
def tell_me_about():
    try:
        speak("Bạn muốn nghe về gì ạ")
        time.sleep(2)
        text = get_text()
        contents = wikipedia.summary(text).split('\n')
        speak(contents[0].split(".")[0])
        time.sleep(10)
        for content in contents[1:]:
            speak("Bạn muốn nghe thêm không")
            time.sleep(2)
            ans = get_text()
            if "có" not in ans:
                break    
            speak(content)
            time.sleep(10)

        speak('Cảm ơn bạn đã lắng nghe!!!')
        time.sleep(3)
    except:
        speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")
        time.sleep(5)

# Khúc này là tự bạch của Alex. Bạn có thể thay đổi cái nội dung bên trong tùy theo ý thích của bạn nha
def introduce():
    speak("Xin chào bạn. Rất hân hạnh được phục vụ bạn. Tôi là Alex. Tôi là trợ lý ảo được tạo ra dựa trên ngôn ngữ lập trình Python kết hợp với AI. Tôi sinh ra vào ngày 4/10/2020 và được sáng lập bởi Lê Phước Nghĩa. Hiện tại bạn đang sử dụng phiên bản Alex 1.0 và cũng đang là phiên bản mới nhất.")


# Ở đây là những gì mà Alex có thể làm và đang show cái list ra cho bạn xem nè
def help_me():
    speak("""Bot có thể giúp bạn thực hiện các câu lệnh sau đây:
    1. Chào hỏi
    2. Hiển thị giờ
    3. Mở website, application
    4. Tìm kiếm trên Google
    5. Gửi email
    6. Dự báo thời tiết
    7. Mở video nhạc
    8. Thay đổi hình nền máy tính
    9. Đọc báo hôm nay
    10. Kể bạn biết về thế giới """)
    time.sleep(27)
    
    
# Liên kết chúng lại để tạo thành con Bot Alex hoàn chỉnh thôi nào ^_^
def assistant():
    speak("Xin chào, bạn tên là gì nhỉ?")
    time.sleep(2)
    name = get_text()
    if name:
        speak("Chào bạn {}".format(name))
        speak("Bạn cần Bot Alex có thể giúp gì ạ?")
        time.sleep(3)
        while True:
            text = get_text()
            if not text:
                break
            elif "dừng" in text or "tạm biệt" in text or "chào robot" in text or "ngủ thôi" in text:
                stop()
                break
            elif "có thể làm gì" in text:
                help_me()
            elif "chào" in text:
                hello(name)
            elif "giờ" in text or "ngày" in text:
                get_time(text)
            elif 'mở google và tìm kiếm' in text:
                open_google_and_search(text)
            elif "mở " in text:
                open_website(text)
            elif "ứng dụng" in text:
                speak("Tên ứng dụng bạn muốn mở là ")
                time.sleep(3)
                text1 = get_text()
                open_application(text1)
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
                time.sleep(2)

assistant()