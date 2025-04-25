def give_feedback(landmarks):
    feedback = []

    # Get needed landmarks
    left_elbow = landmarks.landmark[13]
    right_elbow = landmarks.landmark[14]
    left_knee = landmarks.landmark[25]
    right_knee = landmarks.landmark[26]
    left_hip = landmarks.landmark[23]
    right_hip = landmarks.landmark[24]
    right_shoulder = landmarks.landmark[12]  # ✅ FIXED LINE

    # Example: Are knees bent enough?
    avg_knee_y = (left_knee.y + right_knee.y) / 2
    avg_hip_y = (left_hip.y + right_hip.y) / 2

    if avg_knee_y < avg_hip_y - 0.1:
        feedback.append("Good knee bend 👍")
    else:
        feedback.append("Try bending your knees more 🦵")

    # Example: Is back elbow high enough? (common cricket stance issue)
    if right_elbow.y < right_shoulder.y - 0.05:
        feedback.append("Great! Back elbow is up 🏏")
    else:
        feedback.append("Try raising your back elbow a bit 🏏")

    return feedback
