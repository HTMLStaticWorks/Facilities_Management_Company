import os
import re

files = ['index.html', 'about.html', 'blog.html', 'contact.html', 'home-2.html', 'industries.html']

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Regex to find the signup block and the icons block
        # Group 1: Signup block
        # Group 2: Icons block
        
        pattern = re.compile(
            r'(<div class="pt-4">\s*<a href="signup\.html" class="[^"]*">\s*Signup\s*</a>\s*</div>)\s*(<div class="pt-4 flex justify-center gap-4 border-t border-gray-100 dark:border-gray-800 mt-4">.*?</button>\s*</div>)',
            re.DOTALL
        )
        
        if pattern.search(content):
            # We want to put Group 2 BEFORE Group 1. We might want to remove the top border from the icons 
            # and instead add a border to the signup button container if needed, but let's just swap them first.
            
            # Let's adjust the styling: 
            # The icons block has: pt-4 border-t border-gray-100 dark:border-gray-800 mt-4
            # We will keep the border on the icons since they come after the links, 
            # but maybe we need some margin. Let's just swap them directly as a starting point.
            
            def replacer(match):
                signup_block = match.group(1)
                icons_block = match.group(2)
                # Remove border-t from icons if we move them up? The links above also have border-b, so maybe it's fine.
                # Actually, the links above have border-b. So no top border needed on icons.
                icons_block = icons_block.replace('border-t border-gray-100 dark:border-gray-800 mt-4', 'mt-4 pb-4 border-b border-gray-100 dark:border-gray-800')
                return icons_block + '\n          ' + signup_block
            
            new_content = pattern.sub(replacer, content)
            with open(f, 'w', encoding='utf-8') as file:
                file.write(new_content)
            print(f"Updated {f}")
        else:
            print(f"Pattern not found in {f}")
