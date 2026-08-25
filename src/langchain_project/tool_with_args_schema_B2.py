from pydantic import BaseModel, Field
from typing import Literal

class OrderInput(BaseModel):
    dish_name: str
    quantity: int = Field(ge=1, le=10, description = "defines a dish name")
    delivery_or_pickup: Literal["delivery", "pickup"] = Field(default= "pickup", description = "Options for delivery.")

from langchain.tools import tool

@tool(args_schema=OrderInput)
def place_order():
    """ Place order tool plcaes dummy order """
    print("The tool has been called")

print(place_order.args)
