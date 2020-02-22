
function handle_checkbox_event(e){   
  var checkedBoxes=document.querySelectorAll('input[name=ck]:checked');
    checked_item =[]
    for (i=0; i<checkedBoxes.length;i++){
       checked_item.push(checkedBoxes[i].value)
       console.log(checked_item)
     }
     console.log(checked_item)
     call_Api(checked_item)
     
     if (checked_item.length==0){
      fetch_data()

     }
}


function updateProductLines(){
  axios.get('http://127.0.0.1:8000/classic_app/getProducts').then(function (response) {
  product_line_div =  document.getElementById('check_boxes');
  //console.log(response.data.product_line);
  response.data.product_line.map(product_line_obj=(product_line)=>{

    product_line_div.innerHTML += `
    <div class="custom-control custom-checkbox custom-control-inline">
        <input type="checkbox" name = "ck" class="custom-control-input" value="${product_line}"  id="defaultInline${product_line}">
        <label class="custom-control-label" for="defaultInline${product_line}">${product_line}</label>
      </div>
    `
    console.log(product_line)

  })
})
}


function call_Api(checked_item){
 axios.get('http://127.0.0.1:8000/classic_app/getProducts').then( function(response){

  product_catalog =  document.getElementById('product_catalog')
  
  product_catalog.innerHTML = " "
 for (product in response.data.products){
    product_object = response.data.products[product]

    //console.log(product_object.productline)
    if (checked_item.indexOf(product_object.productline)>-1){
      
        product_catalog.innerHTML += 

`<div class="col-lg-4 col-md-6 mb-4">

<!--Card-->
<div class="card">

  <!--Card image-->
  <div class="view overlay">
      <img src="/static/${product_object.product_img[0]}"
          class="card-img-top" alt="">
      <a href="#">
          <div class="mask rgba-white-slight"></div>
      </a>
  </div>

  <!--Card content-->
  <div class="card-body">
      <!--Title-->
      <h4 class="card-title ">${product_object.productname}</h4>
      
      <!--Text-->
      <i class="fas fa-dollar-sign">${product_object.msrp*1000}</i>
      <a href="#!"class="btn btn-indigo btn-sm float-right">Buy</a>
  </div>

</div>
<!--/.Card-->

</div>`


    }
    
}
 }).catch(function (error) {console.log(error);})
 //console.log(data)
}


function fetch_data(){
      axios.get('http://127.0.0.1:8000/classic_app/getProducts').then(function (response) {
    
      for (product in response.data.products){
          product_object = response.data.products[product]
          //console.log(product_object.product_img[0])
          product_catalog =  document.getElementById('product_catalog')
          product_catalog.innerHTML += 
    
  `<div class="col-lg-4 col-md-6 mb-4">

    <!--Card-->
    <div class="card">

        <!--Card image-->
        <div class="view overlay">
            <img src="/static/${product_object.product_img[0]}"
                class="card-img-top" alt="">
            <a href="#">
                <div class="mask rgba-white-slight"></div>
            </a>
        </div>

        <!--Card content-->
        <div class="card-body">
            <!--Title-->
            <h4 class="card-title ">${product_object.productname}</h4>
            
            <!--Text-->
            <i class="fas fa-dollar-sign">${product_object.msrp*1000}</i>
            <a href="#!"class="btn btn-indigo btn-sm float-right">Buy</a>
        </div>

    </div>
    <!--/.Card-->

</div>`
  
      }
  })
  .catch(function (error) {
    // handle error
    console.log(error);
  })
  .then(function () {
    // always executed
  });
  }