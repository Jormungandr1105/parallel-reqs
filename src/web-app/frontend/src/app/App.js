import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import "./App.css";
import Navbar from './navbar/Navbar.js';
import NavItem from './navbar/NavItem.js';
import Status from './pages/Status.js';
import Add_Job from './pages/Add_Job.js';


function App() {

  return (
    <div className="app">
      <Router>
        <div className="app-inner">
          <Navbar>
            <NavItem icon="S" path="/" />
            <NavItem icon="+" path="/add" />
          </Navbar>
          <Switch>
            <Route exact path="/">
              <Status/>
            </Route>
            <Route path="/add">
              <Add_Job/>
            </Route>
          </Switch>
        </div>
      </Router>
    </div>
  );
}

export default App;
