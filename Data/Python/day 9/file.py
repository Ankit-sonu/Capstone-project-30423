with open('input.txt', 'r') as infile:
    lines = infile.readlines()
    unique_lines = []
    seen = set()
    for line in lines:
        if line not in seen:
            unique_lines.append(line)
            seen.add(line)

with open('output.txt', 'w') as outfile:
    outfile.writelines(unique_lines)
