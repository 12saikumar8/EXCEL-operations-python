# You call requests.delete() with an API URL that contains the ID for the todo you would like to remove.
#  This sends a DELETE request to the REST API, which then removes the matching resource. 
#  After deleting the resource,
#  the API sends back an empty JSON object indicating that the resource has been deleted.

import requests
api_url="https://jsonplaceholder.typicode.com/todos/10"
response=requests.delete(api_url)
print(response.json())

print(response.status_code)