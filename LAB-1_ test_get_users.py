import requests 

BASE_URL = "http://localhost:5000" 

def test_get_users(): 
  response = requests.get(BASE_URL + "/users" ) 
  assert response.status_code == 200 
  print(response.status_code) 
  data = response.json() 
  print(data) 
  assert isinstance(data, list) 
  assert len(data) > 0 
  print(response.status_code) 

