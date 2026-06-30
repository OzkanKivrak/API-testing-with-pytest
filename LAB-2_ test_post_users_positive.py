import requests 

BASE_URL = "http://localhost:5000" 

def test_positive_post(): 
  response = requests.post(BASE_URL + "/users", json={"name":"automation"}) 
  assert response.status_code == 201, "failure status code" 
  data = response.json()
  print(type(data)) 
  assert data["message"] == "user created", "user not created" 
  print("server response:",data) 
  assert isinstance(data, dict), "response is not dict" 
