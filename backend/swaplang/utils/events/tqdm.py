# from tqdm.auto import tqdm
from huggingface_hub.utils.tqdm import tqdm

from swaplang.utils.events import event
from swaplang.utils.events.models import MessageEvent


def emit(n, total, rate, elapsed, **kwargs):
    total = total or 1
    event.emit(
        MessageEvent(
            # event="download_progress",
            data={
                "downloaded_bytes": n,
                "total_bytes": total,
                "progress_percentage": n / total * 100,
                "rate": rate,
                "time_remaining": (total - n) / rate,
                "total_time": elapsed,
            },
        )
    )


class TqdmToEvent(tqdm):
    def update(self, n=1):
        displayed = super().update(n)
        if displayed:
            emit(**self.format_dict)
        return displayed
