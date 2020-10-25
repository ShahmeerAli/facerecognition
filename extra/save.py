import cv2
import os
import matplotlib.pyplot as plt
import test 

cap = cv2.VideoCapture(0)
# name = str(test.make_dir())
name = '0'

for i in range(1,10): # the range means the no. of pic to be saved
    ret, frame = cap.read()
    img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    plt.imshow(img)
    # plt.title('image 1')
    plt.xticks([])
    plt.yticks([])
    image = str(i)
    path = '/home/shahmir/Desktop/Face Detection/test/'  
    plt.savefig(path+ name+ '/'+ image)
    # plt.show()

    if cv2.waitKey(10) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows
