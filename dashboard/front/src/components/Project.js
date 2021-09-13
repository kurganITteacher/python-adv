const Project = ({project}) => {
    console.log('project:', project);
    return (
        <tr className="project-row">
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
                <th>Name</th>
                <th>Created</th>
            </tr>
            </thead>
            <tbody>
            {/*{projects.map(Project)}*/}
            {projects.map((project) => <Project key={project.name} project={project}/>)}
            </tbody>
        </table>
    )
}

export default ProjectList;
