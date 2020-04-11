import axios from 'axios'

import React, { useState , useEffect} from 'react';
import {Card , Button , Col , Row} from 'react-bootstrap'


function Orders(){
    const [state, setstate] = useState([]); 
    useEffect(() => {
        axios.get('http://127.0.0.1:8000/api/orders/').then(res=>{setstate(res.data)})
    }, []);

    const orderitems = state.map((order,index) =><Order prod={order} key= {index} id={index}></Order>);
    return(
    <Row>
      
    {orderitems}
    </Row>    
    )
}



function Order(props){
    const {ordernumber,orderdate,requireddate,shippeddate,status,comments,customernumber} = props.prod
    return(
        <Col sm>
        <Card style={{ width: '18rem' }}>
        <Card.Body>
       <Card.Title>{ordernumber}</Card.Title>
          <Card.Text>{orderdate}</Card.Text>
          <Card.Text>{requireddate}</Card.Text>
          <Card.Text>{shippeddate}</Card.Text>
          <Card.Text>{status}</Card.Text>
          <Card.Text>{comments}</Card.Text>


        </Card.Body>
      </Card>
      </Col>
    )
}


export default Orders
