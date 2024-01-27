import urequests
from utime import sleep
# The URL to use to get updates, full path to the PHP script (Raspberry Pi IP Address). The update file must be in the same folder as the PHP script.
update_url = "http://172.30.252.XXX/get_ESP_data.php?file=program.py"
delete_url = "http://172.30.252.XXX/delete_ESP_data.php?file=program.py"


def check_for_updates(OTA):
    try:
        # print ('Checking for updates')
        response = urequests.get(update_url)
        x = response.text.find("FAIL")
        if x > 15:
            OTA = 1
            print('There is an update available')
            return (OTA)
        else:
            print('There are no updates available.')
            return (OTA)

    except:
        print('unable to reach internet')
        return (OTA)


def mainprog(OTA):
    print('Mainprog - OTA is' + str(OTA))
# Check if there is a file on the server, delete if so
    response = urequests.get(delete_url)
    print('Program start')
    while OTA == 0:
        program_tasks()
        OTA = check_for_updates(OTA)
        if OTA == 1:
            return (OTA)
        print('OTA = ' + str(OTA))


def program_tasks():
    # doe programma
    sleep(2)
    print('Tasks completed, entering loop 2')
    sleep(2)
    print('Tasks completed, entering loop 3')
    sleep(2)
    print('Tasks completed, entering loop 4')
    sleep(2)
    print('Tasks completed, entering loop 5')
    sleep(2)
    print('5 loops completed, checking for updates')
