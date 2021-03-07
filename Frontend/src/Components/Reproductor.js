import { buildQueries } from "@testing-library/dom";
import React, { useState } from "react";
import Player from "react-player";
import video from "./Media/ibai.mp4";

export default function Reproductor(){
     const [show,setShow] = useState(false);

    if(show){
        return(
            <>
                <div className="container">
                    <Player
                    url={video}
                    width="100%"
                    height="100%"
                    className="reproductor"
                    controls
                />
                </div>
                <button onClick={()=> setShow(false)}>Volver a Inicio</button>
            </>
        );

    } else {
        return(
            <>
                <div>Pulsa el Botón</div>
                <button onClick={()=> setShow(true)}>Reproducir Video de Ibai</button>
            </>
        );
    }

}