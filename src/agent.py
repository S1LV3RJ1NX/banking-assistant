from src.llm import llm
from src.banking_tools import tools
from src.prompt import prompt_template

from langgraph.prebuilt import create_react_agent
from langgraph.checkpoint.memory import MemorySaver

memory = MemorySaver()

agent = create_react_agent(
    model=llm, 
    tools=tools, 
    state_modifier=prompt_template,
    checkpointer=memory
)


def print_stream(stream):
    for s in stream:
        message = s["messages"][-1]
        if isinstance(message, tuple):
            print(message)
        else:
            message.pretty_print()

def run_agent(thread_id: str, user_input: str):

    config = {"configurable": {"thread_id": thread_id}}
    inputs = {"messages": [("user", user_input)]}

    print_stream(agent.stream(inputs, config=config, stream_mode="values"))