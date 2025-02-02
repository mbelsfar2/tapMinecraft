from agentFramework import BaseAgent
import random
import time


def get_random_message(messages):
    return random.choice(messages)

class OracleBot(BaseAgent):
    def perform_action(self):
        list = [
            "Sí, definitivamente",
            "No, ciertamente no.",
            "Es posible.",
            "No lo creo.",
            "Pregunta de nuevo más tarde.",
            "Absolutamente",
            "No estoy seguro.",
            "Sin duda.",
            "Muy dudoso.",
            "Sí, a su debido tiempo."
        ]
                
        messages = self.mc.events.pollChatPosts()
        
        for message in messages:
            if "oraclebot" in message.message.lower():
                    # Extrae la pregunta y obtiene una respuesta de OpenAI
                answer =get_random_message(list)  
                        # Envía la respuesta al chat

                self.mc.postToChat(f"<oracleBot> {answer}")