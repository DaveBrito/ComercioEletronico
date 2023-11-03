class SistemaAutenticacao {
  autenticarUsuario(usuario, senha) {
    console.log(`Autenticacao do usuario ${usuario}....`);

    if (usuario === "maria@gmail.com" && senha === "maria24") {
      console.log("Acesso Permitido");
      console.log("-----------------------");
      return true;
    } else if (usuario !== "" && senha !== "") {
      console.log("Acesso Negado");
      console.log("-----------------------");
      return false;
    }
  }
}

class SistemaCadastro {
  cadastrarUsuario(usuario) {
    console.log("-----------------------");
    console.log(`Cadastrando o usuario ${usuario}....`);
    console.log(`Bem Vindo(a)...`);
    console.log("-----------------------");
  }
}

class SistemaPedido {
  criarPedido(pedido) {
    console.log(`Criando o pedido ${pedido}....`);
  }
}

class AtendimentoCliente {
  gerarID() {
    return Math.random().toString(36).substr(2, 9);
    //Cria um ID com 9 letras misturado com numeros
  }

  realizarAtendimento(usuario, senha, produto) {
    const autenticacao = new SistemaAutenticacao();
    const cadastro = new SistemaCadastro();
    const pedido = new SistemaPedido();

    if (autenticacao.autenticarUsuario(usuario, senha)) {
      const pedidoID = this.gerarID();
      const ID = pedidoID;
      pedido.criarPedido(produto, usuario);
      cadastro.cadastrarUsuario(usuario);
      console.log(`Atendimento realizado com sucesso. Pedido ID : ${pedidoID}`);
    } else {
      console.log(`Falha na autenticação. Atendimento não realizado`);
    }
    return "Camisa";
  }
}
//Criacao do Proxy
class AtendimentoClienteProxy {
  constructor() {
    this.atendimentoCliente = new AtendimentoCliente();
  }
  //realizarAtendimento irá chamar outra funcao do msm nome acima
  realizarAtendimento(usuario, senha, produto) {
    console.log("Interceptando requisição...");
    this.atendimentoCliente.realizarAtendimento(usuario, senha, produto);
  }
}

//Uso do Proxy
const proxy = new AtendimentoClienteProxy();
// E-mail ou senha diferente, irá dar erro
const usuario = "maria@gmail.com";
const senha = "maria24";
const produto = "Camisa";
proxy.realizarAtendimento(usuario, senha, produto);
