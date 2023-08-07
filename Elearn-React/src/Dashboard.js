import './dashboard.css'
import SideNav from './SideNav'
import { useLocation} from 'react-router-dom';
import React from "react";
import Courses from "./Courses";
import {useSelector} from "react-redux";


function Dashboard() {
    const location = useLocation();
    // const name = location.state.name;
    const username = useSelector(state => state.username);
    // const userId = useSelector(state => state.userId);
    return(
        <div>
            <h1>Welcome, {username}</h1>
            <SideNav />
            <div className='mainframe'>
                <Courses />
            </div>

            {/*<Routes>*/}
            {/*    <Route exact path="/courses" component={Dashboard} />*/}
            {/*    <Route path="/mycourses" component={Dashboard} />*/}
            {/*    <Route path="/addCourses" component={Dashboard} />*/}
            {/*</Routes>*/}
        </div>
    )
}
export default Dashboard;