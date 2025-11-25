# backend/main.py

import time
from detector.camera_auto import iniciar_camera, capturar_frame
from detector.uniform_detector import verificar_uniforme
from detector.whatsapp import enviar_alerta
from mqtt.client_mqtt import client, acionar_led_buzzer

cap = iniciar_camera()

def loop_principal():
    try:
        while True:
            frame = capturar_frame(cap)
            uniforme = verificar_uniforme(frame)
            if not uniforme:
                print("⚠️ Pessoa sem uniforme detectada!")
                acionar_led_buzzer("ON")
                enviar_alerta("⚠️ Pessoa sem uniforme detectada!")
            else:
                print("✅ Pessoa com uniforme")
                acionar_led_buzzer("OFF")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\nPrograma interrompido pelo usuário.")
    finally:
        if cap:
            cap.release()
        try:
            client.disconnect()
            client.loop_stop()
            print("MQTT desconectado com sucesso.")
        except:
            pass

if __name__ == "__main__":
    loop_principal()
