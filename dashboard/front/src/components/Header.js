import {NavLink as Link} from "react-router-dom";
import React from "react";

function Header() {
    return (
        <header className="d-flex flex-wrap justify-content-center py-3 mb-4 border-bottom">
            <Link to={"/"}
                  className="d-flex align-items-center mb-3 mb-md-0 me-md-auto text-dark text-decoration-none">
                DashBoard
            </Link>
            <ul className="nav nav-pills">
                <li className="nav-item">
                    <Link to={"/users"} className="nav-link">
                        Users
                    </Link>
                </li>
                <li className="nav-item">
                    <Link to={"/projects"} className="nav-link">
                        Projects
                    </Link>
                </li>
                <li className="nav-item">
                    <Link to={"/tasks"} className="nav-link">
                        Tasks
                    </Link>
                </li>
                <li className="nav-item">
                    <Link to={"/login"} className="nav-link">
                        Login
                    </Link>
                </li>
            </ul>
        </header>
    )
}

export default Header;
