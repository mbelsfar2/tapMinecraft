from agentFramework import BaseAgent

import random

class InsultBot(BaseAgent):
    def __init__(self, address="localhost", port=4711):
        super().__init__(address, port)
        self.messages = [
            "You're doing great!",
            "Keep up the good work!",
            "You're awesome!",
            "Believe in yourself!",
            "Stay positive and happy!",
            "You are amazing just the way you are!",
            "Keep smiling, the world needs your light!"
        ]

    def perform_action(self):
        message = random.choice(self.messages)
        self.mc.postToChat(message)