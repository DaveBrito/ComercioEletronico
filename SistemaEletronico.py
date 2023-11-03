import random

# Subsistema 1
class SistemaAutenticacao:
    def autenticar_usuario(self, usuario, senha):
        if usuario == "fulano@gmail.com" and senha == "usuario123":
            print("Acesso Permitido")
            return True
        else:
            print("Acesso Negado")
            return False

# Proxy para o Subsistema 1
class SistemaAutenticacaoProxy:
    def __init__(self):
        self.sistema_autenticacao = SistemaAutenticacao()
        self.usuario_autenticado = False

    def autenticar_usuario(self, usuario, senha):
        if self.usuario_autenticado:
            print("Usuário já está autenticado.")
            return True
        else:
            return self.sistema_autenticacao.autenticar_usuario(usuario, senha)

# Subsistema 2
class SistemaCadastro:
    def __init__(self):
        self.usuarios_cadastrados = []

    def cadastrar_usuario(self, usuario):
        print(f"Cadastrando usuário {usuario}...")
        self.usuarios_cadastrados.append(usuario)
        return True  # Simulado deu certo

# Subsistema 3
class SistemaPedido:
    def criar_pedido(self, produtos):
        pedido_id = f"PED-{random.randint(100, 999)}"  # ID aleatório de 3 números
        print(f"Criando pedido de produtos {produtos} com ID: {pedido_id}")
        return pedido_id

# Fachada (Facade)
class AtendimentoCliente:
    def __init__(self):
        self.autenticacao_proxy = SistemaAutenticacaoProxy()
        self.cadastro = SistemaCadastro()
        self.pedido = SistemaPedido()

    def realizar_atendimento(self, usuario, senha, produtos):
        if self.autenticacao_proxy.autenticar_usuario(usuario, senha):
            pedido_id = self.pedido.criar_pedido(produtos)
            self.cadastro.cadastrar_usuario(usuario)
            print(f"Atendimento realizado com sucesso. Pedido: {pedido_id}")
        else:
            print("Falha na autenticação. Atendimento não realizado.")

# Cliente
atendimento = AtendimentoCliente()

# usuario = "shaolin123@gmail.com" # // Para testar possíveis falhas na autenticação
# senha = "shaolin1234"

usuario = "fulano@gmail.com"
senha = "usuario123"
produtos = ["Fita RGB", "Caneta Esferográfica", "Empire: Total War"]

atendimento.realizar_atendimento(usuario, senha, produtos)
