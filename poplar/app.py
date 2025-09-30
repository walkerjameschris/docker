import shinyswatch
from subprocess import run
from shiny.express import ui
from chatlas import ChatOllama

chat_client = ChatOllama(
    model="gemma3:12b",
    base_url="http://ollama:11434",
    system_prompt="You are a helpful general knowledge assistant running on a home server."
)

ui.page_opts(
    theme=shinyswatch.theme.darkly,
    fillable=True,
    fillable_mobile=True
)

chat = ui.Chat("poplar")
chat.ui(messages=[
    {
        "content": "My name is Poplar, the `treehouse` assistant.\n\nType `\status` to get server status.",
        "role": "assistant"
    }
])

@chat.on_user_submit
async def handle_user_input(user_input: str):
    if user_input == "\status":
        gpu = run("nvidia-smi", capture_output=True)
        user_input = f"""
        I want you to describe my server utilization in a very
        matter-of-fact format. Do not add additional context,
        just report statitics in a very user friendly way. I
        want to know temperatures and VRAM utilization: \n\n{gpu}
        """
    response = await chat_client.stream_async(user_input)
    await chat.append_message_stream(response)






