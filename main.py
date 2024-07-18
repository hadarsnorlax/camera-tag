import os
import constants
from src.profile_loader import encode_faces
from src.profile_recognition import recognize_face

if __name__ == "__main__":
    encode_faces()
    tag_image_name = ""
    tag_image_path = os.path.join(constants.PROJECT_ROOT, "images/tag_game/{}")
    tagged_person = recognize_face(tag_image_path)
    print(f"Person tagged: {tagged_person}")
