import React, {Component, useState, useEffect} from 'react';
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

export default Status;

/*
class Status extends Component {
	state = {
		temperature: 0
	};

	componentDidMount() {

	}

	componentWillUnmount() {

	}

	callBackendAPI = async() => {
		const response = await fetch('/data');
		const body = await response.json();

		if (response.status !== 200) {
			throw Error(body.message);
		}
		return body;
	}
}
*/