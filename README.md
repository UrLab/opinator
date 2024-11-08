This is the O.P.I.N.A.T.O.R. project, you can find info at https://urlab.be/projects/108

## Opinator
The opinator project is an ON/OFF switch button that sends "0" (close) or "1" (open) to a mqtt broker, which can be used to alert people that the hackerspace is open or closed, trigger the website, unlock the music servers in the Hackerspace, and any thing that can be done from the mqtt signal.

### Hardware
The hardware/ folder contains the code and information for the mqtt publisher, the switch part of the project.

Hardware :
 - An ESP8266Wifi
 - An ON/OFF switch
 - A Led
 - A resistor
 - Some cables
The cables.txt file contains the wiring for the hardware. Each line is a circuit.

The rest of the files contains the code for the switch part of the project, the mqtt publisher.

Software :
 - Platformio (cli pip version is enough)
 - A wifi.h file to locate in the src folder with the following :
```c
const char* WIFI_H_SSID = "<wifi ssid>";
const char* WIFI_H_PASSWORD = "<wifi password>";
const char* WIFI_H_MQTT_SERVER = "<mqtt broker server ip or hostname>";
```
 (Do not upload this file to the github repo as it contains your wifi credentials)

To build the project :

```bash
pio run -t upload
```
in root directory

## Software
The software/ folder contains the code for the mqtt subscribers, the chaotic part of the project.


