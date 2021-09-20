import React from 'react';
import Header from "./components/Header";
import Footer from "./components/Footer";
import ProjectList from "./components/Project";
// import {ProjectList} from "./components/Project";
// import {ProjectList, ProjectListExt} from "./components/Project";


const projectsMock = [
    {'name': "Project X", 'created': "2021-09-02"},
    {'name': "Project Alpha", 'created': "2021-09-07"}
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
        // call API
        this.setState({
            projects: projectsMock
        })
    }

    render() {
        console.log('state', this.state);
        return (
            <div>
                <Header/>
                Dashboard
                <ProjectList projects={this.state.projects}/>
                <Footer/>
            </div>
        )
    }
}

export default App;
