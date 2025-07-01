# tests/test_blogs.py

def test_create_blog(auth_client):
    response = auth_client.post(
        "/blogs/",
        json={"title": "Test Blog", "content": "This is a test blog"}
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Blog"
    assert data["content"] == "This is a test blog"
