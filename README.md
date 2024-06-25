<div align="center">
<h1>
API Call Example
</h1>

Built with `asyncflows`

[![main repo](https://img.shields.io/badge/main_repo-1f425f)](https://github.com/asynchronous-flows/asyncflows)
[![Discord](https://img.shields.io/badge/discord-7289da)](https://discord.gg/AGZ6GrcJCh)

</div>

## Introduction

This example demonstrates how to use and write custom asyncflows actions.  

This repo includes:
- `my_actions/my_get_url.py`, an action that fetches the HTML of a website
- `get_website_title.yaml`, a flow that prompts a language model to get the title of the fetched website
- `get_website_title.py`, a script that runs the flow

## Running the Example

To run the example:

1. Set up [Ollama](https://github.com/asynchronous-flows/asyncflows#setting-up-ollama-for-local-inference) or configure [another language model](https://github.com/asynchronous-flows/asyncflows#using-any-language-model)  

2. Clone the repository

```bash
git clone ssh://git@github.com/asynchronous-flows/api-call-example
```

3. Change into the directory

```bash
cd api-call-example
```

4. Create and activate your virtual environment (with, for example)

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

5. If not already installed, [install poetry](https://python-poetry.org/docs/#installation). Install dependencies with:

```bash
poetry install
```

6. Run the example

```bash
python -m api_call_example.get_website_title
```

## Writing your own Actions

Use this repository as a template, and add more actions in the `api_call_example/my_actions` directory.

As long as they are in the `my_actions` directory, they will be automatically loaded by the `asyncflows` library.
If you'd like to change that directory, or use the paradigm in the different package,
simply include the [`tool.poetry.plugins` directive in the `pyproject.toml` file](https://github.com/asynchronous-flows/api-call-example/blob/main/pyproject.toml#L20):

```toml
[tool.poetry.plugins."asyncflows"]
actions = "api_call_example.my_actions"
```
