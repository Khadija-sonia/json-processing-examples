import json
import os

def convert_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = json.load(f)

    formatted_data = {}
    formatted_data['filename'] = os.path.basename(input_file).split('.')[0]
    formatted_data['objects'] = []

    if 'vehicle' in data:
        formatted_data['objects'].append({
            'class': 'car',
            'presence': True if data['vehicle'] else False
        })

    if 'license plate' in data:
        formatted_data['objects'].append({
            'class': 'number',
            'presence': True if data['license plate'] else False
        })

    with open(output_file, 'w') as f:
        json.dump(formatted_data, f, indent=4)

# Usage example
input_file = r'C:\pos_0.png.json'
output_file = r'C:\formatted_pos_0.png.json'
convert_json(input_file, output_file)
