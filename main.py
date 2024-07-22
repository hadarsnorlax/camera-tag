import os
import constants
from src.profile_loader import encode_faces
from src.face_recognition import recognize_face
from src.recognition_display import display_recognition

if __name__ == "__main__":
    # encode_faces()
    tag_image_name = "bibi_2.jpeg"
    tag_image_path = os.path.join(constants.PROJECT_ROOT, f"images/tag_game/{tag_image_name}")
    tagged_person = recognize_face(tag_image_path)
    print(f"Person tagged: {tagged_person}")
    display_recognition(tag_image_path, tagged_person)
