import React from "react";
import {useParams} from "react-router";

const ProjectDetail = ({projects}) => {
    // let id = useParams();
    let {id} = useParams();
    // console.log('id:', id, typeof id, typeof parseInt(id), typeof +id);
    // console.log('projects:', projects);
    // let project = projects.filter((item) => item.id == id)[0];
    let project = projects.filter((item) => item.id === +id)[0];
    console.log('this project:', project);

    return (
        <h3>Project</h3>
    )
}

export default ProjectDetail;

