#include <WiFi.h>
#include <WiFiClientSecure.h>
#include <PubSubClient.h>

// ----------------------------------
//  CONFIG Wi-Fi (Wokwi)
// ----------------------------------
const char* ssid = "Wokwi-GUEST";
const char* password = "";

// ----------------------------------
//  CONFIG HiveMQ Cloud
// ----------------------------------
const char* HIVEMQ_HOST = "4d6e4976cb0b43778701600649659302.s1.eu.hivemq.cloud";
const int   HIVEMQ_PORT = 8883;  // TLS
const char* HIVEMQ_USERNAME = "adminuser";
const char* HIVEMQ_PASSWORD = "Admin123456";

// ----------------------------------
//  MQTT
// ----------------------------------
WiFiClientSecure espClient;  // cliente TLS
PubSubClient client(espClient);

// Pinos
int led = 5;
int buzzer = 4;

// ----------------------------------
//  CALLBACK MQTT
// ----------------------------------
void callback(char* topic, byte* payload, unsigned int length) {
  String msg;
  for (unsigned int i = 0; i < length; i++)
    msg += (char)payload[i];

  Serial.print("Mensagem recebida: ");
  Serial.println(msg);

  if (msg == "ON") {
    digitalWrite(led, HIGH);
    tone(buzzer, 1000);
    delay(1500);
    noTone(buzzer);
    digitalWrite(led, LOW);
  } 
  else if (msg == "OFF") {
    digitalWrite(led, LOW);
    noTone(buzzer);
  }
}

// ----------------------------------
//  RECONNECT MQTT
// ----------------------------------
void reconnect() {
  while (!client.connected()) {
    Serial.println("Conectando MQTT (HiveMQ Cloud TLS)...");

    if (client.connect("ESP32-UNIFORME", HIVEMQ_USERNAME, HIVEMQ_PASSWORD)) {
      Serial.println("MQTT conectado!");
      client.subscribe("iot/uniforme/led");
      client.subscribe("iot/uniforme/buzzer");
    } else {
      Serial.print("Falha, rc=");
      Serial.print(client.state());
      Serial.println(" tentando novamente em 2s");
      delay(2000);
    }
  }
}

// ----------------------------------
//  SETUP
// ----------------------------------
void setup() {
  Serial.begin(115200);
  pinMode(led, OUTPUT);
  pinMode(buzzer, OUTPUT);

  Serial.println("Conectando ao Wi-Fi...");
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  Serial.println("\nWi-Fi conectado!");

  // Aceita qualquer certificado — necessário no Wokwi
  espClient.setInsecure();

  client.setServer(HIVEMQ_HOST, HIVEMQ_PORT);
  client.setCallback(callback);

  Serial.println("Cliente MQTT seguro (TLS) configurado para HiveMQ Cloud.");
}

// ----------------------------------
//  LOOP
// ----------------------------------
void loop() {
  if (!client.connected()) {
    reconnect();
  }
  client.loop();
}
