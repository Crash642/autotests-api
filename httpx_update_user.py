import httpx

from tools.fakers import get_random_email


create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}
create_user_response = httpx.post("http://localhost:8000/api/v1/users", json=create_user_payload)
create_user_response_data = create_user_response.json()



login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()



get_user_headers = {
    "Authorization": f"Bearer {login_response_data['token']['accessToken']}"
}
patch_user_data = {
    "email": get_random_email(),
    "lastName": "UpdatedLastName",
    "firstName": "UpdatedFirstName",
    "middleName": "UpdatedMiddleName"
}

patch_user = httpx.patch(
    f"http://localhost:8000/api/v1/users/{create_user_response_data['user']['id']}",
    headers=get_user_headers,
    json=patch_user_data
)
print("Status code:", patch_user.status_code)
print('Patch user response:', patch_user.json())
