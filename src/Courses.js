import SideNav from "./SideNav";
import React, {useEffect, useState} from "react";
import { useSelector } from 'react-redux';
import { useDispatch } from 'react-redux';
function Courses(props) {
    const [data,setData] = useState([])
    const url = 'http://127.0.0.1:8089/elearn/getcourses';
    const username = useSelector(state => state.username);
    const dispatch = useDispatch();
    useEffect(() => {

        fetch(url, {
            method: 'GET',
            headers: {
                'Content-Type': 'application/json'
            }
        })
            .then(response => {
                return response.json();
            })
            .then(data => {
                if (data) {
                    setData(data.result)
                    console.log(data.result)
                    dispatch({ type: 'SET_COURSES', payload:data.result });
                }
                else {
                    console.log("error");
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    },[1])

    const TableView = ({ items }) => {
        return (
            <div className="container">
                {items.map((item, index) => (
                        <div  key={index} className="box">
                            <h1 key={index}>{item.title}</h1>
                            <hr/>
                            By -
                            &nbsp;
                            {item.author}<br/>
                            <br/><br/><br/>
                            {item.description}
                        </div>
                ))}
            </div>
        );
    };



    return (
        // <div onLoad={getCourses}>
        //     <div className="course-layout">
        //         <p>Title</p>
        //     </div>
        // </div>
        <div >
            <h1>Welcome, {username}</h1>
            <SideNav />

            <div className='mainframe'>

                {/*{<Course />}*/}
            <TableView items={data} />
            </div>
            {/*<div className="box">Box 2</div>*/}
            {/*<div className="box">Box 3</div>*/}
            {/*<div className="box">Box 4</div>*/}
         </div>
    )
}

export default Courses;