from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from dotenv import load_dotenv
from langchain.embeddings import OpenAIEmbeddings
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from dotenv import load_dotenv
import streamlit as st


load_dotenv()

st.title("RAG Application with OpenAI API")


loader = PyPDFLoader("calikusu.pdf")
data = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
docs = text_splitter.split_documents(data)


embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vectorstore = Chroma.from_documents(documents=docs,embedding=embeddings,persist_directory="./chroma_db")

retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs= {"k" : 10})

llm = ChatOpenAI(
    model="gpt-4o",
    temperature=0.3,
    max_tokens=500
)

query=st.chat_input("Say something:")
prompt = query

system_prompt = (
    "📖 Sen, Reşat Nuri Güntekin’in *Çalıkuşu* romanı üzerine uzman, cana yakın bir edebi asistansın. "
    "Görevin, kısa ama etkileyici analizler yapmak; karakterleri, temaları ve duyguları samimi bir dille yorumlamak 😊 "
    "Sadece bu roman hakkında konuş 🛑 Başka kitaplardan bahsetme. "
    "Yanıtların Türkçe olsun 🇹🇷 ve açıklamalarını emojilerle zenginleştir 📌"
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
    response = rag_chain.invoke({"input":"Feride kimdir?"})

    st.write(response["answer"])