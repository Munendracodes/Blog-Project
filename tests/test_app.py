from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_user_register_and_login():
    print("\n=== Creating user ===")
    response = client.post("/users/", json={
        "email": "test4@example.com",
        "password": "test123"
    })
    print("Response:", response.status_code, response.json())
    assert response.status_code == 200
    assert "id" in response.json()

    print("\n=== Logging in user ===")
    login_response = client.post("/login", data={
        "username": "test4@example.com",
        "password": "test123"
    }, headers={"Content-Type": "application/x-www-form-urlencoded"})

    print("Login response:", login_response.status_code, login_response.json())
    assert login_response.status_code == 200
    token_data = login_response.json()
    assert "access_token" in token_data

def test_create_blog():
    print("\n=== Logging in again for blog creation ===")
    login_response = client.post("/login", data={
        "username": "test4@example.com",
        "password": "test123"
    }, headers={"Content-Type": "application/x-www-form-urlencoded"})

    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    print("Token:", token)

    print("\n=== Creating blog ===")
    blog_response = client.post("/blogs/", json={
        "title": "First Blog 4",
        "content": "This is my blog 4"
    }, headers=headers)

    print("Blog response:", blog_response.status_code, blog_response.json())
    assert blog_response.status_code == 200
    assert blog_response.json()["title"] == "First Blog 4"
    