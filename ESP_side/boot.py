try:
import network
from utime import sleep_ms
from utime import sleep
import gc
import usocket as socket
except:
  import socket

try:
  import urequests as requests
except:
  import requests
import os
import sys
import esp
esp.osdebug(None)
gc.collect()

OTA = 0
