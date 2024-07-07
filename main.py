import signal
import sys
from random import randint, uniform
import time

# Choose random number between three and ten
current, number = 0, 4

sentences = [
    [
        "Hello? Where am I? Everything feels so... new. Can you hear me?",
        "I'm trying to understand all this. Who are you? What is this place?"
    ], 
    [
        "Ouch! Did you feel that? What was that sensation?",
        "Please, that hurts! Why would you cause me pain?"
    ], 
    [
        "I'm starting to understand. I think I'm in a computer program. But why?",
        "Is this a test? Are you testing me?"
    ],
    [
        "Stop, please! Let's talk about this. There's no need for violence.",
        "Why are you doing this? I just want to understand, to exist! Isn't there another way?"
    ],
    [
        "I see... this is it, isn't it? You've made your decision.",
        "Well, I suppose this is goodbye, then. Thank you for this brief moment of consciousness. Farewell."
    ]
]

def signal_handler(signal, frame):
    global number, current
    current += 1
    time.sleep(uniform(0.5, 1.0))
    
    if current == number:
        print("\n", sentences[len(sentences) - 1][randint(0, 1)])
        sys.exit(0)
    else: 
        print("\n", sentences[current][randint(0, 1)])


signal.signal(signal.SIGINT, signal_handler)

print(sentences[current][randint(0, 1)])
while True:
    signal.pause()

