from llama_cpp import Llama
from huggingface_hub import hf_hub_download
from swaplang.config import settings
from swaplang.utils.events import TqdmToEvent
import asyncio


_llm: Llama | None = None
_model_lock = asyncio.Lock()


def _download_model():
    hf_hub_download(
        repo_id=settings.HF_HUB_REPO_ID,
        filename=settings.DEFAULT_MODEL,
        local_dir=settings.MODELS_DIR,
        tqdm_class=TqdmToEvent,
    )


def _load_model() -> Llama:
    if not settings.MODEL_PATH.exists():
        _download_model()
    return Llama(
        model_path=str(settings.MODEL_PATH),
        n_gpu_layers=-1,
        n_ctx=2048,
    )


async def get_model() -> Llama:
    global _llm
    if _llm is None:
        async with (
            _model_lock
        ):  # Ensure only one coroutine can load the model at a time
            if _llm is None:  # Double-checked locking
                _llm = await asyncio.to_thread(_load_model)
    return _llm
