import json

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0,"felineIQ": null}'
json_data_as_python_value = json.loads(stringOfJsonData)
print(json_data_as_python_value)


