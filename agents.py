from autogen_agentchat.agent import AssistantAgent
import asyncio

async def main():
    arxiv_agent = AssistantAgent(
        name="ArxivAgent",
        system_message=(
            """You are a helpful assistant that gets a description from user and
            searches for the most relevant or newest papers on arxiv.org using
            the python arxiv API"""
        )
    )