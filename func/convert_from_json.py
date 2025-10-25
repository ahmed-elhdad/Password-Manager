import json
def convert_from_json(path):
    with open(path,"r+") as f:
        json_txt=f.read()
        if json_txt == "" or json_txt is None:
            print("no data in file")
            return
        python_txt=json.loads(json_txt)
        return python_txt