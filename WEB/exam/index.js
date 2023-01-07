

let index = 0;
const prev = document.querySelector('.prev')
const next = document.querySelector('.next')
const carousel = document.querySelector('.carousel')

// next 버튼을 누를 때마다 index 증가
next.addEventListener('click', () => {
    if (index = 2) return;
    index += 1;
    console.style.transform = 'translateX(-$(index * 100)vw)';

});
prev.addEventListener('click', () => {
    if (index == 0) return;
    index -= 1;
    console.style.transform = 'translateX(-$(index * 100)vw)';

});