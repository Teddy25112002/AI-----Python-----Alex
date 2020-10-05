def change_wallpaper():
	api_key = 'RF3LyUUIyogjCpQwlf-zjzCf1JdvRwb--SLV6iCzOxw'
	url = 'https://api.unsplash.com/photos/random?client_id=' + \
		api_key # bạn chọn ảnh trên web api.unsplash.com để dễ thao tác với Alex nha
	f = urllib2.urlopen(url)
	json_string = f.read()
	f.close()
	parsed_json = json.loads(json_string)
	photo = parsed_json['urls']['full']
	# Đường dẫn vào tấm ảnh hồi nãy nha ^^
	urllib2.urlretrieve(photo, "C:/Users/PC/a.jpg")
	image=os.path.join("C:/Users/PC/a.jpg")
	ctypes.windll.user32.SystemParametersInfoW(20,0,image,3)
	speak('Hình nền máy tính vừa được thay đổi')