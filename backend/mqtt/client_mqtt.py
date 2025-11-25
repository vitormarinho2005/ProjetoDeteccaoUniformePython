# backend/mqtt/client_mqtt.py

import paho.mqtt.client as mqtt
import ssl

# ---------------------------------------------------------
# CONFIGURAÇÃO DO HIVEMQ CLOUD
# ---------------------------------------------------------
broker = "4d6e4976cb0b43778701600649659302.s1.eu.hivemq.cloud"   # exemplo: a1b2c3d4e5f6.s1.eu.hivemq.cloud
port = 8883                                 # HiveMQ Cloud ALWAYS uses 8883 (TLS)
username = "adminuser"
password = "Admin123456"
client_id = "UniformeClient"

# Cria o cliente MQTT
client = mqtt.Client(client_id)

# Ativa autenticação
client.username_pw_set(username, password)

# Ativa TLS (OBRIGATÓRIO NO HIVEMQ CLOUD)
client.tls_set(
    cert_reqs=ssl.CERT_REQUIRED,
    tls_version=ssl.PROTOCOL_TLSv1_2,
)

client.tls_insecure_set(False)

# ---------------------------------------------------------
# CALLBACKS PARA VALIDAR A CONEXÃO
# ---------------------------------------------------------
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Conectado ao HiveMQ Cloud com sucesso!")
    else:
        print(f"❌ Falha ao conectar. Código RC = {rc}")

def on_disconnect(client, userdata, rc):
    print(f"⚠️ Desconectado. Código RC = {rc}")

def on_publish(client, userdata, mid):
    print(f"📤 Mensagem publicada (ID={mid})")

# Associa os callbacks
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_publish = on_publish

# ---------------------------------------------------------
# Função para acionar LED e buzzer
# ---------------------------------------------------------
def acionar_led_buzzer(estado):
    if estado == "ON":
        client.publish("iot/uniforme/led", "ON")
        client.publish("iot/uniforme/buzzer", "ON")
    else:
        client.publish("iot/uniforme/led", "OFF")
        client.publish("iot/uniforme/buzzer", "OFF")

# ---------------------------------------------------------
# TENTAR CONECTAR
# ---------------------------------------------------------
try:
    print("🔌 Tentando conectar ao HiveMQ Cloud...")
    client.connect(broker, port)
    client.loop_start()   # permite processar mensagens em segundo plano
except Exception as e:
    print(f"❌ Erro ao conectar: {e}")

