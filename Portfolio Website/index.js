let mouseCursor = document.querySelector(".cursor");
let navLinks = document.querySelectorAll(".nav-link");
let contentText = document.querySelectorAll(".text");
let college = document.querySelector(".college");

window.addEventListener('mousemove', cursor);

function cursor(e){
  mouseCursor.style.top = e.pageY + 'px';
  mouseCursor.style.left = e.pageX + 'px';
}

// For nav links
navLinks.forEach(link => {
  link.addEventListener('mouseover', () => {
    mouseCursor.classList.add('link-grow');
  });
  link.addEventListener('mouseleave', () => {
    mouseCursor.classList.remove('link-grow');
  });
});

// For contentText
contentText.forEach(text => {
  text.addEventListener('mouseover', () => {
    mouseCursor.style.borderColor = 'red';
    mouseCursor.classList.add('link-grow1');
  });
  text.addEventListener('mouseleave', () => {
    mouseCursor.style.borderColor = 'white';
    mouseCursor.classList.remove('link-grow1');
  });
});
