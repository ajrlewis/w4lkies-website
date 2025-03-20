const aboutUsSection = document.querySelector('.about-us');
window.addEventListener('scroll', () => {
  if (aboutUsSection.getBoundingClientRect().top < window.innerHeight) {
    aboutUsSection.classList.add('about-us-reveal');
  }
});

var serviceSections = document.querySelectorAll('.service');
console.log('serviceSections = ', serviceSections);
window.addEventListener('scroll', () => {
  serviceSections.forEach((serviceSection) => {
    if (serviceSection.getBoundingClientRect().top < window.innerHeight) {
      serviceSection.classList.add('service-reveal');
    }
  });
});