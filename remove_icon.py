import os

files = ['index.html', 'about.html', 'blog.html', 'contact.html', 'home-2.html', 'industries.html']

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Replace the signup icon
        if 'Signup <i class="ph ph-sign-in"></i>' in content:
            content = content.replace('Signup <i class="ph ph-sign-in"></i>', 'Signup')
            with open(f, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Updated {f}")
        else:
            print(f"Pattern not found in {f}")
