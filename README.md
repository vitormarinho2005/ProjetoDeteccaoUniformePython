# Sistema de Detecção de Uniformes com IoT, MQTT, ESP32 e WhatsApp

Este projeto integra Visão Computacional, IoT e Comunicação em Tempo Real para detectar automaticamente pessoas **com ou sem uniforme**, acionar alarmes via **ESP32**, enviar mensagens via **WhatsApp (CallMeBot)** e exibir tudo em um **Dashboard Web**.

A arquitetura final é modular, profissional e fácil de manter.

---

## ✅ 1. Arquitetura Geral

Webcam → Python (detector) → MQTT → ESP32 (LED + buzzer)
↓
WhatsApp (CallMeBot)
↓
Dashboard Web (Flask)


---

## ✅ 2. Funcionalidades

- Detecção de uniforme pela cor (azul)
- Identificação automática da webcam
- Envio de alerta via MQTT para o ESP32
- Acionamento de LED e buzzer
- Envio automático de mensagem via WhatsApp
- Dashboard Web em Flask exibindo contagem
- Código totalmente modularizado

---

## ✅ 3. Requisitos de Sistema

Instale as dependências:

pip install -r requirements.txt


---

## ✅ 4. Estrutura do Projeto

projeto-uniforme-iot/
│
├── backend/
│ ├── detector/
│ │ ├── camera_auto.py
│ │ ├── uniform_detector.py
│ │ └── whatsapp.py
│ │
│ ├── mqtt/
│ │ └── client_mqtt.py
│ │
│ ├── web/
│ │ ├── app.py
│ │ ├── templates/
│ │ │ └── index.html
│ │ └── static/
│ │ └── style.css
│ │
│ └── main.py
│
├── esp32/
│ ├── esp32.ino
│ └── wokwi.json
│
├── requirements.txt
└── README.md


## ✅ 5. Como Rodar o Projeto

### 5.1 Backend (detector + MQTT + WhatsApp)

python backend/main.py

### 5.2 Dashboard Web

python backend/web/app.py

### 5.3 ESP32
Abra o Wokwi, carregue:
- esp32.ino  
- wokwi.json  

Simule e veja o LED e buzzer reagirem.

---

## ✅ 6. Configuração do WhatsApp (CallMeBot)

1) Adicione o número:

+34 644 52 89 81 (exemplo)

2) Envie:

I allow callmebot to send me messages

3) Você receberá seu API KEY.

4) Coloque dentro de:

backend/detector/whatsapp.py

---

## ✅ 7. Fluxo Completo

1. Python detecta azul (uniforme).
2. Se não houver, envia:
   - MQTT → ESP32 aciona alarme
   - WhatsApp → mensagem automática
3. Dashboard exibe contagem em tempo real.

---

## ✅ 8. Créditos

Projeto desenvolvido para fins educacionais e aplicação prática em IoT, Visão Computacional e Sistemas Embarcados.
