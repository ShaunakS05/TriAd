import './App.css';
import React, { useState } from "react";

function App() {

  const endpoint_Visual = "http://localhost:8000/upload-images"
  const [video, setVideo] = useState(null);

  const handleVideo = (event) => {
    setVideo(event.target.files[0]);
    console.log("hi");
  }

  const handleSubmit = async (event) => {
    event.preventDefault();

    const formData = new FormData()
    formData.append('video', video);

    const response = await fetch(endpoint_Visual, {
      method: 'POST',
      body: formData
    })
    
    if(response.ok){
      console.log("hi");
    } else {
      console.error("No video selected");
    }
  }
  return (
    <div className="body">
      <div className="nav-bar">
            <div className="nav-bar-title">TRIAD</div>
          </div>
      <div className="image-container">
        <div className="image">
          <div className = "text-container">
            <div className="main-title">TRIAD</div>
            <p className="text">THE FUTURE OF ADVERTISING IS HERE</p>
          </div>
        </div>
      </div>
      <div className = "form-container">
        <form onSubmit={handleSubmit}>
          <div className = "form-text">
            Select a video to use our VR converter.
          </div>
          <input type="file" name="video-submit" onChange={handleVideo}></input>
          <button type="submit" name="submit-button">Submit</button>
        </form>
      </div>
    </div>
  );
}

export default App;
