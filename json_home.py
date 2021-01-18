# 1 json to text parser
# 2 json to yaml parser
# 3 Yaml to json parser
# 4 Yaml to text parser
import json
import yaml
with open("sample_json.json", "r") as file:
	data = json.load(file)

with open("text.txt", "w") as text_file:
	print(data, file=text_file)
with open("sample.yaml", "w") as yaml_file:
	yaml.dump(data, yaml_file)

with open("result_json.json", "w") as result:
	json.dump(data, result)
with open("result_text.txt", "w") as result_text:
	print(data, file=result_text)