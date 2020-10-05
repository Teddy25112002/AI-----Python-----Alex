def send_email(text):
    speak('Bạn gửi email cho ai nhỉ')
    recipient = get_text()
    if 'nghĩa' in recipient:
        speak('Nội dung bạn muốn gửi là gì')
        content = get_text()
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('xyz', 'abc') # Ở đây, 'xyz' là địa chỉ email của bạn, còn 'abc' là mật khẩu của email đó
        mail.sendmail('xyz',
                      '123', content.encode('utf-8')) # Chỗ 'xyz' là như bên trên, còn '123' là email bạn muốn gửi nha
        mail.close()
        speak('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
    else:
        speak('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?'