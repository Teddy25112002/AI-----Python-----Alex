def read_news():
	speak("Bạn muốn đọc báo gì")

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
