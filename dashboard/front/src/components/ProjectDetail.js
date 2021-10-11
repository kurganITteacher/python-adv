import React from "react";
import {useParams} from "react-router";

const ProjectDetail = ({projects, users}) => {
    let {id} = useParams();
    let project = projects.filter((item) => item.id === +id)[0];
    // project = filter(projects, lambda item: item.id == int(id));
    // console.log('this project:', project);
    // console.log('users', users);
    let owner = users.find((item) => project.owner === item.id);
    // console.log('owner', owner);
    let members = users.filter((item) => project.members.includes(item.id));
    // console.log('members', members);

    return (
        <div className={"project-detail"}>
            <h2>Project: {project.name}</h2>
            <h3>Owner: {owner.username}</h3>
            <p>Created: {project.created}</p>
            <p>Updated: {project.updated}</p>
            <h4>Members:</h4>
            <ul>
                {members.map((item) => (
                    <li key={item.id}>{item.username}</li>
                ))}
            </ul>
            <p>Description: {project.desc}</p>
        </div>

    )
}

export default ProjectDetail;

