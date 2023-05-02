import datetime
import time,DAN
import cv2
from paz.applications import HaarCascadeFrontalFace, MiniXceptionFER
import paz.processors as pr
import pygame

pygame.init()
pygame.mixer.init()

ServerURL = 'https://7.iottalk.tw'
mac_addr = 'hsuuu'
Reg_addr = 'hsuuu_emotion'
DAN.profile['dm_name'] = 'emotion'
DAN.profile['df_list'] = ['emotion','emotion-o']
DAN.profile['d_name']  = 'emotion2'
DAN.device_registration_with_retry(ServerURL, Reg_addr)

happy = 0
sad = 0
angry = 0
disgust = 0 
surprise = 0
fear = 0

class EmotionDetector(pr.Processor):
    def __init__(self):
        super(EmotionDetector, self).__init__()
        self.detect = HaarCascadeFrontalFace(draw=False)
        self.crop = pr.CropBoxes2D()
        self.classify = MiniXceptionFER()
        self.draw = pr.DrawBoxes2D(self.classify.class_names)

    def call(self, image):
        boxes2D = self.detect(image)['boxes2D']
        cropped_images = self.crop(image, boxes2D)
        for cropped_image, box2D in zip(cropped_images, boxes2D):
            box2D.class_name = self.classify(cropped_image)['class_name']
        output_image = self.draw(image, boxes2D)
        return {'image': output_image, 'boxes2D': boxes2D}

def reset_emotion():
    global happy
    global sad
    global angry
    global disgust
    global surprise
    global fear
    happy = 0
    sad = 0
    angry = 0
    disgust = 0 
    surprise = 0
    fear = 0


if __name__ == "__main__":
    # 初始化攝像頭
    cap = cv2.VideoCapture(0)

    # 檢查攝像頭是否成功打開
    if not cap.isOpened():
        print("無法打開攝像頭")

    # 創建表情檢測器實例
    emotion_detector = EmotionDetector()

    last_print_time = time.time()
    try:
        while True:
            # 從攝像頭讀取一幀圖像
            ret, frame = cap.read()
            if not ret:
                print("無法讀取攝像頭數據")
                break

            # 使用表情檢測器處理圖像
            result = emotion_detector(frame)

            # 顯示處理後的圖像
            cv2.imshow('Emotion Detection', result['image'])
            cv2.waitKey(1)

            current_time = time.time()
            # 打印檢測到的表情結果
            if current_time - last_print_time > 1:
                for box2D in result['boxes2D']:
                    print("表情結果：", box2D.class_name)
                    DAN.push('emotion', [box2D.class_name])
                
                emo = DAN.pull('emotion-o')
                if emo == ['happy']:
                    print(happy)
                    happy = happy + 1
                elif emo == ['surprise']:
                    surprise = surprise + 1
                elif emo == ['angry']:
                    print(angry)
                    angry = angry + 1
                elif emo == ['sad']:
                    sad = sad + 1
                elif emo == ['disgust']:
                    disgust = disgust + 1
                elif emo == ['fear']:
                    fear = fear + 1
                
                if happy >= 5:
                    reset_emotion()
                    pygame.mixer.music.load("happy.mp3")
                    pygame.mixer.music.play()
                    
                elif surprise >= 5:
                    pygame.mixer.music.load("surprise.mp3")
                    pygame.mixer.music.play()
                    reset_emotion()
                elif angry >= 5:
                    pygame.mixer.music.load("angry.mp3")
                    pygame.mixer.music.play()
                    reset_emotion()
                elif sad >= 5:
                    pygame.mixer.music.load("sad.mp3")
                    pygame.mixer.music.play()
                    reset_emotion()
                elif disgust >= 5:
                    pygame.mixer.music.load("disgust.mp3")
                    pygame.mixer.music.play()
                    reset_emotion()
                elif fear >= 5:
                    pygame.mixer.music.load("fear.mp3")
                    pygame.mixer.music.play()
                    reset_emotion()
                
                last_print_time = current_time
            

    finally:
        # 釋放資源並關閉窗口
        cap.release()
        cv2.destroyAllWindows()