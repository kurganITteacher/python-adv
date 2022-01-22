import React from "react";


class RegisterForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            username: "",
            password1: "",
            password2: "",
            email: "",
        };
    }

    handleChange(event) {
        this.setState(
            {[event.target.name]: event.target.value}
        )
    }

    handleSubmit(event) {
        event.preventDefault();
        this.props.register(
            this.state.username,
            this.state.password1,
            this.state.password2,
            this.state.email
        );
    }

    render() {
        return (
            <div className="login-form">
                <form method="post"
                      onSubmit={(event) => this.handleSubmit(event)}>
                    <input type="text"
                           name="username"
                           placeholder="username"
                           onChange={(event) => this.handleChange(event)}/>
                    <input type="password"
                           name="password"
                           placeholder="password"
                           onChange={(event) => this.handleChange(event)}/>
                    <input type="submit"
                           value="login"/>
                </form>
            </div>
        )
    }

}

export default RegisterForm
