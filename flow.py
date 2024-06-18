import os

from dotenv import load_dotenv
from pathlib import Path
from promptflow.tracing import trace
from promptflow.core import Prompty

BASE_DIR = Path(__file__).absolute().parent

"""
Tracing is a powerful tool that offers developers an in-depth understanding of the execution process of their generative AI applications such as agents, AutoGen, and retrieval augmented generation (RAG) use cases. It provides a detailed view of the execution flow, including the inputs and outputs of each node within the application.
"""
@trace
def chat(question: str = "What's the capital of France?") -> str:
    """Flow entry function."""

    if "OPENAI_API_KEY" not in os.environ and "AZURE_OPENAI_API_KEY" not in os.environ:
        # load environment variables from .env file
        load_dotenv()

    prompty = Prompty.load(source=BASE_DIR / "chat.prompty")
    # trigger a llm call with the prompty obj
    output = prompty(question=question)
    return output