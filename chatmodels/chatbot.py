from transformers import pipeline
from langchain_core.messages import AIMessage,SystemMessage,HumanMessage
chatbot = pipeline(
    "text-generation",
    model = "Qwen/Qwen2.5-1.5B-Instruct"
)
print("Bot: Hello krushik alekya always loves you! Type 0 to exit.")
while True:
    prompt = input("You: ")
    if prompt == "0":
        break
    messages = [
        {"role": "system", "content": "you are a funny AI agent"},
        {"role": "user", "content": prompt}
    ]
    response = chatbot(
        messages,
        max_new_tokens=100,
        do_sample=True,
        temperature=0.7
    )
    print("Bot:", response[0]["generated_text"][-1]["content"])
