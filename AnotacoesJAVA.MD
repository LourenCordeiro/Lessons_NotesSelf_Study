# Anotações — Curso de Java

### Aula 01 — 27/10/2026

#### Compilador

- **Compilador** é um software que transforma o **código-fonte** em **código-objeto**.

#### Linguagem de programação

- **Linguagem de programação** é um conjunto de regras:
  - **Léxicas** → ortografia
  - **Sintáticas** → gramática

**Exemplos de linguagens de programação:**

| Linguagem | Como é executada |
| --- | --- |
| C | Compilada para código de máquina |
| C++ | Compilada para código de máquina |
| Go | Compilada para código de máquina |
| Rust | Compilada para código de máquina |
| **Java** | Compilada para *bytecode*, executado pela JVM |
| Kotlin | Compilada para *bytecode*, executado pela JVM |
| C# | Compilada para código intermediário, executado pelo .NET |
| Python | Interpretada |
| JavaScript | Interpretada (navegador ou Node.js) |
| PHP | Interpretada |

#### IDE

- **IDE** (*Integrated Development Environment* — Ambiente Integrado de Desenvolvimento) é um conjunto de softwares utilizados para a construção de programas.

**Funcionalidades de uma IDE:**

- Edição de código-fonte (indentação, autocompletar, destaque de palavras etc.)
- Depuração e testes
- Construção do produto final (*build*)
- Sugestão de modelos (*templates*)
- Auxílio em várias tarefas do projeto
- Etc.

**Exemplos de IDEs:**

| IDE | Linguagens principais |
| --- | --- |
| **IntelliJ IDEA** | **Java**, Kotlin |
| **Eclipse** | **Java** (outras via plugins) |
| **NetBeans** | **Java**, PHP |
| Android Studio | Kotlin, Java (apps Android) |
| Visual Studio | C#, C++ (.NET) |
| PyCharm | Python |
| WebStorm | JavaScript, TypeScript |
| Xcode | Swift, Objective-C (apps Apple) |
| Code::Blocks | C, C++ |

> **VS Code** é muito usado, mas tecnicamente é um **editor de código**: vira algo próximo de uma IDE com extensões, e atende várias linguagens (incluindo Java).

#### Código-fonte

- **Código-fonte** é escrito pelo desenvolvedor em uma linguagem de programação.

#### Compilação

![Fluxo de compilação: código-fonte → código-objeto → código executável](imagens/aula01-compilacao.png)

1. **Código-fonte → código-objeto**: feito pelo **compilador** (compilação), com análise léxica + análise sintática.
2. **Código-objeto → código executável**: feito pelo **gerador de código** (construção / *build*), com geração de código.

#### Linguagens compiladas

O código-fonte é compilado **antes** de executar, gerando um programa pronto para rodar.

**Compiladas para código de máquina** (executável roda direto no sistema operacional):

- C
- C++
- Go
- Rust
- Swift
- Pascal / Delphi
- Fortran
- COBOL

**Compiladas para código intermediário** (precisa de uma máquina virtual para executar — é a **abordagem híbrida**, explicada mais abaixo):

- **Java** → *bytecode*, executado pela **JVM**
- Kotlin → *bytecode*, executado pela JVM
- Scala → *bytecode*, executado pela JVM
- C# → código intermediário, executado pelo .NET

#### Linguagens interpretadas

Não existe uma etapa de compilação separada antes de rodar. Um programa chamado **interpretador** lê o código-fonte e executa as instruções **durante a execução**.

**Como funciona:**

```
Código-fonte → Interpretador (lê, analisa e executa) → Resultado
```

1. O interpretador lê uma instrução do código-fonte.
2. Faz a análise léxica e sintática dessa instrução.
3. Executa a instrução na hora.
4. Passa para a próxima.

**Compilada x interpretada:**

| | Compilada | Interpretada |
| --- | --- | --- |
| Quando o código é traduzido | Antes de executar | Durante a execução |
| Gera arquivo executável | Sim | Não |
| Precisa de quê para rodar | Só o executável | O interpretador instalado |
| Erros de sintaxe aparecem | Na compilação | Ao executar aquela parte |
| Velocidade | Geralmente mais rápida | Geralmente mais lenta |

**Exemplos de linguagens interpretadas:**

- Python
- JavaScript (navegador ou Node.js)
- PHP
- Ruby
- Perl
- Lua
- R
- Shell script (Bash)

> Na prática, muitas linguagens interpretadas modernas também fazem uma compilação interna para ganhar velocidade. O Python gera *bytecode* (`.pyc`), e os motores de JavaScript usam compilação JIT (*Just-In-Time*). Mesmo assim, para quem programa, elas continuam funcionando como interpretadas: você roda o código-fonte direto, sem gerar um executável antes.

#### Abordagem híbrida

Mistura as duas formas: o código-fonte é **compilado** para um código intermediário (*bytecode*), e esse código é **interpretado** por uma **máquina virtual** na hora de executar.

**Como funciona (exemplo com Java):**

```
Código-fonte (.java) → Compilador (javac) → Bytecode (.class) → JVM (interpreta + JIT) → Resultado
```

1. O desenvolvedor escreve o código-fonte em um arquivo `.java`.
2. O compilador `javac` faz a análise léxica e sintática e gera o *bytecode* (arquivo `.class`).
3. O *bytecode* não é código de máquina de nenhum sistema operacional específico.
4. A **JVM** (*Java Virtual Machine*) instalada no computador lê e executa esse *bytecode*.
5. Os trechos executados com mais frequência são compilados pela JVM para código de máquina durante a execução (**JIT** — *Just-In-Time*), o que deixa o programa mais rápido.

**Vantagens:**

- **Portabilidade**: o mesmo `.class` roda em Windows, Linux ou macOS, desde que exista uma JVM. É o famoso lema do Java: *"Write once, run anywhere"* (escreva uma vez, rode em qualquer lugar).
- **Erros de sintaxe pegos antes de rodar**, porque existe a etapa de compilação.
- **Bom desempenho**, graças ao JIT, mais rápido que uma linguagem puramente interpretada.

**Desvantagem:**

- Precisa da máquina virtual instalada (JVM, .NET) para executar.

**Linguagens que usam a abordagem híbrida:**

| Linguagem | Máquina virtual |
| --- | --- |
| **Java** | JVM |
| Kotlin | JVM |
| Scala | JVM |
| Groovy | JVM |
| C# | .NET (CLR) |
| VB.NET | .NET (CLR) |
| F# | .NET (CLR) |

**Resumo das três abordagens:**

| Abordagem | Tradução | Executa com | Exemplos |
| --- | --- | --- | --- |
| Compilada | Tudo antes, para código de máquina | O próprio sistema operacional | C, C++, Go, Rust |
| Interpretada | Durante a execução | Interpretador | Python, JavaScript, PHP |
| Híbrida | Compila para *bytecode* e interpreta/JIT ao executar | Máquina virtual | **Java**, Kotlin, C# |

#### Vantagens

**Compilação:**

- Velocidade do programa
- Auxílio do compilador antes da execução

**Interpretação:**

- Flexibilidade de manutenção do aplicativo em produção
- Expressividade da linguagem
- Código-fonte não precisa ser recompilado para rodar em plataformas diferentes

#### Portabilidade entre sistemas operacionais

- **Compilada**: é necessário **compilar de acordo com o sistema operacional** da máquina (um executável para Windows, outro para Linux, outro para macOS).
- **Interpretada**: o código-fonte é o mesmo; basta **trocar o interpretador** pelo do sistema operacional.
- **Híbrida**: o código-fonte é traduzido para **bytecode** (código pré-compilado), que é executado por uma **máquina virtual específica** para cada sistema operacional.
