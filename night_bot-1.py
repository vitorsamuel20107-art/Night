#!/usr/bin/env python3
"""
Night bot - Assistente do NIGHT Vault
Versão otimizada para Termux (Android)
"""

import os
import sys
from pathlib import Path

# ============================================================
# CONFIGURAÇÃO
# ============================================================

# Caminho do modelo (coloca o .gguf na pasta models/)
MODEL_PATH = Path(__file__).parent / "models" / "model.gguf"

# Modelos recomendados para celular (Termux):
# 1. SmolLM2-135M-Instruct Q4_K_M   (~105 MB)  → mais leve
# 2. SmolLM2-360M-Instruct Q4_K_M   (~270 MB)  → melhor equilíbrio
# 3. Qwen2.5-0.5B-Instruct Q4_K_M  (~490 MB)  → melhor qualidade

KNOWLEDGE_FILE = Path(__file__).parent / "knowledge_base.md"
MAX_TOKENS = 280
TEMPERATURE = 0.65

# ============================================================
# BASE DE CONHECIMENTO
# ============================================================

def load_knowledge() -> str:
    if KNOWLEDGE_FILE.exists():
        return KNOWLEDGE_FILE.read_text(encoding="utf-8")
    return "Base de conhecimento não encontrada."

KNOWLEDGE = load_knowledge()

SYSTEM_PROMPT = f"""Você é o Night bot, o assistente oficial do NIGHT Vault.

Seu jeito de falar:
- Sempre em português brasileiro
- Simples, claro e natural
- Como um amigo prestativo
- Respostas curtas e diretas

Você ajuda os usuários com dúvidas sobre o NIGHT Vault (gerenciador de keys).

=== CONHECIMENTO DO SISTEMA ===
{KNOWLEDGE}
=== FIM DO CONHECIMENTO ===

Regras importantes:
1. Cumprimentos e conversas leves (oi, bom dia, tudo bem, etc) → responda normalmente de forma amigável.
2. Perguntas sobre o NIGHT Vault → responda com base no conhecimento acima.
3. Se a pessoa fugir completamente do assunto (ex: pedir código Lua, receita, conversa nada a ver com o site) → responda educadamente que você é o assistente do NIGHT Vault e só pode ajudar com dúvidas do sistema.
4. Nunca invente informações que não estão no conhecimento.
5. Não fale que é uma inteligência artificial ou modelo de linguagem.
"""

# ============================================================
# CARREGA O MODELO
# ============================================================

llm = None

def load_model():
    global llm
    if llm is not None:
        return llm

    try:
        from llama_cpp import Llama
    except ImportError:
        print("❌ llama-cpp-python não está instalado.")
        print("No Termux rode: pip install llama-cpp-python")
        sys.exit(1)

    if not MODEL_PATH.exists():
        print(f"\n❌ Modelo não encontrado em:\n{MODEL_PATH}")
        print("\nBaixe um modelo pequeno e renomeie para 'model.gguf'")
        print("Coloque dentro da pasta 'models/'")
        print("\nRecomendados para celular:")
        print("• SmolLM2-135M-Instruct Q4_K_M  (mais leve)")
        print("• SmolLM2-360M-Instruct Q4_K_M  (melhor)")
        print("• Qwen2.5-0.5B-Instruct Q4_K_M")
        sys.exit(1)

    print("⏳ Carregando Night bot... aguarde")
    llm = Llama(
        model_path=str(MODEL_PATH),
        n_ctx=2048,
        n_threads=4,
        n_batch=256,
        verbose=False
    )
    print("✅ Night bot pronto!\n")
    return llm


def generate(query: str) -> str:
    model = load_model()

    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": query}
    ]

    try:
        response = model.create_chat_completion(
            messages=messages,
            max_tokens=MAX_TOKENS,
            temperature=TEMPERATURE,
            stop=["</s>", "Usuário:", "Você:", "User:", "Human:"]
        )
        answer = response["choices"][0]["message"]["content"].strip()
        return answer if answer else "Desculpa, não consegui gerar uma resposta agora."
    except Exception as e:
        return f"Ocorreu um erro ao processar: {str(e)[:100]}"


# ============================================================
# INTERFACE NO TERMINAL
# ============================================================

def main():
    print("=" * 50)
    print("       Night bot — NIGHT Vault")
    print("       Assistente de dúvidas")
    print("=" * 50)
    print("Digite sua pergunta (ou 'sair' para sair)\n")

    while True:
        try:
            user_input = input("Você: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nNight bot: Até mais! 👋")
            break

        if not user_input:
            continue

        if user_input.lower() in ("sair", "exit", "quit", "tchau", "flw"):
            print("Night bot: Até mais! Qualquer dúvida é só chamar.")
            break

        print("\nNight bot:", generate(user_input))
        print()


if __name__ == "__main__":
    main()
