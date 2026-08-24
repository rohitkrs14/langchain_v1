from dotenv import load_dotenv

from langchain.agents import create_agent

import pprint

load_dotenv()

import urllib

from langchain.tools import tool

def get_whether(city: str) -> str:
    """
        Get Whether for a given city.
    """ 
    return f"It's always sunny in {city}!"

def fetch_text_from_url(url: str) -> str:
    """
        Fetch the document from a URL.
    """
    req = urllib.request.Request(
        url, 
        headers= {"User-Agent": "Mozilla/5.0 (compatible; quickstart-research/1.0)"},
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            raw = resp.read()
    except urllib.error.URLError as e:
        return f"Fetch failed: {e}"
    text = raw.decode("utf-8", errors = "replace")
    return text


agent = create_agent(
    model = "openai:gpt-5-nano",
    tools = [get_whether, fetch_text_from_url],
    system_prompt="You are a helpful assistant",
)

result = agent.invoke({
    "messages": {
        "role": "user",
        "content": "Hey, I am Stephen, extract page title from google.com?"
    }
})

print(result["messages"][-1].content_blocks)

# print(result)