from func.convert_to_json import convert_to_json
def write_txt(path,txt):
    with open(path,"r+") as f:
        if txt=='':
            print("Valid txt")
            return
        json_txt=convert_to_json(txt)
        f.write(json_txt)