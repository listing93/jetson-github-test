import cv2
import platform
from datetime import datetime

def main():
    print("OpenCV version:", cv2.__version__)
    print("Operating System:", platform.system())
    print("Machine:", platform.machine())

    camera_id = 0  
    cap = cv2.VideoCapture(camera_id)

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return
    
    print("Successful, Press 'q' to quit the camera feed.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            break
        
        text=f"Current date and time: {datetime.now()}"
        cv2.putText(frame, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        cv2.imshow('Camera test', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    print("Camera closed.")

if __name__ == "__main__":
    main()