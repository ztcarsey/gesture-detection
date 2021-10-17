import cv2,math,mediapipe as mp

class handDetector():
    def __init__(self, mode=False, maxHands=1, detectionCon=0.8, trackCon=0.8):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
    #寻找手部关键点
    def findHands(self, img):
        self.img=img
        imgRGB = cv2.cvtColor(self.img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if not self.results.multi_hand_landmarks:
            return False
        return True
    #手部关键点坐标列表
    def findPosition(self):
        self.list = []
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                for id, lm in enumerate(handLms.landmark):
                    h, w, c = self.img.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    self.list.append([id, cx, cy])
        return self.list
    #关键点p1,p2距离
    def findDistance(self, p1, p2):
        x1, y1 = self.list[p1][1:]
        x2, y2 = self.list[p2][1:]
        length = math.hypot(x2 - x1, y2 - y1)
        return length
    #夹角
    def angle(self,lena,lenb,lenc):
        return round(math.acos((lena*lena+lenb*lenb-lenc*lenc)/(2*lena*lenb))*180/math.pi,1)