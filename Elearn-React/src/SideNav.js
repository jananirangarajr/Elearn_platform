import './dashboard.css'
import { NavLink } from 'react-router-dom';
import {useState} from "react";

const SideNav = () => {
    const [showContent, setShowContent] = useState(false);
    const handleClick = () => { setShowContent(true)};
    return (
        <div>
    <nav className="sidenav">
        <ul className="ul">
            <li>
                <NavLink to="/courses">Courses</NavLink>
            </li>
            <li>
                <NavLink to="/mycourses">My Courses</NavLink>
            </li>
            <li>
                <NavLink to="/addCourses">Add Courses</NavLink>
            </li>
            {/*<li>*/}
            {/*    <NavLink to="#section1" anchor>Section 1</NavLink>*/}
            {/*</li>*/}
            {/*<li>*/}
            {/*    <NavLink to="#section2" anchor>Section 2</NavLink>*/}
            {/*</li>*/}
            {/*<MyNavLink to="/mycomponent" component={SignIn} onClick={handleClick}>*/}
            {/*    Click me!*/}
            {/*</MyNavLink>*/}

        </ul>
    </nav>
    {/*<section id="section1">*/}
    {/*    <h2>Section 1</h2>*/}
    {/*    <p>This is the content for section 1.</p>*/}
    {/*</section>*/}

    {/*<section id="section2">*/}
    {/*    <h2>Section 2</h2>*/}
    {/*    <p>This is the content for section 2.</p>*/}
    {/*</section>*/}
    </div>
    )
};

export default SideNav;