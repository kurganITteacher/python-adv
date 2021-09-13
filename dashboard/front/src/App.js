import React from 'react';


class App extends React.Component {
    constructor(props) {
        super(props);  // parent constructor
        this.setState({
            'users': [],
            'projects': [],
            'tasks': []
        })
    }

    render() {
        console.log('state', this.state);
        return (
            <div>
                Dashboard
            </div>
        )
    }

}

export default App;
// jsx -> js + ...
