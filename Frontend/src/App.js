import React from 'react';
import './App.css';
import Login from './Components/Login';

//Forma 1 de Crear Componente
function App() {
  return (
    <Login/>
  );
}

//Forma 2 de crear Componente
// const app = () => <div>Hello World!</div>;

//Forma 3 de Crear Componente
// class App extends React.Component{
//   render(){
//     return <div>Hello World!</div>
//   }
// }

export default App;
