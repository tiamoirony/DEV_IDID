document.querySelector("div.index").addEventListener("click", () => {
    document.querySelector(".black-bg").classList.add("show-modal");
  });
  
// document.querySelector(".col-sm-4 .jinro").addEventListener("click", () => {
//     document.querySelector(".black-bg").classList.add("show-modal");
      // document.querySelector(".list-group").classList.remove("show");
  // });
  
document.querySelector(".black-bg").addEventListener("click", (e) => {
    if (
      e.target == document.querySelector(".black-bg") ||
      e.target == document.querySelector("span.close")
    ) {
      document.querySelector(".black-bg").classList.remove("show-modal");
    }
  });
  

  function count(type)  {
    // 결과를 표시할 element
    const resultElement = document.getElementById('result');
    
    // 현재 화면에 표시된 값
    let number = resultElement.innerText;
    
    // 더하기/빼기
    if(type === 'plus') {
      number = parseInt(number) + 1;
    }else if(type === 'minus')  {
      number = parseInt(number) - 1;
    }
    
    // 결과 출력
    resultElement.innerText = number;
  }