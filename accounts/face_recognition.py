import face_recognition
import base64
import numpy as np
import cv2
import requests


def verify_face(profile_photo_url, image_data):

    try:
        # ==========================================
        # 1. Cloudinary Profile Photo Download
        # ==========================================

        response = requests.get(
            profile_photo_url,
            timeout=15
        )

        if response.status_code != 200:
            return False, "Unable to load profile photo."

        profile_bytes = response.content

        profile_np = np.frombuffer(
            profile_bytes,
            np.uint8
        )

        profile_image = cv2.imdecode(
            profile_np,
            cv2.IMREAD_COLOR
        )

        if profile_image is None:
            return False, "Unable to read profile photo."

        profile_rgb = cv2.cvtColor(
            profile_image,
            cv2.COLOR_BGR2RGB
        )


        # ==========================================
        # 2. Decode Live Camera Image
        # ==========================================

        if "," in image_data:
            image_data = image_data.split(",", 1)[1]

        image_bytes = base64.b64decode(
            image_data
        )

        np_image = np.frombuffer(
            image_bytes,
            np.uint8
        )

        captured_image = cv2.imdecode(
            np_image,
            cv2.IMREAD_COLOR
        )

        if captured_image is None:
            return False, "Unable to read captured image."

        captured_rgb = cv2.cvtColor(
            captured_image,
            cv2.COLOR_BGR2RGB
        )


        # ==========================================
        # 3. Find Faces
        # ==========================================

        profile_encodings = face_recognition.face_encodings(
            profile_rgb
        )

        captured_encodings = face_recognition.face_encodings(
            captured_rgb
        )

        print(
            "Profile Faces:",
            len(profile_encodings)
        )

        print(
            "Captured Faces:",
            len(captured_encodings)
        )


        # ==========================================
        # 4. Check Profile Face
        # ==========================================

        if len(profile_encodings) == 0:

            return False, (
                "No face found in profile photo."
            )


        # ==========================================
        # 5. Check Camera Face
        # ==========================================

        if len(captured_encodings) == 0:

            return False, (
                "No face detected in camera."
            )


        # ==========================================
        # 6. Face Comparison
        # ==========================================

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


        print(
            "Face Distance:",
            distance
        )

        print(
            "Matched:",
            match
        )


        # ==========================================
        # 7. Final Result
        # ==========================================

        if match[0]:

            return True, "Face Matched"

        return False, "Face Not Matched"


    except Exception as e:

        print(
            "Face Verification Error:",
            e
        )

        return False, str(e)