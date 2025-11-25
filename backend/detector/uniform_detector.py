# backend/detector/uniform_detector.py

import numpy as np

def verificar_uniforme(frame):
    if frame is None:
        return True  # simulação
    media = np.mean(frame, axis=(0,1))
    return media[0] > 100  # azul predominante = uniforme

