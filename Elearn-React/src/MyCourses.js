import SideNav from "./SideNav";
import React, {useEffect, useState} from "react";
import { useSelector } from 'react-redux';
import { useDispatch } from 'react-redux';

function MyCourses(props) {
    const [data,setData] = useState([])

    const username = useSelector(state => state.username);
    const userId = useSelector(state => state.userId);
    const url = 'http://127.0.0.1:8089/elearn/getuser/'+ userId ;
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
            .then(data_response => {
                if (data_response) {
                    console.log("data : " ,data_response)
                    // console.log("data : " ,data_response.result.courses," ",typeof(data_response.result.courses))
                    setData(data_response.result.courses)
                    dispatch({ type: 'SET_USER_COURSES', payload:data });
                    // console.log(data)
                }
                else {
                    console.log("error");
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    },[])


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

        <div >
            <h1>Welcome, {username}</h1>
            <SideNav />
            <div className='mainframe'>
            <TableView items={data} />
            </div>
         </div>
    )
}

export default MyCourses;