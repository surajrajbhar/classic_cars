import React from 'react';
import './App.css';
import Header from './components/header'
import Products from './components/products'
import Orders from './components/orders'
import ProductsLines from './components/productlines'
import NotFoundPage from './components/NotFoundPage'

import { Route, Switch,Redirect } from "react-router-dom";
function App() {
  return (
    <div className="container-flud">
     <Header></Header>
     <ProductsLines></ProductsLines>
     
     <Switch>
     <Route path='/' exact component={Products}/>
     <Route path='/orders' component={Orders}/>
     <Route component={NotFoundPage}/> 
     </Switch>
    </div>
  );
}

export default App;
