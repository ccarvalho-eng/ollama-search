#!/usr/bin/env python3
"""
Ollama + DuckDuckGo search with LangChain
Install: pip install langchain langchain-ollama duckduckgo-search
"""

from langchain_ollama import ChatOllama
from langchain_community.tools import DuckDuckGoSearchRun
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

# Setup
llm = ChatOllama(model="incept5/llama3.1-claude:latest", temperature=0.7)
search = DuckDuckGoSearchRun()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant with web search access."),
    ("human", "{input}"),
    ("placeholder", "{agent_scratchpad}"),
])

agent = create_tool_calling_agent(llm, [search], prompt)
agent_executor = AgentExecutor(agent=agent, tools=[search], verbose=True)

# Run
query = input("Ask: ")
result = agent_executor.invoke({"input": query})
print(f"\n✨ {result['output']}")
