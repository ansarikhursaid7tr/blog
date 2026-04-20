import { toggleCommentForm } from "./scripts/comment";

document.addEventListener("DOMContentLoaded", () => {
  // ── Theme Toggle ──
  const toggleBtn = document.getElementById("theme-toggle");
  if (toggleBtn) {
    const currentTheme = localStorage.getItem("theme") || 
                         (window.matchMedia("(prefers-color-scheme: light)").matches ? "light" : "dark");
                         
    if (currentTheme === "light") {
      document.documentElement.setAttribute("data-theme", "light");
    }

    toggleBtn.addEventListener("click", () => {
      let theme = document.documentElement.getAttribute("data-theme");
      if (theme === "light") {
        document.documentElement.removeAttribute("data-theme");
        localStorage.setItem("theme", "dark");
      } else {
        document.documentElement.setAttribute("data-theme", "light");
        localStorage.setItem("theme", "light");
      }
    });
  }

  // ── Active Nav Link ──
  document.querySelectorAll('.navbar nav ul a').forEach(link => {
    const linkHref = link.getAttribute("href");
    if (window.location.pathname === '/' && linkHref === "/") {
      link.classList.add('active');
    } else if (linkHref !== "/" && window.location.pathname.startsWith(linkHref)) {
      link.classList.add('active');
    }
  }); // Restored missing bracket for forEach loop
  
  // ── Terminal JSON Typing Animation ──
  const jsonEl = document.getElementById("animated-json");
  const jsonSource = document.getElementById("json-hidden");
  const jsonCursor = document.getElementById("json-cursor");

  if (jsonEl && jsonSource) {
    const jsonText = jsonSource.innerText.trim();
    let jsonIndex = 0;
    
    // Initial display config
    if(jsonCursor) jsonCursor.style.display = 'inline-block';
    
    function typeJson() {
      if (jsonIndex < jsonText.length) {
        jsonEl.textContent += jsonText.charAt(jsonIndex);
        jsonIndex++;
        setTimeout(typeJson, 10); // Extremely fast terminal output effect
      }
    }

    // Initialize Sequence
    setTimeout(typeJson, 300);
  }
});

export { toggleCommentForm };
