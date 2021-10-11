import {NavLink as Link} from "react-router-dom";
import React from "react";

const Project = ({project}) => {
    // console.log('project:', project);
    return (
        <tr className="project-row">
            <td>
                {project.id}
            </td>
            <td>
                <Link to={`/projects/detail/${project.id}`} className="nav-link">
                        {project.name}
                </Link>
            </td>
            <td>
                {project.created}
            </td>
            <td>
                <Link to={`/projects/delete/${project.id}`} className="nav-link">
                        delete
                </Link>
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
                    <th>actions</th>
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

