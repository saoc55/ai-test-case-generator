from generator.prompt_templates import format_prompt


def test_bdd_prompt_contains_feature_description():
    result = format_prompt("User can log in", [], output_format="bdd")
    assert "User can log in" in result


def test_bdd_prompt_contains_gherkin_keywords():
    result = format_prompt("User can log in", [], output_format="bdd")
    assert "Gherkin" in result or "Given" in result or "Scenario" in result


def test_tabular_prompt_contains_feature_description():
    result = format_prompt("User can log in", [], output_format="table")
    assert "User can log in" in result


def test_tabular_prompt_contains_table_structure():
    result = format_prompt("User can log in", [], output_format="table")
    assert "| ID |" in result


def test_examples_are_joined_with_separator():
    result = format_prompt("User can log in", ["example A", "example B"], output_format="bdd")
    assert "example A" in result
    assert "example B" in result


def test_empty_examples_fallback():
    result = format_prompt("User can log in", [], output_format="bdd")
    assert "No examples available." in result


def test_unknown_format_defaults_to_bdd():
    result = format_prompt("User can log in", [], output_format="unknown")
    assert "Gherkin" in result or "Given" in result or "Scenario" in result
