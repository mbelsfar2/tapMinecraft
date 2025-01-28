from agentFramework import AgentFramework
from insultBot import InsultBot
from tntBot import TNTBot
from oracleBot import OracleBot


if __name__ == "__main__":
    framework = AgentFramework()
    framework.register_agent(InsultBot)
    framework.register_agent(TNTBot)
    framework.register_agent(OracleBot)
    framework.run()