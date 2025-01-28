from agentFramework import BaseAgent

import random

def get_random_message(messages):
    return random.choice(messages)

class InsultBot(BaseAgent):
    def perform_action(self):
        list = [
            "You're doing great!",
            "Keep up the good work!",
            "You're awesome!",
            "Believe in yourself!",
            "Stay positive and happy!",
            "You are amazing just the way you are!",
            "Keep smiling, the world needs your light!"
        ]
        message = get_random_message(list)
        self.mc.postToChat(message)