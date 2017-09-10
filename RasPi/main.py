import network
import requests
import sched, time

URL = "http://localhost/switch.php"
devicesTurnedOn = False

#Timer
s = sched.scheduler(time.time, time.sleep)

#Speicher der Daten
status = [3,0,0]

def loop():
	print("Loop runs again ...")
        userIstAnwesend = network.recognize()

        if userIstAnwesend == 1:
		print("User ist da")
		if not devicesTurnedOn:

			#Steckdosen abschalten
	                turnAllOn()
        else:
		print("User ist nicht da")
                if devicesTurnedOn:
			#Daten speichern
			saveStatus()

			#Steckdosen anschalten
                        turnAllOff()

	s.enter(5,1,loop,())

#Speichert die aktuelle Schalterconfig
def saveStatus():
	print("Daten speichern...")
	statusURL = "http://localhost/status_json.php"
	r = requests.get(url=statusURL, params={})
	dataSet = r.json()

	for i in range(3):
		status[i]=dataSet[i]["status"]



#Schaltet alle Schalter aus
def turnAllOff():
	global devicesTurnedOn

	print("Alle Stecker ausschalten")
	for i in range(3):
		parameter = {"id":str(i+1),"value":0}
		r = requests.get(url = URL, params = parameter)
	devicesTurnedOn = False


#Schaltet alle Schalter anhand der Werte in "Status" an
def turnAllOn():
	global devicesTurnedOn

	print("Alle Stecker anhand der Werte Anschalten")
	for i in range(3):
		parameter = {"id":str(i+1),"value":status[i]}
		r = requests.get(url = URL, params = parameter)
	devicesTurnedOn = True

#Erstellt den Timer
def setup():

	#Werte aus der DB speichern
	saveStatus()

	s.enter(5, 1, loop, ())
	s.run()

setup()
