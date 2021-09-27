import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import {BrowserRouter as Router, NavLink as Link, Route} from 'react-router-dom';
import Header from "./components/Header";
import Footer from "./components/Footer";
import ProjectList from "./components/Project";
import UserList from "./components/User";
import TaskList from "./components/Task";
import Main from "./components/Main";


const usersMock = [
    {
        "id": 1,
        "username": "kpk",
        "email": "",
        "first_name": "",
        "last_name": "",
        "gender": "",
        "date_birth": null
    },
    {
        "id": 2,
        "username": "user1",
        "email": "",
        "first_name": "",
        "last_name": "",
        "gender": "",
        "date_birth": null
    }
];

const projectsMock = [
    {
        "id": 1,
        "name": "One",
        "desc": "draft 1",
        "created": "2021-09-06T06:13:51.540849Z",
        "updated": "2021-09-06T06:13:51.540849Z",
        "owner": 2,
        "members": [
            1,
            2
        ]
    },
    {
        "id": 2,
        "name": "Two",
        "desc": "draft 2",
        "created": "2021-09-06T06:14:13.029644Z",
        "updated": "2021-09-06T06:14:13.029644Z",
        "owner": 1,
        "members": [
            1
        ]
    }
];

const projectTasksMock = [
    {
        "id": 1,
        "title": "Initial",
        "text": "start it",
        "created": "2021-09-06T06:14:36.197785Z",
        "updated": "2021-09-06T06:14:36.197785Z",
        "status": false,
        "project": 1,
        "author": 2,
        "executors": [
            1
        ]
    },
    {
        "id": 2,
        "title": "task 1",
        "text": "run migrations",
        "created": "2021-09-06T06:15:01.977061Z",
        "updated": "2021-09-06T06:15:01.977061Z",
        "status": false,
        "project": 1,
        "author": 1,
        "executors": [
            1
        ]
    },
    {
        "id": 3,
        "title": "Initial",
        "text": "start it",
        "created": "2021-09-06T06:15:18.215955Z",
        "updated": "2021-09-06T06:15:18.215955Z",
        "status": false,
        "project": 2,
        "author": 2,
        "executors": [
            1
        ]
    }
];


class App extends React.Component {
    constructor(props) {
        super(props);  // parent constructor
        this.state = {
            users: [],
            projects: [],
            tasks: []
        };
    }

    componentDidMount() {
        // call rest API
        this.setState({
            users: usersMock,
            projects: projectsMock,
            tasks: projectTasksMock
        })
    }

    render() {
        // console.log('state', this.state);
        return (
            <div className="main">
                <Router>
                    <Header/>
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
                        </ul>
                    </header>

                    <Route exact path="/">
                        <Main/>
                    </Route>
                    <Route exact path="/users">
                        <UserList users={this.state.users}/>
                    </Route>
                    <Route exact path="/projects">
                        <ProjectList projects={this.state.projects}/>
                    </Route>
                    <Route exact path="/tasks">
                        <TaskList tasks={this.state.tasks}/>
                    </Route>
                </Router>
                <Footer/>
            </div>
        )
    }
}

export default App;
