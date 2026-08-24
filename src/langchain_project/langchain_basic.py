from langchain.agents import create_agent
import os, json 
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str) -> str:
    """
        Get weather for a given city.
    """
    return f"It's always sunny in {city}!"

agent = create_agent(
    model = "openai:gpt-5.5",
    tools = [get_weather],
    system_prompt = "you are a helpful assistant",
)

result = agent.invoke(
    {
        "messages": [
            {
                "role": "user", 
                "content": "What's the weather in Bangalore?"
            }
        ]
    }
)

print(result["messages"][-1].content_blocks)

# print(result)

# messages_json = [msg.model_dump() for msg in result["messages"]]
# print(json.dumps(messages_json, indent=2))