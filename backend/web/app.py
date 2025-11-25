import sys
import os

# Adiciona automaticamente a pasta 'backend' ao sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.abspath(os.path.join(current_dir, ".."))
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

from flask import Flask, render_template
from detector.camera_auto import iniciar_camera, capturar_frame
from detector.uniform_detector import verificar_uniforme

app = Flask(__name__)
cap = iniciar_camera()

@app.route("/")
def index():
    pessoas = []
    for i in range(10):
        frame = capturar_frame(cap)
        uniforme = verificar_uniforme(frame)
        pessoas.append({"id": i, "uniforme": uniforme})
    com_uniforme = sum(1 for p in pessoas if p["uniforme"])
    sem_uniforme = len(pessoas) - com_uniforme
    return render_template("index.html", pessoas=pessoas,
                           com_uniforme=com_uniforme, sem_uniforme=sem_uniforme)

if __name__ == "__main__":
    app.run(debug=True)
