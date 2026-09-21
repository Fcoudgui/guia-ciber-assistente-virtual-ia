# GuiaCiber - Assistente Virtual de Ciberseguranca

Projeto desenvolvido para o desafio **Construa seu Assistente Virtual com Inteligencia Artificial**, da DIO.

## 1. Visao geral

O **GuiaCiber** e um assistente virtual simples para ajudar pessoas iniciantes a entender boas praticas de ciberseguranca. Ele responde perguntas sobre temas basicos como senhas, MFA, phishing, engenharia social, OSINT, metadados, DevSecOps e sistemas operacionais.

O objetivo nao e substituir um especialista, mas oferecer uma primeira orientacao clara, segura e baseada em uma pequena base de conhecimento.

## 2. Publico-alvo

- Pessoas iniciantes em tecnologia.
- Estudantes de ciberseguranca.
- Usuarios que querem melhorar habitos digitais.
- Profissionais que precisam revisar conceitos basicos.

## 3. Problema

Muitas pessoas conhecem termos como phishing, MFA e engenharia social, mas ainda nao sabem como aplicar esses conceitos no dia a dia. Isso aumenta o risco de golpes, vazamentos de senhas e decisoes inseguras.

## 4. Solucao

O GuiaCiber recebe uma pergunta do usuario, procura termos relacionados na base de conhecimento e responde de forma objetiva. Quando nao encontra informacao suficiente, ele informa a limitacao e sugere reformular a pergunta.

## 5. Estrutura do projeto

```text
assistente-virtual-ia/
  README.md
  data/
    base_conhecimento.json
  docs/
    agente.md
    prompts.md
    avaliacao_metricas.md
    pitch.md
  src/
    assistente.py
  tests/
    perguntas_teste.md
```

## 6. Como executar

### Opcao 1: navegador

Abra o arquivo:

```text
src/index.html
```

Essa versao nao precisa instalar nada.

### Opcao 2: terminal

Requisito: Python 3.10 ou superior.

```bash
python src/assistente.py
```

Depois, digite uma pergunta, por exemplo:

```text
Como identificar phishing?
```

Para sair:

```text
sair
```

## 7. Como funciona

1. O usuario digita uma pergunta.
2. A aplicacao normaliza o texto.
3. O sistema compara palavras-chave da pergunta com a base de conhecimento.
4. O melhor topico encontrado e usado para montar a resposta.
5. Se nenhum topico for encontrado, o assistente explica que nao tem informacao suficiente.

## 8. Exemplos de perguntas

- O que e phishing?
- Como criar uma senha forte?
- Por que usar MFA?
- O que e engenharia social?
- O que sao metadados?
- O que e DevSecOps?
- O que e kernel?

## 9. Etapas do desafio

### Documentacao do agente

Arquivo: `docs/agente.md`

Descreve objetivo, publico, tom de voz, limites e comportamento esperado.

### Base de conhecimento

Arquivo: `data/base_conhecimento.json`

Contem topicos, palavras-chave e respostas-base usadas pelo assistente.

### Prompts do agente

Arquivo: `docs/prompts.md`

Define prompt de sistema, prompt de usuario e regras de seguranca.

### Aplicacao funcional

Arquivo: `src/assistente.py`

Implementa um prototipo funcional em linha de comando.

### Avaliacao e metricas

Arquivo: `docs/avaliacao_metricas.md`

Mostra perguntas de teste, criterios de avaliacao e resultados esperados.

### Pitch

Arquivo: `docs/pitch.md`

Apresenta problema, solucao, publico e valor do projeto.

## 10. Limitacoes

- Base de conhecimento pequena.
- Nao usa modelo generativo real.
- Nao executa diagnostico tecnico.
- Nao deve ser usado como consultoria profissional de seguranca.

## 11. Possiveis melhorias

- Integrar uma API de IA generativa.
- Criar interface web.
- Adicionar historico de conversa.
- Aumentar a base de conhecimento.
- Implementar busca semantica com embeddings.

## 12. Conclusao

O GuiaCiber demonstra como um assistente virtual pode usar uma base de conhecimento organizada para orientar usuarios em uma tarefa real. O foco do projeto esta em documentacao, clareza, utilidade e aprendizado pratico.
