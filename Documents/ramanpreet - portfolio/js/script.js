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
  const currentHref = anchor.getAttribute("href");
  if (currentHref && currentHref !== "#" && currentHref.startsWith("http")) {
    return;
  }
  const heading = anchor.closest(".project").querySelector("h3").textContent.trim();
  const matchKey = Object.keys(CONFIG.repoUrls).find((key) => heading.includes(key));
  const url = matchKey ? CONFIG.repoUrls[matchKey] : currentHref;
  wireLink(anchor, url, "Repository link not added yet.");
});

const copyEmailBtn = document.getElementById("copy-email-btn");
if (copyEmailBtn) {
  copyEmailBtn.addEventListener("click", () => {
    navigator.clipboard.writeText("r.preet01@outlook.it").then(() => {
      showToast("Email copied to clipboard!");
    }).catch(() => {
      showToast("r.preet01@outlook.it");
    });
  });
}

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



// Certificate Modal & PDF Proof Viewer
const certModal = document.getElementById("cert-modal");
const certModalBackdrop = document.getElementById("cert-modal-backdrop");
const certModalClose = document.getElementById("cert-modal-close");
const certModalTitle = document.getElementById("cert-modal-title");
const certModalIframe = document.getElementById("cert-modal-iframe");
const certModalOpenLink = document.getElementById("cert-modal-open-link");
const certModalFallbackLink = document.getElementById("cert-modal-fallback-link");
let lastFocusedElement = null;

function openCertModal(pdfUrl, title, triggerEl) {
  if (!certModal) return;
  lastFocusedElement = triggerEl || document.activeElement;
  certModalTitle.textContent = title;
  certModalIframe.src = pdfUrl;
  certModalOpenLink.href = pdfUrl;
  certModalFallbackLink.href = pdfUrl;
  certModal.removeAttribute("hidden");
  document.body.style.overflow = "hidden";
  certModalClose.focus();
}

function closeCertModal() {
  if (!certModal || certModal.hasAttribute("hidden")) return;
  certModal.setAttribute("hidden", "");
  certModalIframe.src = "";
  document.body.style.overflow = "";
  if (lastFocusedElement && typeof lastFocusedElement.focus === "function") {
    lastFocusedElement.focus();
  }
}

document.querySelectorAll(".cert-badge").forEach((badge) => {
  badge.addEventListener("click", (event) => {
    // If user holds Ctrl, Cmd, Shift, or Alt, open normally in new tab
    if (event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) {
      return;
    }
    event.preventDefault();
    const pdfUrl = badge.getAttribute("data-pdf") || badge.getAttribute("href");
    const title = badge.getAttribute("data-title") || badge.textContent.trim();
    openCertModal(pdfUrl, title, badge);
  });
});

if (certModalClose) {
  certModalClose.addEventListener("click", closeCertModal);
}

if (certModalBackdrop) {
  certModalBackdrop.addEventListener("click", closeCertModal);
}

window.addEventListener("keydown", (event) => {
  if (event.key === "Escape" && certModal && !certModal.hasAttribute("hidden")) {
    closeCertModal();
  }
});
