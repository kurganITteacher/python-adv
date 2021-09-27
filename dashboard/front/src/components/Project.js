const Project = ({project}) => {
    // console.log('project:', project);
    return (
        <tr className="project-row">
            <td>
                {project.id}
            </td>
            <td>
                {project.name}
            </td>
            <td>
                {project.created}
            </td>
        </tr>
    )
}

const ProjectList = ({projects}) => {
    // console.log('projects:', projects);
    return (
        <div className="project-list">
            <h1>Projects</h1>
            <table className="project-list__table">
                <thead>
                <tr>
                    <th>id</th>
                    <th>name</th>
                    <th>created</th>
                </tr>
                </thead>
                <tbody>
                {projects.map((project) => <Project key={project.id} project={project}/>)}
                </tbody>
            </table>
        </div>
    )
}

export default ProjectList;

