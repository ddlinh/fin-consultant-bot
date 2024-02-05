from langchain import OpenAI, ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.llms import OpenAI

model_name = "gpt-3.5-turbo-1106"

chat = OpenAI(model_name=model_name, temperature=0)

conversation = ConversationChain(
    llm=chat,
    verbose=True,
    memory=ConversationBufferMemory()
)