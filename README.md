# login-pushover

Simple script to send a mobile notification using Pushover when a user logs into a Linux machine.

This is by no means a secure way of knowing a user has logged into a system. I created this just to get a brief idea who and when someone was logging into one of my Linux boxes.

### Dependencies

- CentOS/Ubuntu/RedHat/Debian machine
- Python 2.6+
- Python requests, getpass & socket
- A [Pushover](https://pushover.net/) account

### Install

1. You'll need to grab yourself a copy of the code using `git clone git@github.com:davidmaitland/login-pushover.git`
2. Then you'll need to copy the files into some directories on your system as root
```
sudo cp login-pushover/login-pushover.sh /etc/profile.d/ && sudo cp login-pushover/login-pushover.py /usr/local/bin/
```

3. Edit the `/usr/local/bin/login-pushover.py` file and add your Pushover API keys
4. All done! Try and login to your machine and you should get a message pushed to your mobile device!
