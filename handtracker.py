#Import the cv2 and Mediapipe

import cv2
import mediapipe as mp
mp_drawing = mp.solutions.drawing_utils
mp_drawing_style = mp.solutions.drawing_styles
mphands = mp.solutions.hands

cap = cv2.VideoCapture(0)
hands = mphands.Hands()
while True:
    data, image = cap.read()
    #Flip the image
    image = cv2.cvtColor(cv2.flip(image,1),cv2.COLOR_BGR2RGB)
    #sorting the results
    results = hands.process(image)
    #print(results.multi_hand_landmarks)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(image,hand_landmarks,mphands.HAND_CONNECTIONS,mp_drawing_style.get_default_hand_landmarks_style(),mp_drawing_style.get_default_hand_connections_style())
    cv2.imshow("Hand Tracking",image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break