const Task = ({task}) => {
    // console.log('task:', task);
    return (
        <tr className="task-row">
            <td>
                {task.id}
            </td>
            <td>
                {task.title}
            </td>
            <td>
                {task.text}
            </td>
            <td>
                {task.created}
            </td>
            <td>
                {task.updated}
            </td>
            <td>
                {task.status ? "solved" : "in progress"}
            </td>
        </tr>
    )
}

const TaskList = ({tasks}) => {
    // console.log('tasks:', tasks);
    return (
        <div className="task-list">
            <h1>Tasks</h1>
            <table className="task-list__table">
                <thead>
                <tr>
                    <th>id</th>
                    <th>title</th>
                    <th>text</th>
                    <th>created</th>
                    <th>updated</th>
                    <th>status</th>
                </tr>
                </thead>
                <tbody>
                {tasks.map((task) => <Task key={task.id} task={task}/>)}
                </tbody>
            </table>
        </div>
    )
}

export default TaskList;

