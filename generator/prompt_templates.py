from langchain_core.prompts import PromptTemplate

# ---------------------------------------------------------------------------
# BDD Template — outputs Gherkin (Feature / Scenario / Given-When-Then)
# ---------------------------------------------------------------------------
BDD_TEMPLATE = PromptTemplate(
    input_variables=["feature_description", "examples"],
    template="""You are a senior QA engineer. Generate structured BDD test cases in Gherkin format for the following feature.

FEATURE DESCRIPTION:
{feature_description}

REFERENCE EXAMPLES (use these as format and style guidance):
{examples}

INSTRUCTIONS:
- Generate 3 to 5 test cases covering the happy path and key negative scenarios
- Use standard Gherkin syntax: Feature, Scenario, Given, When, Then, And
- Keep steps concrete and specific — avoid vague language
- Each Scenario must have a clear, descriptive title
- Output only the Gherkin block — no extra explanation

OUTPUT:
"""
)

# ---------------------------------------------------------------------------
# Tabular Template — outputs a Markdown table
# ---------------------------------------------------------------------------
TABULAR_TEMPLATE = PromptTemplate(
    input_variables=["feature_description", "examples"],
    template="""You are a senior QA engineer. Generate structured test cases in Markdown table format for the following feature.

FEATURE DESCRIPTION:
{feature_description}

REFERENCE EXAMPLES (use these as format and style guidance):
{examples}

INSTRUCTIONS:
- Generate 3 to 5 test cases covering the happy path and key negative scenarios
- Use exactly this table structure:
  | ID | Title | Preconditions | Steps | Expected Result |
- Number steps within the Steps cell (1. Do X  2. Do Y)
- Use IDs in the format TC-001, TC-002, etc.
- Output only the table — no extra explanation

OUTPUT:
"""
)


def format_prompt(
    feature_description: str,
    examples: list[str],
    output_format: str = "bdd"
) -> str:
    """
    Builds the final prompt string from a feature description,
    retrieved RAG examples, and the desired output format.

    examples (list[str]) are joined with a separator so the LLM sees
    each retrieved test case as a distinct reference block.

    output_format accepts "bdd" or "table" — anything else defaults to BDD.
    """
    examples_text = "\n\n---\n\n".join(examples) if examples else "No examples available."

    if output_format == "table":
        return TABULAR_TEMPLATE.format(
            feature_description=feature_description,
            examples=examples_text
        )
    return BDD_TEMPLATE.format(
        feature_description=feature_description,
        examples=examples_text
    )