import pytest
from fastapi.testclient import TestClient

from app.data.database import connect
from app.main import app


@pytest.fixture
def client() -> TestClient:
    return TestClient(app)


def test_health_endpoint_returns_ok(client: TestClient) -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_home_page_is_rendered_with_starter_content(client: TestClient) -> None:
    response = client.get("/")
    normalized_html = " ".join(response.text.split())

    assert response.status_code == 200
    assert response.headers["content-type"].startswith("text/html")
    assert "<title>Team and Guide Allocation</title>" in normalized_html
    assert "Allocation features are not implemented yet." in normalized_html
    assert "one capacity slot" in normalized_html
    assert "/static/app.js" in normalized_html


def test_static_javascript_is_served(client: TestClient) -> None:
    response = client.get("/static/app.js")

    assert response.status_code == 200
    assert "aria-expanded" in response.text


def test_sqlite_factory_returns_independent_connections_without_tables() -> None:
    first_connection = connect(":memory:")
    second_connection = connect(":memory:")
    try:
        assert first_connection is not second_connection
        assert first_connection.execute("PRAGMA foreign_keys").fetchone()[0] == 1
        assert first_connection.execute(
            "SELECT name FROM sqlite_master WHERE type = 'table'"
        ).fetchall() == []
    finally:
        first_connection.close()
        second_connection.close()
