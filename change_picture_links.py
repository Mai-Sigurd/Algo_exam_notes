import os
import re

def update_markdown_links(directory):
    pattern = re.compile(r'!\[\[([^]]+)\]\]')
    replacement = r'![](\1)'
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                print(file)
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                updated_content = pattern.sub(replacement, content)

                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(updated_content)

# Usage
update_markdown_links('.')