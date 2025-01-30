from agentFramework import BaseAgent
import random
import time


def get_random_message(messages):
    return random.choice(messages)

class OracleBot(BaseAgent):
    def perform_action(self):
        list = [
            "Yes, definitely!",
            "No, certainly not.",
            "It is possible.",
            "I don't think so.",
            "Ask again later.",
            "Absolutely!",
            "I'm not sure.",
            "Without a doubt.",
            "Very doubtful.",
            "Yes, in due time."
        ]
                
        messages = self.mc.events.pollChatPosts()
        
        for message in messages:
            if "oraclebot" in message.message.lower():
                    # Extrae la pregunta y obtiene una respuesta de OpenAI
                answer =get_random_message(list)  
                        # Envía la respuesta al chat

                self.mc.postToChat(f"<oracleBot> {answer}")