import json
from pathlib import Path

def combine_json_files(folder_path, output_file):
    combined_data = {'files': []}
    folder_path = Path(folder_path)

    for file_path in folder_path.glob('*.json'):
        with open(file_path, 'r') as f:
            data = json.load(f)

        if 'objects' in data:
            for obj in data['objects']:
                if 'class' in obj:
                    if obj['class'] == 'vehicle':
                        obj['class'] = 'car'
                    elif obj['class'] == 'license plate':
                        obj['class'] = 'number'

        combined_data['files'].append(data)

    with open(output_file, 'w') as f:
        json.dump(combined_data, f, indent=4)

# Usage example
folder_path = r'C:\path\to\json\folder'
output_file = r'C:\combined.json'
combine_json_files(folder_path, output_file)
