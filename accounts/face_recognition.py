import face_recognition
import base64
import numpy as np
import cv2


def verify_face(profile_photo_path, image_data):

    try:
        # Base64 image decode
        image_data = image_data.split(",")[1]
        image_bytes = base64.b64decode(image_data)

        np_image = np.frombuffer(image_bytes, np.uint8)
        captured_image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)

        captured_rgb = cv2.cvtColor(captured_image, cv2.COLOR_BGR2RGB)

        # Load registered profile photo
        profile_image = face_recognition.load_image_file(profile_photo_path)

        profile_encodings = face_recognition.face_encodings(profile_image)
        captured_encodings = face_recognition.face_encodings(captured_rgb)
        print("Profile Faces:", len(profile_encodings))
        print("Captured Faces:", len(captured_encodings))

        if len(profile_encodings) == 0:
            return False, "No face found in profile photo."

        if len(captured_encodings) == 0:
            return False, "No face detected."

        profile_encoding = profile_encodings[0]
        captured_encoding = captured_encodings[0]

        match = face_recognition.compare_faces(
            [profile_encoding],
            captured_encoding,
            tolerance=0.45
        )

        distance = face_recognition.face_distance(
            [profile_encoding],
            captured_encoding
        )[0]

        print("Face Distance:", distance)
        print("Matched:", match)

        if match[0]:
            return True, "Face Matched"

        return False, "Face Not Matched"

    except Exception as e:
        print(e)
        return False, str(e)