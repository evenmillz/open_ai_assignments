


// Lazy loading for all flower images
document.addEventListener("DOMContentLoaded", () => {
  const images = document.querySelectorAll("section img");
  images.forEach((img) => {
    img.setAttribute("loading", "lazy");
  });
});

// Lightbox functionality
document.addEventListener("DOMContentLoaded", () => {
  const lightbox = document.createElement("div");
  lightbox.id = "lightbox";
  document.body.appendChild(lightbox);

  const images = document.querySelectorAll("section img");
  images.forEach(image => {
    image.addEventListener("click", () => {
      lightbox.classList.add("active");
      const img = document.createElement("img");
      img.src = image.src;
      while (lightbox.firstChild) {
        lightbox.removeChild(lightbox.firstChild);
      }
      lightbox.appendChild(img);
    });
  });

  lightbox.addEventListener("click", () => {
    lightbox.classList.remove("active");
  });
});

// Scroll to top button
document.addEventListener("DOMContentLoaded", () => {
  const scrollBtn = document.createElement("button");
  scrollBtn.id = "scrollToTop";
  scrollBtn.textContent = "↑";
  document.body.appendChild(scrollBtn);

  scrollBtn.style.display = "none";

  window.addEventListener("scroll", () => {
    scrollBtn.style.display = window.scrollY > 300 ? "block" : "none";
  });

  scrollBtn.addEventListener("click", () => {
    window.scrollTo({ top: 0, behavior: "smooth" });
  });
});