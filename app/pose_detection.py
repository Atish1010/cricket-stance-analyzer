import cv2
import mediapipe as mp

mp_pose = mp.solutions.pose
pose = mp_pose.Pose(static_image_mode=True)
mp_drawing = mp.solutions.drawing_utils


def detect_pose(image_path):
    image = cv2.imread(image_path)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    results = pose.process(image_rgb)

    if not results.pose_landmarks:
        print("No pose detected.")
        return None

    # Draw landmarks
    annotated_image = image.copy()
    mp_drawing.draw_landmarks(
        annotated_image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

    # Show image
    cv2.imshow("Pose Detection", annotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return results.pose_landmarks
