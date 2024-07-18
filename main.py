import os
import constants
from src.profile_loader import encode_faces
from src.profile_recognition import recognize_face

if __name__ == "__main__":
    encode_faces()
    tag_image_name = "curry_2.jpg"
    tag_image_path = os.path.join(constants.PROJECT_ROOT, f"images/tag_game/{tag_image_name}")
    tagged_person = recognize_face(tag_image_path)
    print(f"Person tagged: {tagged_person}")
