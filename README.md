1. clone this repo

2. install some packages
    pip install pypaz --user <br>
    pip install pygame <br>
    pip install opencv-python 

3. IoTtalk

    http://7.iottalk.tw:7788/connection
    open project "try", password: 123

    register a bulb by your own

4. execute <br>
    python DAI.py <br>
    register your emotion model
    
    六個emotion，分別是happy、sad、surprise、angry、disgust、fear。
    
    1. emotion音效: 每兩秒判斷一次情緒，若有一個情緒達到2次，會撥出相對應的音效。播完音效後，情緒數量會重置
    2. emotion轉換燈泡: 每兩秒判斷一次情緒，不同的情緒對應到不同的燈泡顏色。
    

> [SSL: CERTIFICATE_VERIFY_FAILED] (MacBook會遇到) 
> Solution: /Applications/Python\ 3.10/Install\ Certificates.command

