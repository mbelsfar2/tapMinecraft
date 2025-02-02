from agentFramework import BaseAgent

import random

def get_random_message(messages):
    return random.choice(messages)

class InsultBot(BaseAgent):
    def perform_action(self):
            # Lista de mensajes
        list = [
            "¡Eres un desastre!",
            "¿Así que crees que eres alguien?",
            "No sabes lo que haces.",
            "Qué poca vergüenza.",
            "Eres un completo inútil.",
            "Nadie te entiende, ni tú mismo.",
            "No eres más que un estorbo."
        ]
        # Elige un mensaje al azar y lo envía al chat
        message = get_random_message(list)
        self.mc.postToChat(message)