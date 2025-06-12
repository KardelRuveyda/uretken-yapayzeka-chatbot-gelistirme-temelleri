from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.llms import HuggingFaceHub
import os

load_dotenv()

st.title("RAG Application with HuggingFace API")


loader = PyPDFLoader("attentionisallyouneed.pdf")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
docs = text_splitter.split_documents(data)


embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vectorstore = Chroma.from_documents(documents=docs,embedding=embeddings,persist_directory="./chroma_db")

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs= {"k" : 10})

llm =  HuggingFaceHub(repo_id="HuggingFaceH4/zephyr-7b-beta",model_kwargs ={"temperature":0.3, "max_new_tokens" :100 },
                      huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"))

query=st.chat_input("Say something:")
prompt = query

system_prompt = ("You are an assistant for question-answering tasks"
                 "Use the following pieces of retrieved context to answer"
                 "If you don't know the answer, say that you don't know"
                 "Use three sentences maximum and keep the answer corrects."
                 "\n\n"
                 "{context}"
                )

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",system_prompt),
        ("human","{input}")
    ]
)

if query:
    question_answer_chain = create_stuff_documents_chain(llm,prompt)
    rag_chain = create_retrieval_chain(retriever,question_answer_chain)
    response = rag_chain.invoke({"input":"What is encoder?"})

    st.write(response["answer"])