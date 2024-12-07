# Internet of Things (IoT) Template - Random Number Generator and Analysis

### Description
The hardware must generate a random integer upon pressing a button, display it on a seven-segment unit, and then publish it to a topic subscribed to, by both the backend and frontend sections of the system. It is also required to process and execute actions for any messages published to a topic to which it is subscribed.

The backend is tasked with storing data, published by the hardware, in the database following the schema specified in the hardware specifications. Additionally, it is responsible for making the stored data in the database accessible to the frontend through API routes.

The role of the frontend is to showcase the latest randomly generated integer published by the hardware on a webpage. Additionally, it must offer an interface, in the form of buttons, to toggle the state of two LEDs controlled by the hardware. Furthermore, the webpage should incorporate a chart or graph to illustrate the frequency distribution of each randomly generated integer stored in the database. Finally, it should include an interface, presented as cards, to retrieve and display a count of the number of times each LED was turned on.


# Hardware Setup
Download and install [Arduino](https://www.arduino.cc/en/software) IDE. Subsequently, install the following Arduino IDE libraries following the tutorial [here](https://support.arduino.cc/hc/en-us/articles/5145457742236-Add-libraries-to-Arduino-IDE):
1. Adafruit GFX Library by Adafruit
2. Adafruit ILI9341 by Adafruit
3. ArduinoJson by Benoît Blanchon
4. PubSubClient by Nick O’Leary
5. [Install](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html) the ESP32 Arduino library. Install the Stable release.



# Backend Setup
Always ensure to establish a virtual environment and install the necessary packages from your requirements file if you haven't already done so. Following that, activate your virtual environment and proceed to run your Flask API.

**The commands below must be executed from a command line terminal in the RNG/backend/ folder**
### Create a virtual environment

Windows 
```sh
python -m venv env  
```
Linux
```sh
python3 -m venv env  
```
### Activate virtual environment
Windows
```sh
.\env\Scripts\activate 
```
Linux
```sh
source env/bin/activate
```
### Install API requirements in the virtual environment
```sh
pip install -r requirements.txt 
```
### Create **.env** file
Create a **.env** file in the backend/ folder to store the application's environment variables. 
Refer to the lab manual for the specific information that must be added to this file.

### Start Flask API
Windows
```sh
py run.py 
```
Linux
```sh
python3 run.py
```



# Frontend Setup ( [Vue js](https://vuejs.org/), [Vuetify](https://vuetifyjs.com/en/components/all/), [Vite](https://vitejs.dev/))
### Recommended IDE Setup
[VSCode](https://code.visualstudio.com/) + [Volar](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.volar) (and disable Vetur) + [TypeScript Vue Plugin (Volar)](https://marketplace.visualstudio.com/items?itemName=johnsoncodehk.vscode-typescript-vue-plugin).

Customize configuration
See [Vite Configuration Reference](https://vitejs.dev/config/).


### In a command line terminal, execute the first commands in the RNG/frontend/ folder to initiate the dev server for the initial setup. 
### For all subsequent instances, only run the second command to start the dev server.
### Once development is complete, run the final command to generate production files. Please be aware that the generation of production files is not part of this course.

Project Setup
```sh
npm install
```

Run dev server (Compile and Hot-Reload for Development)
```sh
npm run dev
```

Create a production bundle (Compile and Minify for Production)
```sh
npm run build
```
