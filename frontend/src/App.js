// import logo from './logo.svg';
import './App.css';
import { useEffect, useState } from 'react';
import { Button } from 'react-bootstrap';
import axios from 'axios';
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
  useParams
} from "react-router-dom";

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// const IncidentWrapper = () => {
//   // Set State for Incident Data
//   const [incidents, setIncidents] = useState([])

//   // fetch data
//   useEffect(() => {
//     // // fetch the Incident data
//     // fetch(`api/`)
//     setIncidents([
//       {
//         "id":1,
//         "description": "Testing a description for an incident",
//         "title": "Incident Title"
//       },
//       {
//         "id":2,
//         "description": "Testing another description for an incident",
//         "title": "Another Incident Title"
//       }
      

//     ])
//   })
// }
// function MyButton() {
//   return (
//     <Button>This is a button</Button>
//   );
// }

function Incident(props){
  const { incident } = props
  return (
    <div className="incident-item">
      <h3>{incident.title} ({incident.id})</h3>
      <p>{incident.description}</p>
    </div>
  )
}

function getCookie(name) {
  let cookieValue = null;
  if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
          const cookie = cookies[i].trim();
          // Does this cookie string begin with the name we want?
          if (cookie.substring(0, name.length + 1) === (name + '=')) {
              cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
              break;
          }
      }
  }
  return cookieValue;
}

function SendIncident(props){
  const [incident, setIncident] = useState(
    { title : "", description: ""}
  );

  const handleChange = (e) => {
    setIncident({...incident, [e.target.name]: e.target.value})
  }

  const handleSubmit = (e) => {
    e.preventDefault()
    axios.defaults.xsrfCookieName = 'csrftoken';
    axios.defaults.xsrfHeaderName = 'X-CSRFToken';

    axios.post('localhost:8000/create-incident', incident, {headers: { "X-CSRFToken" : getCookie('csrftoken')}})
     .then(function (response) {
      console.log(response)
     })
     .catch(function (error) {
      console.log(error)
     })
  }

  return(
    <div className="incident-create">
      <form>
        <input type="text" name="title" />
        <input type="text" name="description" />
        <Button> Save </Button>
      </form>
    </div>
  )
}

function App() {
  // Set State for Incident Data
  const [incidents, setIncidents] = useState([])

  // fetch data
  useEffect(() => {
    // // fetch the Incident data
    async function fetchIncidents() {
      const res = await fetch("localhost:8000/api")
      res.json().then(res => setIncidents(res.response))
        // .catch(err => setErrors(err));
    }
    fetchIncidents();
  }, [])

    // placeholder setter
    // setIncidents([
    //   {
    //     "id":1,
    //     "description": "Testing a description for an incident",
    //     "title": "Incident Title"
    //   },
    //   {
    //     "id":2,
    //     "description": "Testing another description for an incident",
    //     "title": "Another Incident Title"
    //   }
      

  //   ])
  // })

  return (
    <div>
      <h1>Hello again, World!</h1>
      {/* <MyButton /> */}

    <div className="incident-list">
      {incidents.map((item,index) => {
        return (
          <Incident incident={item} key={index} />
        )}
      )}
    </div>

    <div className="create-incident">

    </div>
  
  </div>
  )
}

function SingularIncident(params) {
  const{ id } = useParams()
  const[incident,setIncident] = useState([])
  const[error, setError] = useState(false)

  useEffect (() => {
    async function fetchIncidents() {
      const res = await fetch("http://127.0.0.1:8000/api/"+id);
      res
        .json()
        .then(res => setIncident(res))
        .catch(err => setError(err));
    }

    fetchIncidents();
  },[])

  return (
    <div className="App">
      <header className="App-header">
      </header>
    
          { error || incident.status==="error" ? 
           <p>Something went wrong</p>
           :
           <div className="incident-list">
              <h1>{incident.title} ({incident.id})</h1>
              <p>{incident.description}</p>
           </div>
          }
    </div>
  );
}

// function SingularIncident(params) {
//   const{ id } = useParams()
//   const[incident, setIncident] = useState([])
//   const[error, setErrors] = useState(false)

//   useEffect (() => {
//     async function fetchIncidents() {
//       const res = await fetch("https://localhost:8000/api/"+id);
//       res.json()
//         .then(res => setIncident(res))
//         .catch(err => setErrors(err));
//     }
//   },[])

//   return (
//     <div className="App">
//       <header className="App-header">
//       </header>

//         { error || incident.status==="error" ?
//         <p>Something went wrong</p>
//         :
//         <div className="incident-list">
//           <h1>{incident.title} ({incident.id})</h1>
//           <p>{incident.description}</p>
//         </div>
//       }
//     </div>
//   );
// }

// export default App;
export default function Landing(){
  return(
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Incident list</Link>
            </li>
            <li>
              <Link to="/create-incident">Create Incident</Link>
            </li>
          </ul>
        </nav>

        <Routes>
          <Route path="/api/:id">
            <SingularIncident />
          </Route>
          <Route path="/create-incident">
            <SendIncident />
          </Route>
          <Route path="/">
            <App />
          </Route>
        </Routes>
      </div>
    </Router>
  )
}