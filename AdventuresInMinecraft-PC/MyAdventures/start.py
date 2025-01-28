from agentFramework import AgentFramework
from insultBot import InsultBot
from tntBot import TNTBot

if __name__ == "__main__":
    framework = AgentFramework()
    framework.register_agent(InsultBot)
    framework.register_agent(TNTBot)
    framework.run()