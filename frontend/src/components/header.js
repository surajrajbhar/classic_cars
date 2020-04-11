import React from 'react';
import {Card , Navbar , Nav , NavDropdown, Form, FormControl, Button} from 'react-bootstrap'
import {NavLink} from 'react-router-dom'



function Header(){
    return(
      <nav>
        <NavLink exact to='/'> Home</NavLink>
        {" | "}
        <NavLink to='/orders'> Orders</NavLink>
        {" | "}
        <NavLink to='/payments'> Payments</NavLink>
        {" | "}
        <NavLink to ='/login'> Login</NavLink>
         {" | "}
         <NavLink to='/signup'>Signup</NavLink>        
      </nav>
    )
}

export default Header