function showToast(message) {
  const toast = document.getElementById("toast");
  toast.textContent = message;
  toast.classList.add("show");
  window.setTimeout(() => toast.classList.remove("show"), 2600);
}

function wireLink(anchor, url, message) {
  if (url) {
    anchor.href = url;
    return;
  }

  anchor.addEventListener("click", (event) => {
    event.preventDefault();
    showToast(message);
  });
}

document.querySelectorAll(".resume-link").forEach((anchor) => {
  wireLink(anchor, CONFIG.resumeUrl, "Resume link not added yet.");
});

document.querySelectorAll(".repo-link").forEach((anchor) => {
  const projectName = anchor.closest(".project").querySelector("h3").textContent;
  wireLink(anchor, CONFIG.repoUrls[projectName], "Repository link not added yet.");
});

const burger = document.getElementById("burger");
const links = document.getElementById("links");

burger.addEventListener("click", () => {
  const isOpen = links.classList.toggle("open");
  burger.setAttribute("aria-expanded", String(isOpen));
});

links.addEventListener("click", (event) => {
  if (event.target.closest("a")) {
    links.classList.remove("open");
    burger.setAttribute("aria-expanded", "false");
  }
});

document.getElementById("yr").textContent = new Date().getFullYear();

const revealElements = document.querySelectorAll(".reveal");
if ("IntersectionObserver" in window) {
  const revealObserver = new IntersectionObserver((entries, observer) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("in");
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  revealElements.forEach((element) => revealObserver.observe(element));
} else {
  revealElements.forEach((element) => element.classList.add("in"));
}

const sectionLinks = document.querySelectorAll('.links a[href^="#"]');
const sections = document.querySelectorAll("main section[id]");

function setActiveSection(sectionId) {
  sectionLinks.forEach((link) => {
    if (link.hash === `#${sectionId}`) {
      link.setAttribute("aria-current", "location");
    } else {
      link.removeAttribute("aria-current");
    }
  });
}

if ("IntersectionObserver" in window) {
  const sectionObserver = new IntersectionObserver((entries) => {
    const visibleEntries = entries.filter((entry) => entry.isIntersecting);
    if (visibleEntries.length) {
      const currentSection = visibleEntries.reduce((closest, entry) =>
        Math.abs(entry.boundingClientRect.top) < Math.abs(closest.boundingClientRect.top)
          ? entry
          : closest
      );
      setActiveSection(currentSection.target.id);
    }
  }, { rootMargin: "-20% 0px -65% 0px", threshold: 0 });

  sections.forEach((section) => sectionObserver.observe(section));
} else {
  setActiveSection("home");
}
