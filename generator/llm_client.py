from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
import os

load_dotenv()

def get_llm(model=None, temperature=0):

    """
    Returns a LangChain-wrapped Claude model.

    temperature=0.2 keeps output deterministic and consistent —
    important for structured formats like Gherkin where we want
    the same structure every time, not creative variation.

    model defaults to whatever is in .env (claude-haiku-4-5),
    but can be overridden via the --model CLI flag later.
    """

    model = model or os.getenv("LLM_MODEL", "claude_haiku-4-5")
    return ChatAnthropic(
        model=model,
        temperature=temperature,
        api_key=os.getenv("ANTHROPIC_API_KEY")  # ← correct spelling
    )