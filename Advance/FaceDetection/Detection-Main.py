import cv2
import numpy
import PIL
import datetime

# Uncomment the function below and use haarcascade classifier to capture the faces, then annotate them using open-cv



# def Face_Cascade(frame):
    # face_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'')  # Add link to haarcascade file
    # gray =                                                        # Convert the image
    # faces =                                                       # Use DetectMultiScale method to capture faces
    # times=[]
    # for (x,y,w,h) in faces:
    #     img =                                                     # Annotate the faces
    #     roi_gray = gray[y:y+h, x:x+w]
    #     roi_color = frame[y:y+h, x:x+w]




if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('StudentName+TestId.avi', fourcc, 20.0, (640, 480))
    print(cap.isOpened())
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            # Face_Cascade(frame)
            out.write(frame)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            pass
    cap.release()
    out.release()
    cv2.destroyAllWindows()
