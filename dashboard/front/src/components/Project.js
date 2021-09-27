const Project = ({project}) => {
    console.log('project:', project);
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
    console.log('projects:', projects);
    return (
        <table className={"project-list"}>
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
    )
}

export default ProjectList;

