FROM python:3.10 as base

WORKDIR /app
COPY ../pyproject.toml .
COPY ../requirements.txt .
RUN pip install . && rm pyproject.toml requirements.txt
ENV PYTHONPATH=/app

FROM base as github_app
COPY ../ai_pr_agent ai_pr_agent
CMD ["python", "ai_pr_agent/servers/github_app.py"]



FROM base as github_polling
COPY ../ai_pr_agent ai_pr_agent
CMD ["python", "ai_pr_agent/servers/github_polling.py"]


FROM base as test
ADD requirements-dev.txt .
RUN pip install -r requirements-dev.txt && rm requirements-dev.txt
ADD ai_pr_agent ai_pr_agent
ADD tests tests

FROM base as cli
COPY ../ai_pr_agent ai_pr_agent
ENTRYPOINT ["python", "ai_pr_agent/cli.py"]
