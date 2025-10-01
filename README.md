# Ollama Search

A standalone Python script that combines Ollama LLM with DuckDuckGo web search using LangChain.

## Features

- Local LLM inference with Ollama
- Free web search via DuckDuckGo (no API key required)
- Agent-based architecture for intelligent search decisions
- Interactive command-line interface

## Requirements

- Python 3.12+
- Ollama installed and running locally
- At least one Ollama model pulled

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure Ollama is running:
```bash
ollama serve
```

3. Pull a model (if you haven't already):
```bash
ollama pull llama3.1
```

## Usage

Run the script:
```bash
python3 ollama_search.py
```

Then enter your question when prompted. The agent will automatically decide when to search the web.

## Configuration

Edit `ollama_search.py` to change the model:
```python
llm = ChatOllama(model="your-model-name", temperature=0.7)
```

## Example

```
Ask: What is the current weather in Paris?

> Entering new AgentExecutor chain...
Invoking: `duckduckgo_search` with `{'query': 'Paris current weather'}`

✨ The current weather in Paris is 12 °C with clear skies.
```
