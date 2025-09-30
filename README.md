
@staticmethod:

· Não recebe referência implícita à classe (não tem cls)
· Funciona como uma função normal, mas organizada dentro de uma classe
· Usado quando a função tem relação conceitual com a classe, mas não precisa acessar seus atributos ou métodos

@classmethod:

· Recebe a classe como primeiro parâmetro (cls)
· Pode acessar e modificar atributos da classe
· Pode criar novas instâncias da classe
· Uso no from_dict: Ideal para métodos de fábrica que criam instâncias da classe a partir de dados alternativos

```python
class MinhaClasse:
    @classmethod
    def from_dict(cls, data):  # Recebe a classe como cls
        return cls(**data)     # Cria nova instância
    
    @staticmethod
    def validar_dados(data):   # Não recebe referência à classe
        return bool(data)
```

2. Dataclasses

Principais vantagens:

· Redução de boilerplate: Gera automaticamente __init__, __repr__, __eq__
· Imutabilidade opcional: Pode ser configurada com frozen=True
· Valores padrão: Facilita definição de valores padrão com default e default_factory
· Type hints: Integração natural com sistema de tipos do Python

Para entidades de domínio:

· Código mais limpo e expressivo
· Foco na lógica de negócio em vez de código boilerplate
· Facilita a implementação de Value Objects e Eventos

3. Eventos de Domínio

O que são:

· Objetos que representam algo significativo que aconteceu no domínio
· Capturam mudanças de estado das entidades
· São imutáveis e carregam dados relevantes do contexto

Finalidade:

· Desacoplamento: Separa a ação da sua consequência
· Extensibilidade: Novos comportamentos podem ser adicionados sem modificar a entidade original
· Auditoria: Registro histórico das mudanças
· Integração: Comunicação entre bounded contexts diferentes

Redução de acoplamento:

· A entidade não precisa conhecer os handlers dos eventos
· Diferentes partes do sistema podem reagir aos eventos independentemente
· Facilita a implementação do padrão Event Sourcing

4. Decoradores (Decorators)

Conceito:

· Funções que modificam o comportamento de outras funções/métodos
· "Açúcar sintático" para funções de ordem superior
· Permitem adicionar funcionalidades sem modificar a função original

Funcionamento:

```python
def meu_decorator(func):
    def wrapper(*args, **kwargs):
        print("Antes da função")
        resultado = func(*args, **kwargs)
        print("Depois da função")
        return resultado
    return wrapper

@meu_decorator
def minha_funcao():
    print("Função executada")
```

Decoradores built-in comuns:

· @staticmethod, @classmethod
· @property, @abstractmethod
· @dataclass (na verdade é uma classe decorator)

Vantagens:

· Reutilização de código
· Separação de preocupações
· Manutenibilidade

---

Como Executar

1. Crie a estrutura de arquivos:

```
projeto/
├── category.py
├── events/
│   └── category_events.py
├── main.py
└── resumo_conceitual.md
```

1. Execute a demonstração:

```bash
python main.py
```

A saída mostrará:

· Teste completo de serialização (to_dict/from_dict)
· Ciclo de vida da entidade com eventos
· Processamento e limpeza de eventos
· Cenários de erro