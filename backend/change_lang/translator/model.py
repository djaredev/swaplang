from llama_cpp import Llama


_llm = None


def get_model() -> Llama:
    global _llm
    if _llm is None:
        _llm = Llama(model_path="gemma-3-1b-it-Q8_0.gguf", n_gpu_layers=-1, n_ctx=2048)
    return _llm
