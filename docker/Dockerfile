FROM node:22.14-slim AS frontend
ENV PNPM_HOME="pnpm"
ENV PATH="$PNPM_HOME:$PATH"
RUN corepack enable
WORKDIR /app

RUN mkdir -p frontend
COPY ./frontend/package.json ./frontend/pnpm-lock.yaml /app/frontend
WORKDIR /app/frontend
RUN --mount=type=cache,id=pnpm,target=/pmpm/store pnpm install --frozen-lockfile
COPY ./frontend/ /app/frontend
RUN pnpm run build


# CPU BUILD

FROM python:3.12.11-alpine AS backend-cpu

RUN apk add --no-cache build-base gcc

WORKDIR /app

RUN --mount=type=bind,source=./backend/uv.lock,target=uv.lock \
    --mount=type=bind,source=./backend/pyproject.toml,target=pyproject.toml \
    --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    uv sync --locked --no-install-project --no-dev --extra cpu

COPY ./backend /app
COPY --from=frontend /app/frontend/build /app/swaplang/frontend/

RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    uv sync --locked --no-dev --no-editable --extra cpu


FROM python:3.12.11-alpine AS cpu

RUN apk add --no-cache libstdc++ libgomp

WORKDIR /swaplang

COPY --from=backend-cpu /app/.venv /swaplang/.venv

ENV HF_HOME="/tmp/huggingface"
ENV HF_HUB_CACHE="/tmp/huggingface/hub"
ENV PATH="/swaplang/.venv/bin:$PATH"
ENV DATA_DIR="/data"
ENV ENVIRONMENT="prod"
ENV GPU_SUPPORT="false"

EXPOSE 1717

CMD ["python", "-m", "swaplang"]


# GPU BUILD 

FROM nvidia/cuda:12.4.0-runtime-ubuntu22.04 AS base-gpu

RUN apt-get update && apt-get install -y \
    libgomp1 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV UV_PYTHON_INSTALL_DIR="/opt/uv/python"

RUN --mount=from=ghcr.io/astral-sh/uv,source=/uv,target=/bin/uv \
    uv python install 3.12

RUN chmod -R a+rX $UV_PYTHON_INSTALL_DIR


FROM base-gpu AS backend-gpu

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY ./backend/uv.lock ./backend/pyproject.toml /app

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-install-project --no-dev --extra gpu

COPY ./backend /app
COPY --from=frontend /app/frontend/build /app/swaplang/frontend/

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev --no-editable --extra gpu


FROM base-gpu AS gpu

WORKDIR /swaplang

COPY --from=backend-gpu /app/.venv /swaplang/.venv

ENV HF_HOME="/tmp/huggingface"
ENV HF_HUB_CACHE="/tmp/huggingface/hub"
ENV PATH="/swaplang/.venv/bin:$PATH"
ENV DATA_DIR="/data"
ENV ENVIRONMENT="prod"

EXPOSE 3737

CMD ["python", "-m", "swaplang"]
