import cv2

import cv2

def iniciar_camera():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Nenhuma câmera encontrada. Usando simulação.")
        return None
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
    return cap

def capturar_frame(cap):
    if cap:
        ret, frame = cap.read()
        if ret:
            return frame
    return None
