1. clone this repo


2. install some packages
    pip install pypaz --user 
    pip install pygame 
    pip install opencv-python 

3. IoTtalk

http://7.iottalk.tw:7788/connection
open project "try", password: 123

4. execute

python DAI.py

六個emotion，分別是happy、surprise、sad、angry、fear、disgust。每秒判斷一次情緒，若有一個情緒達到3次，會撥出相對應的音效。播完音效後，情緒數量會重製。 
如果不知道表情怎麼做可以問陳逸雲怎麼做相應的表情，他是表情大師
下禮拜我們會再試看看加新的功能。 

!!! [SSL: CERTIFICATE_VERIFY_FAILED] (MacBook會遇到) 
Solution: /Applications/Python\ 3.10/Install\ Certificates.command
