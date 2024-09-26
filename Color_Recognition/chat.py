import cv2

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1288)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 780)

while True:
    _, frame = cap.read()
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    cx = int(width / 2)
    cy = int(height / 2)

    pixel_center = hsv_frame[cy, cx]
    hsv_value = pixel_center[0]
    color = "Undefined"
    
    if hsv_value < 10 or hsv_value > 180:  # Red
        color = "RED"
    elif 5 <= hsv_value < 22:  # Orange
        color = "ORANGE"
    elif 22 <= hsv_value < 40:  # Yellow
        color = "YELLOW"
    elif 33 <= hsv_value < 100:  # Green
        color = "GREEN"
    elif 78 <= hsv_value < 130:  # Blue
        color = "BLUE"
    elif 131 <= hsv_value < 160:  # Violet
        color = "VIOLET"
    elif hsv_value >= 170:  # Red (wrap around for hues near 180)
        color = "RED"
        
    # Add detection for black and white
    elif 0 <= hsv_value <= 10:  # Black
        color = "BLACK"
    elif 0 <= hsv_value <= 180 and 0 <= hsv_frame[cy, cx, 1] <= 10:  # White
        color = "WHITE"

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    cv2.putText(frame, color, (660, 360), cv2.FONT_HERSHEY_SIMPLEX, 2, (b, g, r), 2)
    cv2.circle(frame, (cx, cy), 5, (255, 0, 0), 3)
    print(pixel_center)
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
