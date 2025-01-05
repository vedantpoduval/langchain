from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes
import uvicorn
import os
from dotenv import load_dotenv

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

app = FastAPI(
    title = "Langchain Server",
    version = "1.0",
    description="A simple API Server"
)


prompt1 = ChatPromptTemplate.from_template("Write me an essay about {topic} with 100 words")
prompt2 = ChatPromptTemplate.from_template("Write me an poem about {topic} with 100 words")

llm1 = OllamaLLM(model="llama2")
llm2 = OllamaLLM(model = "phi3")

output_parser = StrOutputParser()
add_routes(
    app,
    prompt1 | llm1 | output_parser,
    path = "/essay"
)
add_routes(
    app,
    prompt2 | llm2 | output_parser,
    path = "/poem"
)


if __name__== "__main__":
    uvicorn.run(app,host = "localhost",port=8000)