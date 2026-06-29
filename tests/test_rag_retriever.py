from unittest.mock import MagicMock
from generator.rag_retriever import retrieve


def test_retrieve_returns_list_of_strings(mocker):
    mock_store = MagicMock()
    mock_store.similarity_search.return_value = [
        MagicMock(page_content="TC-001: example one"),
        MagicMock(page_content="TC-002: example two"),
    ]
    mocker.patch("generator.rag_retriever.get_vector_store", return_value=mock_store)
    result = retrieve("User can log in")
    assert isinstance(result, list)
    assert all(isinstance(r, str) for r in result)


def test_retrieve_respects_n_results(mocker):
    mock_store = MagicMock()
    mock_store.similarity_search.return_value = [
        MagicMock(page_content=f"TC-00{i}") for i in range(2)
    ]
    mocker.patch("generator.rag_retriever.get_vector_store", return_value=mock_store)
    result = retrieve("User can log in", n_results=2)
    assert len(result) <= 2


def test_retrieve_empty_result_does_not_crash(mocker):
    mock_store = MagicMock()
    mock_store.similarity_search.return_value = []
    mocker.patch("generator.rag_retriever.get_vector_store", return_value=mock_store)
    result = retrieve("User can log in")
    assert result == []
