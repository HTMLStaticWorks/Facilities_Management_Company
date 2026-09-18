import os
import re

files = ['index.html', 'about.html', 'blog.html', 'contact.html', 'home-2.html', 'industries.html']

injection = '''          </div>
          <div class="pt-4 flex justify-center gap-4 border-t border-gray-100 dark:border-gray-800 mt-4">
            <button class="theme-toggle w-12 h-12 flex items-center justify-center text-gray-500 hover:text-amber-600 dark:text-gray-400 dark:hover:text-amber-400 transition-colors rounded-full border-2 border-gray-500 dark:border-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800" aria-label="Toggle Theme">
              <i class="ph ph-moon text-2xl dark:hidden"></i>
              <i class="ph ph-sun text-2xl hidden dark:block"></i>
            </button>
            <button class="rtl-toggle w-12 h-12 flex items-center justify-center text-gray-500 hover:text-amber-600 dark:text-gray-400 dark:hover:text-amber-400 transition-colors text-base font-bold rounded-full border-2 border-gray-500 dark:border-gray-400 hover:bg-gray-100 dark:hover:bg-gray-800" aria-label="Toggle RTL">
              RTL
            </button>
          </div>
        </div>
      </div>
    </header>'''

for f in files:
    if os.path.exists(f):
        with open(f, 'r', encoding='utf-8') as file:
            content = file.read()
        
        # Hide desktop icons on mobile (if not already hidden)
        content = content.replace('class="theme-toggle w-10 h-10 flex', 'class="theme-toggle w-10 h-10 hidden lg:flex')
        content = content.replace('class="rtl-toggle w-10 h-10 flex', 'class="rtl-toggle w-10 h-10 hidden lg:flex')
        
        # Check if already injected
        if "pt-4 flex justify-center gap-4 border-t" not in content:
            # Add icons to mobile menu
            pattern = re.compile(r'</div>\s*</div>\s*</div>\s*</header>')
            if pattern.search(content):
                content = pattern.sub(injection, content)
                with open(f, 'w', encoding='utf-8') as file:
                    file.write(content)
                print(f"Updated {f}")
            else:
                print(f"Pattern not found in {f}")
        else:
            print(f"Already updated {f}")
