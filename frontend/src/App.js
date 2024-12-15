import React from "react";
import "./styles.css"; 
import ItemList from "./components/ItemList";

const App = () => {
  return (
    <div className="container">
      <h1>Reachify Assignment</h1>
      <ItemList />
    </div>
  );
};

export default App;
