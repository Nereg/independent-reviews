FROM python:3.13.3-slim

# install UV
COPY --from=ghcr.io/astral-sh/uv:0.7.2 /uv /uvx /bin/

# (optional) git install
RUN apt-get update \
    && apt-get install -y --no-install-recommends git \
    && apt-get purge -y --auto-remove \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app/

ENV UV_PROJECT_ENVIRONMENT=/usr/local/venv
# Install dependencies
RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync --locked --no-install-project

# copy the app
# COPY . /app/
# RUN mkdir /app
# WARNING: needs the app volume at /app/
# request the python output to be unbuffered https://stackoverflow.com/a/29745541
ENTRYPOINT [ "uv", "run", "src/main.py" ]