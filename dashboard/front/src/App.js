import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import {BrowserRouter as Router, NavLink, Route} from 'react-router-dom';
import {Container, Nav, Navbar} from 'react-bootstrap';
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
        console.log('state', this.state);
        return (
            <div>
                Dashboard
                <Router>
                    <Header/>
                    <Navbar bg="dark" variant="dark">
                        <Container>
                            <Nav className="me-auto">
                                <Nav.Link>
                                    <NavLink to={"/"}>Main</NavLink>
                                </Nav.Link>
                                <Nav.Link>
                                    <NavLink to={"/users"}>Users</NavLink>
                                </Nav.Link>
                                <Nav.Link>
                                    <NavLink to={"/projects"}>Projects</NavLink>
                                </Nav.Link>
                                <Nav.Link>
                                    <NavLink to={"/tasks"}>Tasks</NavLink>
                                </Nav.Link>
                            </Nav>
                        </Container>
                    </Navbar>

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
