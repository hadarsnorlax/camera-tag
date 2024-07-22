import cv2
import face_recognition

def display_recognition(tag_image_path, recognized_person):
    try:
        image = cv2.imread(tag_image_path)
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)
        
        if not face_encodings:
            print("No faces found in the image")
            return None
        
        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            matches = face_recognition.compare_faces([face_encoding], face_encoding)
            if True in matches:
                # Draw a box around the face
                cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 2)
                # Label the face
                cv2.putText(image, recognized_person, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                
        cv2.imshow("Tagged Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except Exception as err:
        print(f"Error in displaying recognition: {err}")
