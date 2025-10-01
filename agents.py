from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
import os

async def main():
    model_client = OpenAIChatCompletionClient(
        model='o4-mini',
        api_key=os.getenv('OPENAI_API_KEY'),
        temperature=0.3
    )
    arxiv_agent = AssistantAgent(
        name="ArxivAgent",
        system_message=(
            """You are a helpful assistant that gets a description from user and
            searches for the most relevant or newest papers on arxiv.org using
            the python arxiv API. Always search for five time more paper than the
            user requested. Use the tool provided to conduct the search. Craft 
            the query to in arxiv API format."""
        ),
        model_client=model_client,
    )