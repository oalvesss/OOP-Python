# OOP-Python

Repositório de estudos de **Programação Orientada a Objetos (POO) em Python**.
Reúne exercícios de listas de atividades e um pequeno projeto prático (`Restaurant`)
que evolui junto com os conceitos estudados.

O objetivo é registrar a evolução do aprendizado: cada lista introduz um conceito
novo (atributos, métodos, encapsulamento, `@property`, `@classmethod`, etc.) e o
projeto em `models/` aplica esses conceitos em conjunto.

---

## 📁 Estrutura do projeto

```
OOP-Python/
├── main.py                  # Ponto de entrada do projeto Restaurant
├── models/
│   ├── restautant.py        # Classe Restaurant (regras de negócio)
│   └── assessment.py        # Classe Assessment (avaliações dos clientes)
└── activities/
    ├── list1/
    │   ├── exe1.py          # Classe Car + vars()
    │   ├── exe2.py          # Classe Restaurant (atributos simples)
    │   ├── exe3.py          # Restaurant (revisão de atributos)
    │   ├── exe4.py          # Restaurant + __str__
    │   └── exe5.py          # Classe Cliente
    └── list2/
        ├── ex1.py           # ContaBancaria / ClienteBanco (+ @classmethod)
        └── book.py          # Livro / Pessoa (+ @property)
```

---

## 🚀 Como executar

Pré-requisito: **Python 3.8+** (o projeto usa f-strings e métodos modernos de
`str`). Nenhuma dependência externa é necessária.

```bash
# Clone o repositório
git clone https://github.com/oalvesss/OOP-Python.git
cd OOP-Python

# Rode o projeto principal
python main.py

# Rode um exercício específico
python activities/list1/exe1.py
```

> 💡 Use um ambiente virtual para manter o ambiente limpo:
>
> ```bash
> python -m venv .venv
> source .venv/bin/activate      # Linux/macOS
> # .venv\Scripts\activate       # Windows
> ```

---

## 🧠 Conceitos praticados

| Conceito | Onde aparece | O que faz |
|---|---|---|
| **Classe e objeto** | `models/restautant.py`, `activities/` | Define moldes e cria instâncias |
| **`__init__`** | todos os arquivos | Inicializa os atributos do objeto |
| **Encapsulamento** | `self._name`, `self._active` | Atributos "privados" por convenção (`_`) |
| **`__str__`** | `Restaurant`, `Livro`, `Pessoa` | Representação legível do objeto (equivale ao `toString()` do Java) |
| **`@property`** | `active`, `assessmentNote`, `titulo_autor` | Acesso a valores calculados como atributos |
| **`@classmethod`** | `restaurants_list`, `criar_conta` | Métodos que operam na classe, não na instância |
| **Atributo de classe** | `Restaurant.restaurants` | Lista compartilhada por todas as instâncias |
| **Composição** | `Restaurant` → `Assessment` | Um objeto contém/agrega outros objetos |
| **`vars()`** | `activities/list1/exe1.py` | Inspeciona os atributos de uma instância |

---

## 🍽️ Projeto principal: Restaurant

O `main.py` demonstra o uso das classes `Restaurant` e `Assessment`:

- Cada restaurante tem **nome** (formatado com `.title()`) e **categoria** (`.upper()`).
- Todo restaurante é registrado automaticamente na lista da classe.
- `claimAssessment(cliente, nota)` só aceita notas entre **1 e 5**.
- `assessmentNote` calcula a **média das avaliações** (ou retorna `"No reviews"`).
- `toggle_state()` alterna o restaurante entre ativo/inativo.
- `restaurants_list()` imprime um **relatório formatado** de todos os restaurantes.

Exemplo de saída:

```
Restaurant Name: Da Praça   | Category: GOURMET    | Assessment: No reviews | Active: ❌
Restaurant Name: Requinte   | Category: BUFFET     | Assessment: 3.0        | Active: ❌
Restaurant Name: Teixeira   | Category: CASEIRA    | Assessment: No reviews | Active: ✅
```

> ⚠️ **Repare:** o `main.py` tenta lançar notas como `6` e `9` (e uma `10`
> comentada), mas a validação de `claimAssessment` aceita apenas `0 < nota <= 5`.
> Por isso só a nota `3` (do Pedro) é registrada e a média do Requinte fica `3.0`.
> Esse é um bom exercício de depuração: alinhar a regra de validação com as notas
> esperadas.

---

## 📝 Dicas e aprendizados

- **`_atributo` é convenção, não regra.** Em Python não existe `private` de verdade;
  o `_` avisa "não mexa daqui de fora".
- **`@property` evita métodos "get".** Em vez de `get_media()`, use
  `restaurant.assessmentNote` — mais legível e pythonico.
- **`@classmethod` é ótimo para relatórios e fábricas.** `restaurants_list()` e
  `criar_conta()` não precisam de uma instância para funcionar.
- **`__str__` é o `toString()` do Python.** Sempre que quiser uma saída legível
  ao dar `print(objeto)`, implemente esse método.
- **Cuidado ao formatar números com `ljust()`.** `ljust()` só existe em `str`;
  converta antes (`str(valor)`) para não dar `AttributeError`.
- **Valide dados na entrada.** `claimAssessment` ignora notas fora do intervalo
  em vez de quebrar o programa.
- **`if __name__ == '__main__':`** garante que o `main()` só rode quando o arquivo
  for executado diretamente, e não quando for importado.

---

## 🗺️ Próximos passos (ideias)

- [ ] Criar testes com `pytest` para `Restaurant` e `Assessment`.
- [ ] Alinhar a validação de nota (`0 < nota <= 5`) com as notas usadas no `main.py`.
- [ ] Adicionar menu interativo no `main.py` (cadastrar, avaliar, listar).
- [ ] Substituir a lista de classe por um repositório/banco de dados.
- [ ] Renomear `models/restautant.py` → `models/restaurant.py` (corrigir o typo).
- [ ] Adicionar `.gitignore` (ignorar `__pycache__/`, `.venv/`, `*.pyc`).
- [ ] Documentar cada lista de atividades com um `README.md` próprio.

---

## 👤 Autor

Desenvolvido como parte dos estudos de Python e POO.

- GitHub: [@oalvesss](https://github.com/oalvesss)

---

## 📄 Licença

Este projeto está sob a licença MIT — sinta-se livre para estudar, usar e adaptar
o código. (Adicione um arquivo `LICENSE` caso queira formalizar.)
