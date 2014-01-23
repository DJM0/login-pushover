#!/usr/bin/env python

import socket, getpass, requests # Import required modules

host = socket.gethostname()
user = getpass.getuser()

apitoken = "" # Your Pushover application API token/key
apiuser = "" # Your Pushover user or delivery group API key

title = "System Login"
message = "User " + user + " just logged into " + host

def pushover(title, message):
  try:
    parameters = { 'token': apitoken, 'user': apiuser, 'message': message, 'title': title  }
    request = requests.post('https://api.pushover.net/1/messages.json', params=parameters, timeout=3)
  except:
    pass # Die silently

pushover(title, message) # Send notification