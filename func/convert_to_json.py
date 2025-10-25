def convert_to_json(txt):
    import json
    if txt=='':
        print("Valid data ^^ ")
        return
    json_txt=json.dumps(txt)
    return json_txt