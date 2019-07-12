import json

def main():
    dict_path = "dicts/nttfreq.dict"
    with open(dict_path, 'r', encoding='utf-8') as f:
        dict_nttfreq = eval(f.read())
    json_path = "dicts/nttfreq.json"
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(dict_nttfreq, f, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    print('start')
    main()
    print('done')