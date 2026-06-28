from generator.llm_client import get_llm
from generator.rag_retriever import retrieve
from generator.prompt_templates import format_prompt

def generate(feature_description: str, output_format: str = "bdd", model: str = None) -> str:
    """
    Main generation pipeline. Orchestrates the full RAG -> prompt -> LLM flow
    
    Steps:
    1. retrieve()      - finds the 3 most similar test caase templates from ChromaDB
    2. format_prompt() - builds the final prompt string with feature + examples
    3. llm.invoke()    - sends the prompt to claude and returns the response

    output_fomrmat: "bdd" (Gherkin) or "table" (markdown table)
    model: optional override - defaults to LLM_MODEL in .env
    """

    examples = retrieve(feature_description)
    prompt = format_prompt(feature_description, examples, output_format)
    llm = get_llm(model = model)
    response = llm.invoke(prompt)
    return response.content

