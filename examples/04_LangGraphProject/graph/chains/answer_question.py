from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel,Field
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
class GradeAnswer(BaseModel):
    binary_score:bool = Field(
        description="Answer addresses the question 'yes' or 'no'"
    )

llm = ChatOpenAI(temperature=0)
structured_llm_grader = llm.with_structured_output(GradeAnswer)

system = """You are a grader assesing whether an answer addresses / resolves q quetsion \n 
Give a binary score 'yes' or 'no'. 'Yes' means that the answer resolves the question."""

answer_prompt = ChatPromptTemplate.from_messages(
    [
    ("system",system),
    ("human","User question: \n\n {question} \n\n LLM Generation: {generation}")
    ]
)

answer_grader : RunnableSequence = answer_prompt | structured_llm_grader

if __name__ == "__main__":
    question = "Türkiye'nin başkenti neresidir?"
    generation = "Türkiye'nin başkenti Trabzon'dur."

    result = answer_grader.invoke({
        "question":question,
        "generation":generation
    })

    print(result)