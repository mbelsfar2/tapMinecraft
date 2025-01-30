from agentFramework import AgentFramework
from insultBot import InsultBot
from tntBot import TNTBot
from oracleBot import OracleBot


if __name__ == "__main__":
    # Crea una instancia del framework de agentes
    framework = AgentFramework()
    # Registra los agentes
    framework.register_agent(InsultBot)
    framework.register_agent(TNTBot)
    framework.register_agent(OracleBot)
    # Ejecuta el framework
    framework.run()