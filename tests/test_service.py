from unittest import mock

from src.services import _get_trends


def test_get_trends_with_success():
    # Arrange
    mock_api = mock.Mock()
    mock_api.trends_place.return_value = [
        {
            "trends": [
                {"name": "#EPJuliette", "url": "http://twitter.com/search?q=%23EPJuliette"},
                {"name": "Addison", "url": "http://twitter.com/search?q=Addison"},
            ]
        }
    ]

    # Act
    trends = _get_trends(woe_id=1000, api=mock_api)

    # Assert
    assert trends == [
        {"name": "#EPJuliette", "url": "http://twitter.com/search?q=%23EPJuliette"},
        {"name": "Addison", "url": "http://twitter.com/search?q=Addison"},
    ]


def test_get_trends_without_return_with_success():
    # Arrange
    mock_api = mock.Mock()
    mock_api.trends_place.return_value = [{"trends": []}]

    # Act
    trends = _get_trends(woe_id=1000, api=mock_api)

    # Assert
    assert trends == []
