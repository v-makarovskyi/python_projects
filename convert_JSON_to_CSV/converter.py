import json

if __name__ == '__main__':
    try:
        with open('/Users/vladimir/Документы/IT/python_projects/convert_JSON_to_CSV/input.json', 'r') as f:
            data = json.loads(f.read())

        output = ','.join([*data[0]])
        for obj in data:
            output += f'\n{obj["Name"]},{obj["age"]},{obj["birthyear"]}'

        with open('/Users/vladimir/Документы/IT/python_projects/convert_JSON_to_CSV/output.csv', 'w') as f:
            f.write(output)
    
    except Exception as ex:
        print(f'Error: {str(ex)}')