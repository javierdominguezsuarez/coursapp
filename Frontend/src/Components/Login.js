import React from "react";
import "./Styles/Login.css"
import vector from "./Vector.svg"

export default function Login(){
    return(
        <>
            <div className="login-container">
                <div className = "login-head-container">
                    <img src = {vector} alt = "Imagen Diamante" id = "diam-login"></img>
                    <h2 id = "coursLogin">CoursApp</h2>
                </div>

                <div>
                    <h1 id = "login-txt">Login</h1>

                    <div>
                        <input className="txt" type="text" placeholder="Username"></input>
                        <br></br>
                        <input className="txt" type="password" placeholder="Password"></input>
                    </div>
                </div>

                <div className="btn-group">
                    <button id="btn">Sign in</button>
                    <br></br>
                    <button id="rgst">Register</button>
                </div>
                    
            </div>

            <div className="present">
                <div className = "login-head-container">
                    <img src = {vector}  alt = "Imagen Diamante" id = "diam-present"></img>
                    <h1 id = "cours-present">CoursApp</h1>

                </div>
                <h2 id = "your-learning">Your Learning</h2>
            </div>
        </>
    );
} 