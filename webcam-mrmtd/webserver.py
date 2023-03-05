import cv2
from PIL import Image
from six import StringIO
import requests

#https://www.kirupa.com/html5/accessing_your_webcam_in_html5.htm

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()

    cv2.imshow('frame', frame)
    if cv2.waitKey(1) and 0xFF == ord('q'):

        frame_im = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        pil_im = Image.fromarray(frame_im)
        stream = StringIO()
        pil_im.save(stream, format="JPEG")
        stream.seek(0)
        img_for_post = stream.read()    
        files = {'image': img_for_post}
        response = requests.post(
            url='http://127.0.0.1:1337/mjpeg_stream',
            files=files
        )

        break

cap.release()
cv2.destroyAllWindows()