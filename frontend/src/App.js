import './App.css';
import React, { useState } from "react";

function App() {
  const [video, setVideo] = useState(null);

  const handleVideo = (event) => {
    setVideo(event.target.files[0]);
  }

  const handleSubmit = (event) => {
    event.preventDefault();

    const formData = FormData()
    formData.append('video', video);

    fetch('/upload-images', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => console.log('Success:', data))
    .catch((error) => console.error('Error:', error));
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
