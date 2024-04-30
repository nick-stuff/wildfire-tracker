import React from 'react';
import { Link } from 'react-router-dom';
import logo from '../images/brushfire.png';
import '../images/logo.css';
const Header = () => {


return (
    <header className="image-container">
        <Link to="/"><img src={logo} alt="Bonfire Logo" /></Link>
    </header>
    );
};
export default Header;
