
// querySelectorAll() li, div
const allLi = document.querySelectorAll(".tab-button");
const allDiv = document.querySelectorAll(".tab-content");

allLi.forEach((li, idx) => {
    console.log(li, idx);
    
    li.addEventListener("click", (e) => {
        // 모든 li orange 클래스명 제거
        allLi.forEach((item) => item.classList.remove("orange"));
        // 모든 div show 클래스명 제거
        allDiv.forEach((item) => item.classList.remove("show"));
        //현재 이벤트 대상 orange 클래스명과 div show 추가
        e.target.classList.add("orange");
        allDiv[idx].classList.add("show");
    });
});

// select 동작
// 셔츠 클릭 시 form-hide 클래스 제거 
document.querySelectorAll('.form-select').addEventListener('change',(e)=> {
    // document.querySelector('form .form-select:nth-child(3)').classList.remove('form-hide');

    const productDetail = document.querySelector('from .form-select:nth-child(3)');


    console.log(e.target.value);

    let value = e.target.value
    let options = '';

    if(value == '셔츠') {
        options += '<option>90</option>';
        options += '<option>95</option>';
        options += '<option>100</option>';
        options += '<option>105</option>';

    }else if(value =='신발'){
        options += '<option>26</option>';
        options += '<option>27</option>';
        options += '<option>28</option>';
        options += '<option>29</option>';

    }else if(value =='바지'){
        options += '<option>26</option>';
        options += '<option>27</option>';
        options += '<option>28</option>';
        options += '<option>29</option>';
    }

    productDetail.innerHTML= '';

    productDetail.innerHTML= options;

    productDetail.classList.remove('form-hide')

});