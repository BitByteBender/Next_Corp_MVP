let slideIndex = 0;
showSlides();

function showSlides() {
  let slides = document.querySelectorAll('.slides img');
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none';
  }
  slideIndex++;
  if (slideIndex > slides.length) {
    slideIndex = 1;
  }
  slides[slideIndex - 1].style.display = 'block';
  setTimeout(showSlides, 5000); // Change image every 5 seconds
}

function plusSlides(n) {
  slideIndex += n;
  let slides = document.querySelectorAll('.slides img');
  if (slideIndex > slides.length) {
    slideIndex = 1;
  } else if (slideIndex < 1) {
    slideIndex = slides.length;
  }
  for (let i = 0; i < slides.length; i++) {
    slides[i].style.display = 'none';
  }
  slides[slideIndex - 1].style.display = 'block';
}

function scrollToSection(sectionId) {
  document.getElementById(sectionId).scrollIntoView({ behavior: 'smooth' });
}

document.getElementById('contactForm').addEventListener('submit', function (event) {
  event.preventDefault();
  alert('Thank you for your message!');
});

window.addEventListener('load', function () {
  const aboutSection = document.querySelector('.about');
  const featuresSection = document.getElementById('features');

  if (aboutSection && featuresSection) {
    const aboutHeight = aboutSection.offsetHeight;
    featuresSection.style.height = aboutHeight + 'px';
  }
});
