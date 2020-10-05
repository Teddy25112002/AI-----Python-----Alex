def play_song():
	speak('Xin mời bạn chọn tên bài hát')
	mysong = get_text()
	while True:
		result = YoutubeSearch(mysong, max_results=10).to_dict()
		if result:
			break
	url = 'https://www.youtube.com' + result[0]['channel_link']
	webbrowser.open(url)
	speak("Bài hát bạn yêu cầu đã được mở.")