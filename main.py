'''
请选择在光源充足的情况下运行该程序
'''
import time,cv2
from hand import handDetector as hd

cap,dt,t=cv2.VideoCapture(0),hd(),0

while cap.isOpened():
    ret,frame=cap.read()
    if dt.findHands(frame):
        list=dt.findPosition()
        a=dt.findDistance(1,4)
        cv2.line(frame, list[1][1:], list[4][1:], (255, 255, 255), 2)
        b=dt.findDistance(1,8)
        cv2.line(frame, list[1][1:], list[8][1:], (255, 255, 255), 2)
        c=dt.findDistance(4,8)#计算食指和拇指两个指头间的距离
        angle=dt.angle(a,b,c)
        print('食指与拇指间的角度: %3.1f度'%(angle))
    else:
    	print('未检测到手')
    now = time.time()
    fps = 1/(now-t)
    t = now
    cv2.putText(frame, str(int(fps))+'FPS', (10, 70), cv2.FONT_HERSHEY_PLAIN, 3,(0, 0, 0), 3) # 显示帧率
    cv2.imshow('Hand detector',frame)
    #按下Q退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()