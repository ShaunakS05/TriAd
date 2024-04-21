import './App.css';
import React, { useState } from "react";

function App() {

  const endpoint_Visual = "http://localhost:8000/upload-images"
  const [video, setVideo] = useState(null);

  const handleVideo = (event) => {
    setVideo(event.target.files[0]);
  }

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData()
    formData.append('video', video);

    const response = await fetch(endpoint_Visual, {
      method: 'POST',
      body: formData,
    })
    
    if(response.ok){
      console.log("hi")
    }
  }
  return (
    <div className="slide">
      <div className="nav-bar">
            <div className="nav-bar-title">VRCARD</div>
          </div>
      <div className="image-container">
        <div className="image">
          <div className = "text-container">
            <div className="main-title">VRCARD</div>
            <p className="text">THE FUTURE OF POSTCARDS IS HERE</p>
          </div>
        </div>
      </div>
      <div className = "form-container">
        <form onSubmit={handleSubmit}>
          <div className = "form-text">
            Submit a video here!
          </div>
          <input type="file" name="video-submit"></input>
          <input type="submit" name="submit-button" onchange={handleVideo}></input>
        </form>
      </div>
    </div>
  );
}

export default App;
