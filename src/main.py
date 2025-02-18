from src.agent import run_agent

thread_id = "1"

while True:
    user_input = input("\nHuman: ")
    run_agent(thread_id, user_input)