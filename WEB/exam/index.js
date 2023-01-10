document.querySelector(".navbar-toggler").addEventListener("click", () => {
  //alert("버튼클릭");
  document.querySelector(".list-group").classList.toggle("show");
});

document.querySelector("ul.navbar-nav a").addEventListener("click", () => {
  document.querySelector(".black-bg").classList.add("show-modal");
});
document.querySelector("div.list-group a").addEventListener("click", () => {
  document.querySelector(".black-bg").classList.add("show-modal");
  document.querySelector(".list-group").classList.remove("show");
});

document.querySelector(".black-bg").addEventListener("click", (e) => {
  if (
    e.target == document.querySelector(".black-bg") ||
    e.target == document.querySelector("span.close")
  ) {
    document.querySelector(".black-bg").classList.remove("show-modal");
  }
});

document
  .querySelector("div.d-grid button.btn-primary")
  .addEventListener("click", (e) => {
    let id = document.querySelector("#userid");
    let pw = document.querySelector("#password");
    if (id.value == "") {
      alert("아이디를 입력해주세요");
      id.focus();
      e.preventDefault();
    } else if (pw.value.length < 6 || !/[A-Z]/.test(pw.value)) {
      alert("비밀번호를 확인해주세요");
      pw.focus();
      e.preventDefault();
    } else {
      document.querySelector("form").submit();
    }
  });
//transform:translateX(0)
let index = 0;
const prev = document.querySelector("button.prev");
const next = document.querySelector("button.next");
const carousel = document.querySelector(".carousel");
prev.addEventListener("click", () => {
  if (index == 0) return;
  index -= 1;
  carousel.style.transform = `translateX(-${index * 100}vw)`;
});
next.addEventListener("click", () => {
  if (index == 2) return;
  index += 1;
  carousel.style.transform = `translateX(-${index * 100}vw)`;
});
