from pose_detection import detect_pose
from feedback import give_feedback  # Import the feedback logic

if __name__ == "__main__":
    # Update this if your image name/path is different
    image_path = "images/stance1.jpg"
    landmarks = detect_pose(image_path)  # Run pose detection and get landmarks

    if landmarks:
        # Get feedback based on landmarks
        suggestions = give_feedback(landmarks)
        print("\n🏏 Batting Stance Feedback:")
        for line in suggestions:
            print("👉", line)
