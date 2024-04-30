import React, { useState, useEffect } from 'react';
import logo from './images/bonfire.gif';
import './App.css';
import {Routes, Route} from "react-router-dom";
import Layout from './components/layout';
import Home from './webpages/home';
import Tracker from './webpages/tracker';


function App() {




  return (

    <div className="App">
      <header className="App-header">
        {/*<img src={logo} className="App-logo" alt="logo" />*/}

          <Layout>
          <Routes>
            <Route path = "/" element = {<Home />} />
            <Route path = "/tracker" element = {<Tracker />} />
          </Routes>
          </Layout>
          
      </header>
    </div>
  );
}

export default App;
