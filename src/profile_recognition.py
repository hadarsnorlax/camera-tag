import cv2
import pickle
import face_recognition

import constants

def recognize_face(new_image_path):
    try:
        known_encodings = None
        known_names = None

        with open(constants.ENCODINGS_PATH, "rb") as f:
            known_encodings, known_names = pickle.load(f)

        new_image = face_recognition.load_image_file(new_image_path)
        new_encodings = face_recognition.face_encodings(new_image)

        if not new_encodings:
            print("No faces found in the image")
            return None

        for new_encoding in new_encodings:
            matches = face_recognition.compare_faces(known_encodings, new_encoding)
            if True in matches:
                matched_idx = matches.index(True)
                person_name = known_names[matched_idx]
                print(f"Person recognized: {person_name}")
                return person_name
            else:
                print("Person not recognized")
                return None
    except Exception as err:
        print(f"Error in face recognition: {err}")
