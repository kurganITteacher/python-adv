import React from "react";


class LoginForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password: ""
        };
    }

    handleChange(event) {
        console.log('change:', event.target.name, event.target.value);
        // this.setState(
        //     {[event.target.name]: event.target.value}
        // )
    }

    handleSubmit(event) {
        event.preventDefault();
        console.log('submit:', event.target);
    }

    render() {
        return (
            <div className="login-form">
                <form method="post" onSubmit={this.handleSubmit}>
                    <input type="text"
                           name="username"
                           placeholder="username"
                           onChange={this.handleChange}/>
                    <input type="password"
                           name="password"
                           placeholder="password"
                           onChange={this.handleChange}/>
                    <input type="submit"
                           value="login"/>
                </form>
            </div>
        )
    }

}

export default LoginForm
