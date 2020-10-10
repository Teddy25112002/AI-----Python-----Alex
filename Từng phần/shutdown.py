def shutdown():  
    h = int(input("Nhập giờ: "))
    m = int(input("Nhập phút: "))
    s = int(input("Nhập giây: "))
    while True:
        t = input("Mời bạn chọn chế độ (ShutDown = s, Restart = r ): ")
        if t == "s" or t == "r":
            break  
        
    h = h*60*60
    m = m*60 
    s = s+m+h  
    print("Bắt đầu hẹn giờ")
    os.system(f"ShutDown -{t} -t {s}") # Lệnh thực hiện dòng lệnh
    print("Gõ lệnh ShutDown -a để hủy hẹn giờ")
    speak("Nhớ tắt hết ứng dụng trước khi tắt máy nhoa, ihihi ^^")
    time.sleep(2)
