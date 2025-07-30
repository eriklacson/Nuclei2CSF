# Convert Nuclei JSON output to CSV format for CSF integration

import json
import csv

#read Nuclie JSON output
def read_json(): 
    # Input file containing Nuclei JSON output
    input_file = 'nuclei_output.json'

    # 1. Read from a .json file and parse into a Python dict/list
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

#parse data 
def parse_data(data):
    """
    Parse the Nuclei JSON data and convert it to a list of dictionaries.
    Each dictionary represents a finding with relevant fields.
    """
    findings = []
    for entry in data:
        finding = {
            'timestamp': entry.get('timestamp'),
            'host': entry.get('host'),
            'template_id': entry.get('templateID'),
            'severity': entry.get('info', {}).get('severity'),
            'matcher_name': entry.get('matcher_name', ''),
            'description': entry.get('info', {}).get('name'),
            'matched_url': entry.get('matched', ''),
        }
        findings.append(finding)
    return finding

# Convert Nuclei JSON output to CSV format for CSF integration
def convert_to_csv(findings, output_file='findings.csv'):
    """
    Convert the list of findings to a CSV file.
    """
    fields = ['timestamp', 'host', 'template_id', 'severity', 'matcher_name', 'description', 'matched_url']
    
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields)
        writer.writeheader()
        for finding in findings:
            writer.writerow(finding)

