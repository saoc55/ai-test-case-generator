from generator.pipeline import generate


def test_bdd_generation_returns_scenario(mocker):
    mocker.patch("generator.pipeline.retrieve", return_value=["TC-001: example"])
    mock_llm = mocker.patch("generator.pipeline.get_llm")
    mock_llm.return_value.invoke.return_value.content = "Scenario: User logs in\n  Given the login page"
    result = generate("User can log in", output_format="bdd")
    assert "Scenario" in result


def test_tabular_generation_returns_table(mocker):
    mocker.patch("generator.pipeline.retrieve", return_value=["TC-001: example"])
    mock_llm = mocker.patch("generator.pipeline.get_llm")
    mock_llm.return_value.invoke.return_value.content = "| ID | Title | Steps | Expected Result |"
    result = generate("User can log in", output_format="table")
    assert "|" in result


def test_pipeline_returns_string(mocker):
    mocker.patch("generator.pipeline.retrieve", return_value=[])
    mock_llm = mocker.patch("generator.pipeline.get_llm")
    mock_llm.return_value.invoke.return_value.content = "some output"
    result = generate("User can log in")
    assert isinstance(result, str)
