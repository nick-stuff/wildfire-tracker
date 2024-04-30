import React from 'react';
import { Link } from 'react-router-dom';
import './navigation.css';
const Navigation = () => {
    return (
        <nav>
            <ul>
                <li>
                    <Link to="/">Home</Link>
                </li>
                <li>
                    <Link to="/tracker">Tracker</Link>
                </li>

            </ul>
        </nav>
    );
};
export default Navigation;
