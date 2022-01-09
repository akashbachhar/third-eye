# Third Eye
This project is built for DotSlash 5.0 Hackathon :)
## Problem Statement

According to a study by the Central Road Research Institute (CRRI), 21% of all fatal accidents are due to drowsy
driving. It's a serious issue and most people that have driven for long hours at night can relate to the fact that
fatigue and a slight brief state of unconsciousness can happen to anyone and everyone.

There are some of the existing car companies (BMW, Ford, Tesla, Honda, etc) that propose driver's distraction tracking
systems, but due to high costs, those are out of reach of ordinary people, say, for example, taxi drivers, cab drivers,
and people with a car that has minimum functionalities.

So, to reach the technology to everyone from an e-rickshaw driver to taxi driver I created "Third Eye", a deep learning
and Django-based website (and mobile application in the future) that detects the drowsiness of the driver in real-time
with the help of eye blinking and yawning of the driver. After detection in two different states, drowsing, and
sleeping, it will immediately sound an alarm.

Now, any driver can open the application, give the camera access, and put the mobile on the mobile holder in the car,
and be secure.

## Tech Stack

**Client:** HTML, CSS

**Server:** Python, Django

**Other Necessary Libraries:** 

* OpenCV
* dlib 
* imutils
* simpleaudio
* numpy

## Run Locally

Create a new directory 
```bash
  mkdir thirdeye
```

Create a virtual environment

```bash
  sudo apt-get install python3-venv
  python3 -m venv env
```
Clone the project

```bash
  git clone https://github.com/akashbachhar/third-eye
```

Activate the virtual environment

**Linux/Mac:**

```bash
  source env/bin/activate
```

**Windows:**

```bash
  .\Scripts\activate
```

Install the requirements

```bash
  cd thirdeye
  pip install -r requirements.txt
```

Run the migrations 

```bash
  python manage.py makemigrations
  python manage.py migrate
```

Run the Development Server 

```bash
  python manage.py runserver
```
Head to server http://127.0.0.1:8000/admin, and enjoy !
