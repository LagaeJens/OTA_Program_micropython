import program
import machine

# URLs for the updates
update_url = "http://172.30.252.125/get_ESP_data.php?file=program.py"


# change your wifi credentials here.
ssid = ''   # your wifi SSID
password = ''  # your wifi password


print('OTA is ' + str(OTA))  # debug

# here we set up the network connection
station = network.WLAN(network.STA_IF)
station.active(False)
station.active(True)

station.connect(ssid, password)

while station.isconnected() == False:
    pass

# print board local IP address
print(station.ifconfig())

if OTA == 0:
    print('starting program')
    OTA = program.mainprog(OTA)

# mainprog() is the starting function for my program. OTA is set to 0 on boot so the first time this code
# is run, it sets up the network connection and then runs the program.
# The following code only runs when program.py exits with OTA = 1

if OTA == 1:
    print('Downloading update')
    # download the update and overwrite program.py
    response = requests.get(update_url)
    x = response.text.find("FAIL")
    if x > 15:
        # download twice and compare for security
        x = response.text
        response = requests.get(upd_url)
        if response.text == x:
            f = open("program.py", "w")
            f.write(response.text)
            f.flush()
            f.close

            # soft reboot
            print('reboot now')
            machine.deepsleep(5000)
