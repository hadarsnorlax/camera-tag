import os
import pickle
import face_recognition

import constants

PROFILE_IMAGES_DIR = os.path.join(constants.PROJECT_ROOT, "images/profiles")

def encode_faces():
    known_encodings = []
    known_names = []

    try:
        for person_name in os.listdir(PROFILE_IMAGES_DIR):
            person_dir = os.path.join(PROFILE_IMAGES_DIR, person_name)

            for image_name in os.listdir(person_dir):
                image_path = os.path.join(person_dir, image_name)
                image = face_recognition.load_image_file(image_path)
                encodings = face_recognition.face_encodings(image)

                if encodings:
                    known_encodings.append(encodings[0])
                    known_names.append(person_name)
                    print(f"Reading profile of: {person_name}")

        with open("face_encodings.pkl", "wb") as f:
            pickle.dump((known_encodings, known_names), f)
            print(f"Finish loading new profiles")
        
    except Exception as err:
        print("Error in loading profiles")
