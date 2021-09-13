const Project = (project) => {
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

// const ProjectList = (props) => {
function ProjectList(props) {
    console.log('props:', props);
    // console.log('projects:', props.projects);
    return (
        <table className={"project-list"}>
            <thead>
            <tr>
                <th>Name</th>
                <th>Created</th>
            </tr>
            </thead>
            <tbody>
            {[].map(Project)}
            </tbody>
        </table>
    )
}

export default ProjectList;
