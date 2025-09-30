import shinyswatch
from subprocess import run
from shiny.express import ui
from chatlas import ChatOllama

messages = [
    {
        "content": "You are a helpful general knowledge assistant running on a home server.",
        "role": "system"
    },
    {
        "content": "My name is Poplar, the `treehouse` assistant. Type \status to get server status",
        "role": "assistant"
    }
]

chat_client = ChatOllama(
    model="llama3",
    base_url="http://ollama:11434"
)

ui.page_opts(
    theme=shinyswatch.theme.darkly,
    fillable=True,
    fillable_mobile=True
)

chat = ui.Chat("poplar")
chat.ui(messages=messages)


@chat.on_user_submit
async def handle_user_input(user_input: str):
    if user_input == "\status":
        gpu = run("nvidia-smi", capture_output=True)
        user_input = f"Tell me about my GPU utilization in a nice list: {gpu}"
    response = await chat_client.stream_async(user_input)
    await chat.append_message_stream(response)


