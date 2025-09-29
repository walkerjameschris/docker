from chatlas import ChatOllama
from shiny.express import ui

chat_client = ChatOllama(
    model="llama3",
    base_url="http://ollama:11434"
)

ui.page_opts(
    title="treehouse",
    fillable=True,
    fillable_mobile=True,
)

chat = ui.Chat(
    id="chat",
    messages=["Hello! How can I help you today?"],
)

chat.ui()


@chat.on_user_submit
async def handle_user_input(user_input: str):
    response = await chat_client.stream_async(user_input)
    await chat.append_message_stream(response)
