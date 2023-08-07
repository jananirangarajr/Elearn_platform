import React, { useState } from 'react';
import './sign-in.css'
import { useNavigate } from 'react-router-dom';
import { useDispatch } from 'react-redux';
// import backgroundImage from 'process.env.PUBLIC_URL/background-img.jpg';
function SignIn(props) {
    const [name, setName] = useState('')
    const [password, setPassword] = useState('')
    const [errordiv,setErrorDiv] = useState(false)
    const [userID,setUserID] = useState('')

    const navigate = useNavigate()
    const dispatch = useDispatch();

    const handleNameChange = (event) => {

        setName(event.target.value)
        dispatch({ type: 'SET_USERNAME', payload:event.target.value });
        setErrorDiv(false)
    }
    const handlePasswordChange = (event) => {
        setPassword(event.target.value)
        setErrorDiv(false)
    }
    const handleSubmit = async (event) => {
        event.preventDefault();
        let url = 'http://localhost:8089/elearn/'
        let validUser = false;
        // handle form submission logic here, such as sending the email and password to a backend API
        fetch((url+'checkuser'), {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                'name':name,
                'password':password
            })
        })
            .then(response => {
                return response.json();
            })
            .then(data => {
                if (data.result == true) {
                    validUser = true
                    // console.log(validUser)
                    // eslint-disable-next-line no-restricted-globals
                    if (validUser) {
                        // console.log("inside")
                        fetch((url+'getuserid?name='+name), {
                            method: 'GET',
                            headers: {
                                'Content-Type': 'application/json'
                            }
                        })
                            .then(response => {
                                return response.json();
                            })
                            .then(data => {

                                // console.log(data.result)
                                setUserID(data.result)
                                dispatch({ type: 'SET_USER_ID', payload: data.result });
                                navigate('/courses', { state: { name } });
                            })
                            .catch(error => {
                                console.error('Error:', error);
                            });
                    }

                }
                else {
                    setErrorDiv(true);
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
        // console.log(validUser)


    }

    return (
        <div style={{ backgroundImage: `url(${process.env.PUBLIC_URL + '/background-img.jpg'})`, height: '100vh', backgroundSize: 'cover' }}>
            {/* Your login page content goes here */}
            {/*<div>*/}
            {/*    <img src={process.env.PUBLIC_URL + '/background-img.jpg'} alt="My Image" />*/}
            {/*</div>*/}
        <div className="sigin-page">
            <div className="login-form">
                <h2>Login</h2>
                <form onSubmit={handleSubmit}>
                    <div className="form-group">
                        <label>
                            User Name
                            <input type="text" onChange={handleNameChange} />
                        </label>
                    </div>
                    <div className="form-group">
                        <label>
                            Password
                            <input type="password" value={password} onChange={handlePasswordChange} />
                        </label>
                    </div>
                    <div>
                        <button type="submit">Sign In</button>
                    </div>
                    {errordiv && (
                        <div style={{ display: 'block', marginTop: '20px' }}>
                            Incorrect UserName/Password
                        </div>
                    )}
                </form>
            </div>
        </div>
        </div>
    );
}

export default SignIn;
