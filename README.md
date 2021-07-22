# arduino-real-time-music-player which is designed by SE Aaron and IEE Yazhu
本專題希望利用Arduino與各類型感測模組，
應用在音樂撥放上的演奏，透過雨滴的感測控制低音譜 ，
利用超音波的距離感測控制高音譜，再經由溫濕度控制 鼓聲 ，
而LCD可以顯示目前各模組的數值，不僅使用到Arduino還與Sonic跟Python結合，
因此各項數值和演奏的內容我們只要透過Python就得知，
甚至改變 演奏風格也能靠Python做得到。


材料列表：
Name	Type No.	Qty	Link
控制器	Arduino UNO	1	https://www.arduino.cc/

控制器	sonic pi	1	https://sonic-pi.net/

中間轉換器	python	1	
溫溼度	DHT11	1	
超音波	SR04	1	
LCD	1602	1	
Rain sensor	MH-RD	1	

電路圖：
![arduinoelectric](https://user-images.githubusercontent.com/67402409/126626649-a890aa66-b535-4eee-ba2c-c127c9ecb637.jpg)

SR-04	接腳	DHT-11	接腳
Vcc	5V	Out	2
Echo	13	VCC	5V
Trig	12	GND	GND
GND	GND		

LCD	接腳	MH-RD	接腳
SDA	A4	A0	A0
SCL	A5	VCC	5V
VCC	5V	GND	GND
GND	GND		

注意要點:
要開啟
  1.SoniPi  (不會有程式碼仍然要開)
  2.Python  
  3.Arduino 這三種軟體


Demostration:
https://www.youtube.com/watch?v=eyTs7e2O9MI

Arduino code:
![arduinocode](https://user-images.githubusercontent.com/67402409/126627303-afd63672-8e58-4165-a6b5-415b7345eafd.jpg)

map可以將大範圍數值調整到小範圍 像是0~1024調整成0~2
![arduinocode2](https://user-images.githubusercontent.com/67402409/126627408-20e9253c-a7a8-4be2-9284-a4b7533e4e2f.jpg)
![arduinocode3](https://user-images.githubusercontent.com/67402409/126627412-c8424280-7ecb-43fa-b513-840a1eb87ccf.jpg)
![arduinocode4](https://user-images.githubusercontent.com/67402409/126627417-45da83d2-2420-434e-a6f5-838417b117f6.jpg)

python code:
![pythoncode1](https://user-images.githubusercontent.com/67402409/126627447-33c41032-7500-4af2-80ed-885947123c2a.jpg)

藍色範圍為Python與Arduino的transmission to transmission
![pythoncode2](https://user-images.githubusercontent.com/67402409/126627516-8514648e-8fa2-4c25-9a65-81a7d717c628.jpg)

紅色範圍為sonic pi跟python的transmission to transmission
![pythoncode3](https://user-images.githubusercontent.com/67402409/126627594-bede2a80-07da-4c10-a441-1659ebdf411e.jpg)

ArduinoSerial.realine()為讀取Arduino裡面的值 再打一次ArduinoSerial.realine()則會讀取到Arduino下一個值
![pythoncode4](https://user-images.githubusercontent.com/67402409/126627602-c67eaf8a-2539-4890-882b-c4a7294f602d.jpg)
![pythoncode5](https://user-images.githubusercontent.com/67402409/126627618-399b807f-de8c-4cfc-afc8-a21eeaf5c32c.jpg)

1.cm 2.rain 3.humi分別為控制音樂的元素
假設只有rain達到播放條件 則只有鋼琴聲
假設只有cm達到播放條件 則只會有隨機電音
humi則是會增加一小段音樂

