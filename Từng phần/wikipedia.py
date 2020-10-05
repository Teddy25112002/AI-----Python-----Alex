def tell_me_about():
	try:
		speak("Bạn muốn nghe về gì ạ")
		text = get_text()
		contents = wikipedia.summary(text).split('\n')
		speak(contents[0])
		time.sleep(10)
		for content in contents[1:]:
			speak("Bạn muốn nghe thêm không")
			ans = get_text()
			if "có" not in ans:
				break
			speak(content)
			time.sleep(10)

		speak('Cảm ơn bạn đã lắng nghe !!!')
	except:
		speak("Bot không định nghĩa được thuật ngữ của bạn. Xin mời bạn nói lại")