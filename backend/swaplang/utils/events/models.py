from pydantic import BaseModel, model_serializer
import json


class MessageEvent(BaseModel):
    data: str | dict
    id: int | None = None
    event: str | None = None
    retry: int | None = None

    @model_serializer(mode="plain")
    def serialize_model(self) -> str:
        parts = []
        if self.id is not None:
            parts.append(f"id: {self.id}")
        if self.event is not None:
            parts.append(f"event: {self.event}")
        if self.retry is not None:
            parts.append(f"retry: {self.retry}")
        if isinstance(self.data, dict):
            parts.append(f"data: {json.dumps(self.data)}")
        else:
            for line in self.data.splitlines():
                parts.append(f"data: {line}")
        return "\n".join(parts) + "\n\n"
