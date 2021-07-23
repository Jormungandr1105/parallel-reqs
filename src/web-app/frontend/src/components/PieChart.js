import React from 'react'
import {Doughnut} from 'react-chartjs-2/dist/react-chartjs-2'

const data = {
	datasets: [{
		label: 'Fan Speed',
		data: [79,21],
		backgroundColor: [
			'rbga(255,255,255,1',
			'rgba(255,255,255,1',
		]
	}]
}

function PieChart() {
	return(
		<Doughnut data={data}/>
	);
}

export default PieChart