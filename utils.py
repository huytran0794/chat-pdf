from sentence_transformers import SentenceTransformer
import pinecone
from openai import OpenAI
import streamlit as st

OPEN_AI_KEY = "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"
indexName = 'langchain-chatbot-pdf-demo'

client = OpenAI(
    # This is the default and can be omitted
    api_key=OPEN_AI_KEY
)
model = SentenceTransformer('all-MiniLM-L6-v2')

pinecone.init(
    api_key="445535a3-d2a3-4ae1-9037-7322276f9a81",  # find at app.pinecone.io
    environment="gcp-starter"  # next to api key in console
)
index = pinecone.Index('langchain-chatbot-pdf-demo')


def find_match(input):
    input_em = model.encode(input).tolist()
    result = index.query(input_em, top_k=2, includeMetadata=True)
    return result['matches'][0]['metadata']['text']+"\n"+result['matches'][1]['metadata']['text']


def query_refiner(conversation, query):

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {'role': 'system', 'content': f"Given the following user query and conversation log, formulate a question that would be the most relevant to provide the user with an answer from a knowledge base.\n\nCONVERSATION LOG: \n{conversation}\n\nQuery: {query}\n\nRefined Query:"},
        ],
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    result = (response.choices)[0].message.content
    return result


def get_conversation_string():
    conversation_string = ""
    for i in range(len(st.session_state['responses'])-1):

        conversation_string += "Human: "+st.session_state['requests'][i] + "\n"
        conversation_string += "Bot: " + \
            st.session_state['responses'][i+1] + "\n"
    return conversation_string
