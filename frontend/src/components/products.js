
import axios from 'axios';
import React, { useState , useEffect} from 'react';
import {Card , Button , Col , Row} from 'react-bootstrap'

function Product(props){

    const {productcode,productname,productvendor,productdescription} = props.prod
    console.log('code tcode')
    let key_list = ["productcode","productname","productscale","productvendor", "productdescription","quantityinstock","buyprice","msrp","productline"]
   return ( 
    <Col sm>
    <Card style={{ width: '18rem' }}>
    <Card.Body>
   <Card.Title>{productname}</Card.Title>
      <Card.Text>{productdescription}</Card.Text>
      <Button variant="primary">Buy</Button>
    </Card.Body>
  </Card>
  </Col>
   )
}


function Products(){
    const [state, setstate] = useState([]);
    
    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/products/').then(res =>{setstate(res.data)})        
    },[]);

const listItems = state.map((prod,index) =>
   <Product prod={prod} key= {index} id={index}></Product>
);
    return(
        <div>
            <h1>Our Products</h1>
            <Row>
            {listItems}
            </Row>
           
        </div>
    )
    }



export default Products