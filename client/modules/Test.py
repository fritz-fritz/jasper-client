import re

WORDS = ["TEST"]

def handle(text, mic, profile):
    mic.say("Say something to test the A.P.I. I will then say it 
back")
    other = mic.activeListen(NATIVE=False)
    mic.say(other)

def isValid(text):
    return bool(re.search(r'\btest\b', text, re.IGNORECASE))

