import requests 

BASE_URL = "http://localhost:5000" 

def test_negative_post(): 
  response = requests.post(BASE_URL+"/users", json={}) 
  assert response.status_code == 400, "status code error" 
  data = response.json() 
  assert isinstance(data, dict), "body type error" 
  assert "error" in data, "error message not found"

