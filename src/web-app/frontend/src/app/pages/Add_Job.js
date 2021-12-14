import React, {Component, useState, useEffect} from 'react';
import "./pages.css";


function Add_Job() {
	const [progress, setProgress] = useState([]);
	const [temperature, setTemp] = useState("");
	const [nodes, setNodes] = useState([]);


	return (
		<div className="window" >
			<h1 className="Window-header">Status Window</h1>
			<p className="Progress-Title">PROGRESS</p>
			{progress.map(progress => <div>{progress.job +" => "+ progress.percent + "%"}</div>)}
			<p className="Temperature-Value">{temperature + "C"}</p>
			<p className="Nodes-Title">NODES</p>
			{nodes.map(nodes => <div>{nodes.name +" => "+ nodes.cores}</div>)}
		</div>
	);
}

export default Add_Job;
