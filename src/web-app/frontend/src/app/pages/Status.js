import React, {useState, useEffect} from 'react';

import axios from 'axios';
import "./pages.css";


function Status() {
	const [progress, setProgress] = useState([]);
	const [temperature, setTemp] = useState("");
	const [nodes, setNodes] = useState([]);


	useEffect(() => {
		setInterval(() => {
			getData();
		}, 1000);
	}, []);


	function getData() {
    axios.get("http://localhost:5000/data",  { crossdomain: true }).then(response => {
			//console.log(response.data);
			setProgress(response.data.progress);
			setTemp(response.data.temperature);
			setNodes(response.data.nodes);
    });
  }


	function Job_Status(props) {
		//console.log(props);
		//console.log(index);
		const data = props.children[0];
		const index = props.children[1];
		return(
			<div className="job_info" key={index}>
				<div>{data.job +" => "+ data.percent + "%"}</div>
				
			</div>
		);
	}


	return (
		<div className="window" >
			<h1 className="Window-header">Status Window</h1>
			<p className="Progress-Title">PROGRESS</p>
			{progress.map((progress,index) => <Job_Status>{progress}{index}</Job_Status>)}
			<p className="Temperature-Value">{temperature + "C"}</p>
			<p className="Nodes-Title">NODES</p>
			{nodes.map(nodes => <div>{nodes.name +" => "+ nodes.cores}</div>)}
		</div>
	);
}

export default Status;
