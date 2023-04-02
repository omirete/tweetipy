with open('README_Template.md', 'r', encoding='utf-8') as f:
    template = f.readlines()

readme = ''

for line in template:
    if line.startswith('_fill_with_contents_of:'):
        start = len('_fill_with_contents_of:')
        filepath = line[start:].strip()
        with open(filepath, 'r', encoding='utf-8') as f:
            readme += f.read()
    else:
        readme += line

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)
