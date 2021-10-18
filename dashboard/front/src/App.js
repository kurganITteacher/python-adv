import 'bootstrap/dist/css/bootstrap.min.css';
import React from 'react';
import {BrowserRouter as Router, Route} from 'react-router-dom';
import Header from "./components/Header";
import Footer from "./components/Footer";
import ProjectList from "./components/ProjectList";
import ProjectDetail from "./components/ProjectDetail";
import UserList from "./components/UserList";
import TaskList from "./components/TaskList";
import Main from "./components/Main";
import axios from "axios";

const API_URL = "http://127.0.0.1:8000";
const getResourceURL = (suffix) => `${API_URL}/api/${suffix}/`;


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
        axios
            .get(getResourceURL("users"))
            .then((result) => {
                // console.log('users result:', result)
                this.setState({
                    users: result.data
                })
            })
            .catch((error) => console.log(error));
        axios
            .get(getResourceURL("projects"))
            .then((result) => {
                this.setState({
                    projects: result.data
                })
            })
            .catch((error) => console.log(error));
        axios
            .get(getResourceURL("project-tasks"))
            .then((result) => {
                this.setState({
                    tasks: result.data
                })
            })
            .catch((error) => console.log(error));

    }

    render() {
        // console.log('state', this.state);
        return (
            <div className="main">
                <Router>
                    <Header/>
                    <Route exact path="/">
                        <Main/>
                    </Route>
                    <Route exact path="/users">
                        <UserList users={this.state.users}/>
                    </Route>
                    <Route exact path="/projects">
                        <ProjectList projects={this.state.projects}/>
                    </Route>
                    <Route exact path="/projects/detail/:id">
                        <ProjectDetail projects={this.state.projects}
                                       users={this.state.users}/>
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
