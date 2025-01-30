from agentFramework import AgentFramework

if __name__ == "__main__":
    # Crea una instancia del framework de agentes
    framework = AgentFramework()
    # Registra los agentes desde el módulo especificado
    framework.register_agents_from_module('insultBot')
    framework.register_agents_from_module('tntBot')
    framework.register_agents_from_module('oracleBot')
    # Ejecuta el framework
    framework.run()