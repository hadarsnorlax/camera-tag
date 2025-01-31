import os
import pickle
import face_recognition

import constants

def encode_faces():
    known_encodings = []
    known_names = []

    try:
        for person_name in os.listdir(constants.PROFILE_IMAGES_DIR):
            if person_name != ".gitkeep":
                person_dir = os.path.join(constants.PROFILE_IMAGES_DIR, person_name)
                print(f"Reading profile of: {person_name}")

                for image_name in os.listdir(person_dir):
                    image_path = os.path.join(person_dir, image_name)
                    image = face_recognition.load_image_file(image_path)
                    encodings = face_recognition.face_encodings(image)

                    if encodings:
                        known_encodings.append(encodings[0])
                        known_names.append(person_name)
                        print(f"Reading image: {image_name}")

        with open(constants.ENCODINGS_PATH, "wb") as f:
            pickle.dump((known_encodings, known_names), f)
            print(f"Finish loading new profiles")
        
    except Exception as err:
        print(f"Error in loading profiles: {err}")
