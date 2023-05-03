import {useSelector} from "react-redux";
import {useDispatch} from "react-redux";
import React, {useEffect, useState} from "react";
import SideNav from "./SideNav";

const AddCourses = () => {
    const courses = useSelector(state => state.courses);
    const userCourses = useSelector(state => state.userCourses);
    const userId = useSelector(state => state.userId);
    const url = 'http://127.0.0.1:8089/elearn/getuser/'+ userId ;
    const [data,setData] = useState([])
    const dispatch = useDispatch()
    const [distinctArr, setDistinctArr] = useState([])
    const [reload, setReloadDiv] = useState("");

    useEffect(() => {

        // if (userCourses)
        {
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
                        console.log("Inside Add Courses")
                        console.log(data_response.result.courses)
                        setData(data_response.result.courses)
                        dispatch({ type: 'SET_USER_COURSES', payload:data });
                        console.log("user_courses",userCourses)
                        setDistinctArr(courses.filter(item1 => !data_response.result.courses.find(item2 => item2.id === item1.id)));
                    }
                    else {
                        console.log("error");
                    }
                })
                .catch(error => {
                    console.error('Error:', error);
                });
        }
        // else {
        //     setDistinctArr(courses.filter(item1 => !userCourses.find(item2 => item2.id === item1.id)))
        // }
    },[1])

    // console.log(distinctArr)
     const TableView = ({ items }) => {
         const handleAddCourse= (id,index) => {
             let array = distinctArr;
             for (let i = 0; i <array.length; i++) {
                 console.log("array ",array[i])
                 if (array[i].id == id){
                     console.log("Id Matched")
                     array.splice(i, 1);
                     console.log(array)
                 }
             }
             const add_user_course_url = 'http://127.0.0.1:8089/elearn/user/'+userId+'/addcourses'
             fetch(add_user_course_url, {
                 method: 'POST',
                 headers: {
                     'Content-Type': 'application/json'
                 },
                 body : JSON.stringify({
                     'course_ids': [id]
                 })
             })
                 .then(response => {
                     return response.json();
                 })
                 .then(data_response => {
                     if (data_response) {
                         console.log(data_response.result)
                         // if (data_response.result == 'success') {
                             console.log("Inside user Add course")
                         console.log(data_response)
                     } else {
                         console.log("error");
                     }
                 })
                 .catch(error => {
                     console.error('Error:', error);
                 });
             setDistinctArr(array)
             console.log("After removing",distinctArr)
             return alert('Courses Enrolled. Please check My courses')
         }
        // console.log(distinctArr)
        return (
            <div className="container">
                {items.map((item, index) => (
                    <div key={index}  className="box">

                            <h1 key={index} onClick={() => handleAddCourse(item.id,index)}>{item.title}</h1>
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
console.log("distinct Arr ",distinctArr)
    return (
        <div>
            <h1>Add Courses</h1>
            <SideNav />
            <div>
            {distinctArr ? (
            <div className='mainframe'>
                <TableView items={distinctArr} />
            </div>
            ): <p>Loading</p>}
            </div>
        </div>
    )
}

export default AddCourses