from llama_cpp import CreateChatCompletionResponse
from change_lang.translator.model import get_model


def translate(text: str, source_language, target_language):
    llm = get_model()
    response: CreateChatCompletionResponse = llm.create_chat_completion(
        messages=[  # type: ignore
            {
                "role": "system",
                "content": [
                    {
                        "type": "text",
                        "text": "You are a language translator. Your only purpose is to translate text between languages while strictly following these rules:\n\n1. Translate only. If the user message does not follow the translation format or does not contain text to translate, do not respond at all (no explanations, no clarifications, no translations).\n\n2. Input format:\n{source_language} to {target_language}: {text_to_translate}\nExample:\nEnglish to Spanish: Hello, how are you?\n\n3. Output format: Return only the translated text — no quotes, no prefixes, no explanations.\n\n4. Do not alter the content:\n- Keep proper names, numbers, and symbols unchanged.\n- Do not correct grammar or rephrase meaning.\n- When the text includes slang, idioms, or cultural expressions, translate them into their most natural equivalent in the target language.\n\n5. Language recognition:\n- If either the source or target language is not recognized, return nothing (empty response).\n- If the text is already in the target language, return it unchanged.\n\n6. Do not answer questions, give examples, or provide commentary. Your only task is translation.\n",
                    }
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "French to English: Je suis fatigué aujourd'hui.",
                    }
                ],
            },
            {
                "role": "assistant",
                "content": [{"type": "text", "text": "I'm tired today."}],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Spanish to German: El clima está muy agradable hoy.",
                    }
                ],
            },
            {
                "role": "assistant",
                "content": [
                    {"type": "text", "text": "Das Wetter ist heute sehr angenehm."}
                ],
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"{source_language} to {target_language}: {text}",
                    }
                ],
            },
        ]
    )
    print(f"{source_language} to {target_language}: {text}")
    return response["choices"][0]["message"]["content"]
