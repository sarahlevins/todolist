import React, { useState } from 'react';
import './App.css';
import Todo from './components/Todo.js';
import TodoForm from './components/TodoForm.js';

function App() {
  // set state using hooks
  const [todos, setTodos] = useState([
    {
      text: "Learn React",
      isCompleted: "false"
    },
    {
      text: "Sleep In",
      isCompleted: "false"
    },
    {
      text: "Cry",
      isCompleted: "false"
    },
  ]);

  const addTodo = text => {
    const newTodos = [...todos, { text }];
    setTodos(newTodos);
  }


  const completeTodo = index => {
    const newTodos = [...todos];
    newTodos[index].isCompleted = true;
    setTodos(newTodos);
  }

  const removeTodo = index => {
    const newTodos = [...todos];
    newTodos.splice(index, 1);
    setTodos(newTodos);
  }

  return (
    <div className="App">
      <div className="todo-list">
        {todos.map(
          (todo, index) => (
            <Todo
              key={index}
              index={index}
              todo={todo}
              completeTodo={completeTodo}
              removeTodo={removeTodo}
            />
          )
        )}
        <TodoForm addTodo={addTodo} />
      </div>
    </div>
  );
}

export default App;
