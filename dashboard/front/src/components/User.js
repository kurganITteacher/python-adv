const User = ({user}) => {
    console.log('user:', user);
    return (
        <tr className="user-row">
            <td>
                {user.id}
            </td>
            <td>
                {user.username}
            </td>
            <td>
                {user.date_birth}
            </td>
        </tr>
    )
}

const UserList = ({users}) => {
    console.log('users:', users);
    return (
        <table className={"user-list"}>
            <thead>
            <tr>
                <th>id</th>
                <th>username</th>
                <th>date birth</th>
            </tr>
            </thead>
            <tbody>
            {users.map((user) => <User key={user.id} user={user}/>)}
            </tbody>
        </table>
    )
}


export default UserList;
