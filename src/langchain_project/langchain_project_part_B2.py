
from datetime import date
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

class NewReservation(BaseModel):
    cutomer_name: str
    party_size: int 
    time_slot: date


class CancelReservation(BaseModel):
    customer_name: str
    time_slot: date

from langchain.agents import create_agent
from langchain.agents.structured_output import ToolStrategy
from typing import Union

agent = create_agent(
    model = "openai:gpt-5-nano",
    response_format=ToolStrategy(Union[NewReservation, CancelReservation])
)

response1 = agent.invoke({
    "messages": [
        {"role": "user","content":"Hi, I am Rohit, reserve a table for 2 on 24th July 2026"},
    ]
})

response2 = agent.invoke({
    "messages": [
        {"role": "user", "content": "Hi I am Harshit, Cancel the booking for 24th July 2026"}
    ]
})

print(response1["structured_response"])

print("NEXT INVOKE call")

print(response2["structured_response"])