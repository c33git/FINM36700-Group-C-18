import json

with open('Homework 7_Catherine.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for i, cell in enumerate(nb['cells'][:5]):
    if cell['cell_type'] == 'code':
        source = ''.join(cell['source'])
        if 'excess_returns' in source:
            print(f"Cell {i}:")
            print(source)
            print("\n" + "="*50 + "\n")

