# backend/detector/whatsapp.py

import requests
import urllib.parse

PHONE_NUMBER = "554884641072"
API_KEY = "2411351"

def enviar_alerta(mensagem):
    mensagem_codificada = urllib.parse.quote(mensagem)
    url = (
        f"https://api.callmebot.com/whatsapp.php?"
        f"phone={PHONE_NUMBER}&"
        f"text={mensagem_codificada}&"
        f"apikey={API_KEY}"
    )
    try:
        resposta = requests.get(url, timeout=2)

        if resposta.status_code == 200:
            print("WhatsApp enviado com sucesso:", mensagem)
        else:
            print(f"Erro ao enviar WhatsApp (HTTP {resposta.status_code})")

    except Exception as erro:
        print("Falha ao enviar WhatsApp:", erro)
