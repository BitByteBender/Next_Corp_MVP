document.addEventListener('DOMContentLoaded', () => {
  const navLinks = document.querySelectorAll('nav ul li a');
  navLinks.forEach((link) => {
    link.addEventListener('click', smoothScroll);
  });

  const lazyImages = document.querySelectorAll("img[loading='lazy']");
  lazyImages.forEach((img) => {
    img.addEventListener('load', () => {
      img.classList.add('loaded');
    });
  });

  const projectRepoButton = document.querySelector('.project-repo');
  projectRepoButton.addEventListener('click', () => {
    window.location.href = 'https://github.com/BitByteBender/Next_Corp_MVP.git';
  });
});

function smoothScroll(event) {
  event.preventDefault();
  const targetId = event.currentTarget.getAttribute('href').substring(1);
  const targetSection = document.getElementById(targetId);

  window.scrollTo({
    top: targetSection.offsetTop - document.querySelector('header').offsetHeight,
    behavior: 'smooth',
  });
}
