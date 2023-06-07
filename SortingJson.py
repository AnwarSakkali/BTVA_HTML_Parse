import json

def sortKeysByNameInJson(url):
    # Read the JSON file
    with open(url, encoding='utf-8') as file:
        data = json.load(file)

    # Sort the dictionary keys alphabetically
    sorted_keys = sorted(data.keys())

    # Create a new dictionary with the sorted keys
    sorted_data = {key: data[key] for key in sorted_keys}

    # Write the sorted dictionary back to a JSON file
    with open(url, 'w') as file:
        json.dump(sorted_data, file, indent=4)
    
    print("finished sorting keys by name")

def sortValuesByNameInJson(url):
    with open(url) as file:
        json_data = json.load(file)

    # Iterate over the keys in the JSON data
    for key in json_data:
        values = json_data[key]
        sorted_values = sorted(values)
        json_data[key] = sorted_values

    # Write the updated JSON data to a file
    with open(url, "w") as file:
        json.dump(json_data, file)

    print("finished sorting values by name")

def sortKeysBySurnameInJson(url):
    import json
    from unidecode import unidecode

    # The JSON snippet
    with open(url, 'r', encoding="UTF-8") as file:
        json_str = file.read()

    json_data = json.loads(json_str)

    # Sort the JSON based on surnames
    sorted_data = dict(sorted(json_data.items(), key=lambda x: unidecode(x[0].split()[-1])))

    # Write the updated JSON data to a file
    with open(url, "w") as file:
        json.dump(sorted_data, file)

    print("finished sorting keys by surname")

def readEncodedTextTest(url):
    import json

    # Read the JSON file
    with open(url, 'r', encoding='utf-8') as file:
        json_str = file.read()

    # Decode the Unicode characters from the JSON string
    decoded_json = json.loads(json_str)

    # Access the decoded data
    for key, value in decoded_json.items():
        # Print the key and values
        print(key + ":")
        for item in value:
            print("  -", item)