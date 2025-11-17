import json

# Read the notebook
with open('Homework 7_Catherine.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

# Find the cell with the excess returns calculation
for i, cell in enumerate(nb['cells']):
    if cell['cell_type'] == 'code':
        source_str = ''.join(cell['source'])
        if 'excess_returns = total_returns.sub(risk_free_rate' in source_str:
            print(f"Found cell at index {i}")
            # Find the line to replace
            new_source = []
            skip_next = False
            for j, line in enumerate(cell['source']):
                if '# Calculate excess returns by subtracting risk-free rate from each column' in line:
                    # Add conversion before calculation
                    new_source.append('# Convert annualized risk-free rate to monthly (divide by 12)\n')
                    new_source.append('# Since total_returns are monthly, we need to convert annualized RF rate to monthly\n')
                    new_source.append("risk_free_rate_monthly = risk_free_rate['TBill 3M'] / 12\n")
                    new_source.append('\n')
                    new_source.append('# Calculate excess returns by subtracting monthly risk-free rate from each column\n')
                    # Replace the calculation line
                    skip_next = True
                    continue
                elif skip_next and 'excess_returns = total_returns.sub(risk_free_rate' in line:
                    # Replace with monthly version
                    new_source.append("excess_returns = total_returns.sub(risk_free_rate_monthly, axis=0)\n")
                    skip_next = False
                    continue
                else:
                    new_source.append(line)
            
            cell['source'] = new_source
            print("Updated cell")
            break

# Write the notebook back
with open('Homework 7_Catherine.ipynb', 'w', encoding='utf-8') as f:
    json.dump(nb, f, ensure_ascii=False, indent=1)

print("Done!")

