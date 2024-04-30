import React from 'react';
import Header from './header';
import Navigation from './navigation';
import Footer from './footer';
const Layout = ({ children }) => {
    return (
<div className="App">
        <Header />
        <div className="navigationWrapper">
            <Navigation />
            <main>{children}</main>
        </div>
</div>
    );
};
export default Layout;
