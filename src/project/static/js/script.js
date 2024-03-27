const toggle = document.querySelector('.nav-bar #nav-toggle');
const nav = document.querySelectorAll('.nav-bar .nav-collaps');
toggle.addEventListener('click',function(){
   nav.forEach(col=>col.classList.toggle('nav-collaps-show'))
})
