from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel,Field
from langchain_core.runnables import RunnableSequence
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(temperature=0)

class GradeHallucinations(BaseModel):
    binary_score:bool = Field(
        description="Answer is gorunded in the facts, 'yes' or 'no'"
    )


structured_llm_grader = llm.with_structured_output(GradeHallucinations)

system = """You are a grader assessing whether an LLM generation is grounded in / supported by a set of retrieved facts. 
   Give a binary score 'yes' or 'no'. 'Yes' means that the answer is the grounded in / supported by the set of facts"""

hallucination_prompt = ChatPromptTemplate.from_messages(
    [
        ("system",system),
        ("human", "Set of facts : \n\n {documents} \n\n LLM generation: {generation}")
    ]
)

hallucination_grader = RunnableSequence = hallucination_prompt | structured_llm_grader

if __name__ == "__main__":
    documents = "Rüyada köpek görmek içsel korkuları simgeler."
    generation = "Rüyada köpek görmek , kişinin içsel korkularını simgeler."

    result = hallucination_grader.invoke({
        "documents":documents,
        "generation":generation
    })

    print(result)