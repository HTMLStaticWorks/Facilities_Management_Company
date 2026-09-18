document.addEventListener('DOMContentLoaded', () => {
  // Theme Toggle
  const themeToggleBtns = document.querySelectorAll('.theme-toggle');
  
  // Check for saved theme preference or use system preference
  const savedTheme = localStorage.getItem('theme');
  const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
  
  if (savedTheme === 'dark' || (!savedTheme && prefersDark)) {
    document.documentElement.classList.add('dark');
  } else {
    document.documentElement.classList.remove('dark');
  }

  themeToggleBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      document.documentElement.classList.toggle('dark');
      if (document.documentElement.classList.contains('dark')) {
        localStorage.setItem('theme', 'dark');
      } else {
        localStorage.setItem('theme', 'light');
      }
    });
  });

  // RTL Toggle
  const rtlToggleBtns = document.querySelectorAll('.rtl-toggle');
  const savedDir = localStorage.getItem('dir');
  
  if (savedDir === 'rtl') {
    document.documentElement.setAttribute('dir', 'rtl');
  } else {
    document.documentElement.setAttribute('dir', 'ltr');
  }

  rtlToggleBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      const currentDir = document.documentElement.getAttribute('dir');
      if (currentDir === 'rtl') {
        document.documentElement.setAttribute('dir', 'ltr');
        localStorage.setItem('dir', 'ltr');
      } else {
        document.documentElement.setAttribute('dir', 'rtl');
        localStorage.setItem('dir', 'rtl');
      }
    });
  });

  // Mobile Menu
  const mobileMenuBtn = document.getElementById('mobile-menu-btn');
  const mobileMenu = document.getElementById('mobile-menu');
  const hamburger = document.querySelector('.hamburger');
  const mobileLinks = document.querySelectorAll('.mobile-link');

  if (mobileMenuBtn && mobileMenu) {
    mobileMenuBtn.addEventListener('click', () => {
      mobileMenu.classList.toggle('hidden');
      if(hamburger) hamburger.classList.toggle('open');
    });

    // Close menu when a link is clicked
    mobileLinks.forEach(link => {
      link.addEventListener('click', () => {
        mobileMenu.classList.add('hidden');
        if(hamburger) hamburger.classList.remove('open');
      });
    });
  }

  // Scroll to Top
  const scrollTopBtn = document.getElementById('scrollTopBtn');
  if (scrollTopBtn) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 300) {
        scrollTopBtn.classList.add('visible');
      } else {
        scrollTopBtn.classList.remove('visible');
      }
    });

    scrollTopBtn.addEventListener('click', () => {
      window.scrollTo({
        top: 0,
        behavior: 'smooth'
      });
    });
  }

  // Active Navigation Indication
  const currentPath = window.location.pathname.split('/').pop();
  const navLinks = document.querySelectorAll('.nav-link, .mobile-link');
  
  navLinks.forEach(link => {
    const href = link.getAttribute('href');
    if (href === currentPath || (currentPath === '' && href === 'index.html')) {
      link.classList.add('text-amber-600', 'dark:text-amber-500', 'font-semibold');
    }
  });

});

// Global form validation helper
function validateForm(formElement, callback) {
  if (!formElement) return;

  formElement.addEventListener('submit', (e) => {
    e.preventDefault();
    let isValid = true;

    // Basic required fields
    const requiredInputs = formElement.querySelectorAll('[required]');
    requiredInputs.forEach(input => {
      const group = input.closest('.form-group');
      if (!input.value.trim()) {
        isValid = false;
        if(group) group.classList.add('invalid');
      } else {
        if(group) group.classList.remove('invalid');
      }
    });

    // Password match (if applicable)
    const pwd = formElement.querySelector('input[name="password"]');
    const confirmPwd = formElement.querySelector('input[name="confirmPassword"]');
    
    if (pwd && confirmPwd) {
      if (pwd.value !== confirmPwd.value) {
        isValid = false;
        const confirmGroup = confirmPwd.closest('.form-group');
        if(confirmGroup) {
          confirmGroup.classList.add('invalid');
          const errorMsg = confirmGroup.querySelector('.form-error');
          if(errorMsg) errorMsg.textContent = 'Passwords do not match';
        }
      }
    }

    if (isValid && callback) {
      callback(formElement);
    }
  });
}
