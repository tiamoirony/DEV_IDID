

// 더보기 기능 

let index = 0;
document.querySelector("#more").addEventListener("click", (e) => {
  index += 1;
  let data = index == 1 ? "more1.json" : "more2.json";
  let p = "";
  fetch(data)

    .then((response) => response.json())
    .then((product) => {
      for (i = 0; i < product.length; i++) {
        p += `<div class="col-sm-4">
        <img src="https://placehold.co/600" alt="" class="w-100" />
        <h5>${product[i].title}</h5>
        <p>가격 : ${product[i].price}</p>
      </div>`;
      }
      document.querySelector(".row").insertAdjacentHTML("beforeend", p);
      if (index == 2) {
        e.target.disabled = true;
      }
    });
});
