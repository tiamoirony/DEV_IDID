

let all_li = document.querySelectorAll(".tab-button");
let all_div = document.querySelectorAll(".tab-content");
all_li.forEach((li, idx) => {
  li.addEventListener("click", (e) => {
    all_li.forEach((item) => item.classList.remove("orange"));
    all_div.forEach((item) => item.classList.remove("show"));
    e.target.classList.add("orange");
    all_div[idx].classList.add("show");
  });
});


let select = document.querySelector(".form-select");
select.addEventListener("change", (e) => {
  let detail_option = "";
  if (e.target.value == "셔츠") {
    detail_option =
      '<option value="95">95</option>'+
      '<option value="100">100</option>'+
      '<option value="105">105</option>'+
      '<option value="110">110</option>';
  } else if (e.target.value == "바지") {
    detail_option =
    '<option value="26">26</option>'+
    '<option value="28">28</option>'+
    '<option value="32">32</option>'+
      '<option value="34">34</option>'+
      '<option value="36">36</option>';
  } else if (e.target.value == "신발") {
    detail_option =
      '<option value="250">250</option>'+
      '<option value="260">260</option>'+
      '<option value="270">270</option>'+
      '<option value="280">280</option>';
  }
  document.querySelector("form .form-select:nth-child(3)").innerHTML = detail_option;
  document.querySelector("form .form-select:nth-child(3)").classList.remove('form-hide') = detail_option;
  
});
