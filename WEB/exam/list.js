
// fetch('데이터를 가져올 경로')
// .then(도착한 데이터 원하는 타입으로 변경)
// .then(원하는 타입으로 변경됨)


document.querySelector('#more').addEventListener('click', () =>{
    fetch('./more1.json')
        .then((response) => response.json)
        .then((result) => {

            let products = '';

        
            result.forEach((item, idx) => {
             products += '<div class="col-sm-4">
             <img src="https://placehold.co/600" alt="" class="w-100" />
             <h5>${item.title}</h5>
             <p>가격 : ${item.price}</p>
             </div>';
             
        });

        document.querySelector('row').insertAdjacentHTML('beforeend', products)




    });
});