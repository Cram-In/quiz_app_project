from quiz import client
from unittest.mock import Mock


def test_get_me_question(monkeypatch):
    mock_question_category = "Smoki"
    category_question_mock = Mock()
    category_question_mock.return_value.mock_question_category
    monkeypatch.setattr("client.Category", mock_question_category)
    question_category = client.get_me_question(550)
    assert question_category == mock_question_category
