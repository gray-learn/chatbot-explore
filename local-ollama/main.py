from   langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

# create template pass to llm
# multiple string
template = """
Answer the following questions:

Here is conversation history : {context}

Question: {question}

Answer: 
"""
model = OllamaLLM(model="llama3")
prompt = ChatPromptTemplate.from_template(template)
#  chain toghether
chain = prompt | model 
# prompt chain context # invoke model automatically
def handle_conversation():
    context = ""
    print("welcome to Gray Chatbot LLC, type 'exit' to quit")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            break
        # gen response
        # result = model.invoke(input="Hello world")
        result = chain.invoke({"context":context,"question":user_input})
        print("Bot: ", result)
        # f python 3.6
        context += f"\nUser:{user_input}\nAIBot:{result}"
        #  respond based on what we said before
if __name__  == "__main__":
    handle_conversation() # execute conversation