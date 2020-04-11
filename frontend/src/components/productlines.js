import React , {useState, useEffect} from 'react'
import  'react-bootstrap';
import axios from 'axios'

function ProductLines(props){
  const [state, setstate] = useState([]);
  const [prod_line, setProdline] = useState([])

  useEffect(() => {
     axios.get('http://127.0.0.1:8000/api/products/').then(res=>{setstate(res.data)})
  }, []);
   


  useEffect(() => {
    let prod_line = state.map(prod=>{
        return prod.productline
    }) 
    const unique_prod_line = [...new Set(prod_line)]
    setProdline(unique_prod_line)
    console.log('Do something after counter has changed', unique_prod_line);
 }, [state]);




  return(
  prod_line.map(prd=>(<div>{prd}</div>))
  )

}


export default ProductLines