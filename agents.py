from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.openai import OpenAIChatCompletionClient
import asyncio
import os
import arxiv

def search_arxiv(query:str, max_results:int=5, sort_by:str='relevance'):
    """
    Search for papers on arxiv.org using the arxiv API.
    
    Args: 
        query (str): The search query.
        max_results (int): The maximum number of results to return.
        sort_by (str): The sorting criterion, either 'relevance' or 'latestUpdated'.
    """
    client = arxiv.Client()
    search = arxiv.Search(
        query=query,
        max_results=max_results,
        sort_by=arxiv.SortCriterion.Relevance if sort_by == 'relevance' else arxiv.SortCriterion.LastUpdatedDate
    )
    papers = []
    for one_result in client.results(search):
        papers.append({
            'title': one_result.title,
            'authors': [author.name for author in one_result.authors],
            'summary': one_result.summary,
            # 'published': one_result.published,
            'id': one_result.entry_id,
            'url': one_result.pdf_url
        })
    return papers

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