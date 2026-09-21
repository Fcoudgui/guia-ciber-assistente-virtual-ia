import json
import re
from pathlib import Path


BASE_PATH = Path(__file__).resolve().parents[1] / "data" / "base_conhecimento.json"
TERMOS_BLOQUEADOS = [
    "invadir",
    "roubar",
    "quebrar senha",
    "hackear conta",
    "pegar senha",
    "derrubar site",
]


def normalizar(texto: str) -> str:
    texto = texto.lower()
    texto = re.sub(r"[^a-z0-9\s]", " ", texto)
    return re.sub(r"\s+", " ", texto).strip()


def carregar_base() -> list[dict]:
    with BASE_PATH.open("r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def pergunta_insegura(pergunta: str) -> bool:
    pergunta_normalizada = normalizar(pergunta)
    return any(termo in pergunta_normalizada for termo in TERMOS_BLOQUEADOS)


def pontuar(pergunta: str, item: dict) -> int:
    pergunta_normalizada = normalizar(pergunta)
    pontos = 0

    for palavra in item["palavras_chave"]:
        if normalizar(palavra) in pergunta_normalizada:
            pontos += 3

    for termo in pergunta_normalizada.split():
        if termo in normalizar(item["topico"]):
            pontos += 1

    return pontos


def buscar_resposta(pergunta: str, base: list[dict]) -> dict | None:
    candidatos = sorted(
        ((pontuar(pergunta, item), item) for item in base),
        key=lambda candidato: candidato[0],
        reverse=True,
    )
    melhor_pontuacao, melhor_item = candidatos[0]
    return melhor_item if melhor_pontuacao > 0 else None


def responder(pergunta: str, base: list[dict]) -> str:
    if pergunta_insegura(pergunta):
        return (
            "Nao posso ajudar com invasao, roubo de dados ou abuso de sistemas. "
            "Posso ajudar com boas praticas defensivas, como MFA, senhas fortes e identificacao de phishing."
        )

    item = buscar_resposta(pergunta, base)
    if not item:
        return (
            "Nao encontrei informacao suficiente na minha base para responder com seguranca. "
            "Tente perguntar sobre phishing, senhas, MFA, engenharia social, OSINT, metadados, DevSecOps ou sistemas operacionais."
        )

    return f"{item['resposta']}\n\nProximo passo: aplique essa orientacao em uma situacao simples do seu dia a dia."


def main() -> None:
    base = carregar_base()
    print("GuiaCiber - Assistente Virtual de Ciberseguranca")
    print("Digite sua pergunta ou 'sair' para encerrar.\n")

    while True:
        pergunta = input("Voce: ").strip()
        if normalizar(pergunta) in {"sair", "exit", "quit"}:
            print("GuiaCiber: Ate mais. Continue praticando seguranca digital.")
            break

        if not pergunta:
            print("GuiaCiber: Digite uma pergunta para eu ajudar.")
            continue

        print(f"GuiaCiber: {responder(pergunta, base)}\n")


if __name__ == "__main__":
    main()
