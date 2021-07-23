//import logo from './logo.svg';
import React, {useState, useEffect, useRef} from 'react'
import './App.css'
import PieChart from './components/PieChart'

/*
class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {menu:"+"}
  }

  render(){
    return(
      <div>
        <Navbar>
          <NavItem icon={this.state.menu} />
        </Navbar>
      </div>
    );
  }
}
*/

function App() {
  
  return (
    <div>
      <Navbar>
      <NavItem icon={"+"} />
    </Navbar>
    </div>
  );
}


function Navbar(props) {
  return (
    <nav className="navbar">
      <ul className="navbar-nav"> {props.children} </ul>
    </nav>
  )
}

function NavItem (props) {
  return (
    <li className="nav-item">
      <a href="#" className="icon-button">
        {props.icon}
      </a>
    </li>
  );
}


function MainScreen (props) {
  return(
    <div className="main-screen">
      if 
    </div>
  );
}

export default App;
