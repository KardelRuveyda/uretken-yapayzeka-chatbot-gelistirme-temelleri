import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'../../')))

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel,Field
from langchain_openai import ChatOpenAI
from ingestion import retriever

llm = ChatOpenAI(temperature=0)

class GradeDocuments(BaseModel):
    binary_score: str = Field(description="yes or no")

structured_llm_grader = llm.with_structured_output(GradeDocuments)

system = """You are a grader assesing relavence of retrieved document to a user question.
If the document contains keyword(s) or semantic meaning related to the question, grade it 
as relavant. Give a binary score 'yes' or 'no' score to indicate whether the document is relevant the question."""

grade_prompt = ChatPromptTemplate.from_messages(
    [
        ("system",system),
        ("human","Retrieved document : \n\n {document} \n\n User Question: {question}")
    ]
)

retrieval_grader = grade_prompt | structured_llm_grader

if __name__ == '__main__':
    user_question = "üyamda deniz ile ilgili bir durum yaşadım."
    docs = retriever.get_relevant_documents(user_question)
    retrieved_document= docs[0].page_content

    print(retrieval_grader.invoke(
        {"question":user_question, "document":retrieved_document}
    ))