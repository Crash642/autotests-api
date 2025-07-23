import httpx



login_payload = {
  "email": "user@user.com",
  "password": "Qwerty123"
}

auth  = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = auth.json()

print("Status Code:", auth.status_code)
print("Response JSON:", login_response_data)

headers = {"Authorization": f"Bearer {login_response_data['token']['accessToken']}"}
me_get  = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

print("Status Code:", me_get.status_code)
print("Response JSON:", me_get.json())