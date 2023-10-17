import cv2
import numpy
import PIL
import datetime

def Face_Cascade(frame):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml') # Load the Haar Cascade Classifier for face detection
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert the frame 
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5) # Use the detectMultiScale method to capture faces
    times = []
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2) # Annotate the faces by drawing rectangles
        
        cv2.putText(frame, f'Face: ({x}, {y})', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2) #text with coordinates on the detected face
        
        # extract the region of interest (ROI)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
    cv2.imshow('Annotated Frame', frame) # Display the frame
    return frame, faces




if __name__=='__main__':
    cap = cv2.VideoCapture(0)
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('StudentName+TestId.avi', fourcc, 20.0, (640, 480))
    print(cap.isOpened())
    while (cap.isOpened()):
        ret, frame = cap.read()
        if ret == True:
            Face_Cascade(frame)
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
