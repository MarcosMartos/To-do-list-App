import { useState, useEffect } from "react";
import axios from "axios";

function TodoList() {
  const [todos, setTodos] = useState([]);
  const [title, setTitle] = useState("");
  const [editingTodo, setEditingTodo] = useState(null);
  const [editDialogOpen, setEditDialogOpen] = useState(false);
  const [editedTitle, setEditedTitle] = useState("");

  useEffect(() => {
    axios.get("http://localhost:5000/todos").then((res) => setTodos(res.data));
  }, []);

  const addTodo = () => {
    if (!title.trim()) return;
    axios.post("http://localhost:5000/todos", { title }).then((res) => {
      setTodos([...todos, res.data]);
      setTitle("");
    });
  };

  const toggleTodo = (id, completed) => {
    axios
      .put(`http://localhost:5000/todos/${id}`, { completed: !completed })
      .then(() => {
        setTodos(
          todos.map((todo) =>
            todo.id === id ? { ...todo, completed: !completed } : todo
          )
        );
      });
  };

  const deleteTodo = (id) => {
    axios.delete(`http://localhost:5000/todos/${id}`).then(() => {
      setTodos(todos.filter((todo) => todo.id !== id));
    });
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") addTodo();
  };

  const openEditDialog = (todo) => {
    setEditingTodo(todo);
    setEditedTitle(todo.title);
    setEditDialogOpen(true);
  };

  const handleEditSave = () => {
    if (!editedTitle.trim() || !editingTodo) return;

    axios
      .put(`http://localhost:5000/todos/${editingTodo.id}`, {
        title: editedTitle,
        completed: editingTodo.completed,
      })
      .then(() => {
        setTodos(
          todos.map((todo) =>
            todo.id === editingTodo.id ? { ...todo, title: editedTitle } : todo
          )
        );
        setEditDialogOpen(false);
        setEditingTodo(null);
        setEditedTitle("");
      });
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white flex items-center justify-center p-4">
      <div className="w-full max-w-xl bg-gray-800 rounded-xl shadow-xl p-6 space-y-6">
        <h1 className="text-3xl font-bold text-center">To-Do List</h1>

        <div className="flex gap-2">
          <input
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            onKeyPress={handleKeyPress}
            placeholder="Añadir nueva tarea..."
            className="flex-1 px-4 py-2 rounded-lg bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"
          />
          <button
            onClick={addTodo}
            className="bg-indigo-600 hover:bg-indigo-700 px-4 py-2 rounded-lg font-semibold"
          >
            Agregar
          </button>
        </div>

        <ul className="space-y-3">
          {todos.map((todo) => (
            <li
              key={todo.id}
              onClick={() => toggleTodo(todo.id, todo.completed)}
              className={`flex justify-between items-center px-4 py-2 rounded-lg cursor-pointer transition ${
                todo.completed
                  ? "bg-green-600 line-through"
                  : "bg-gray-700 hover:bg-gray-600"
              }`}
            >
              <span>{todo.title}</span>
              <div className="flex gap-2">
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    openEditDialog(todo);
                  }}
                  className="hover:text-yellow-400 text-lg"
                >
                  ✏️
                </button>
                <button
                  onClick={(e) => {
                    e.stopPropagation();
                    deleteTodo(todo.id);
                  }}
                  className="hover:text-red-400 text-lg"
                >
                  🗑️
                </button>
              </div>
            </li>
          ))}
        </ul>
      </div>

      {editDialogOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-60 flex items-center justify-center z-50">
          <div className="bg-gray-800 p-6 rounded-xl w-full max-w-md space-y-4">
            <h2 className="text-2xl font-bold text-center">Editar Tarea</h2>
            <textarea
              value={editedTitle}
              onChange={(e) => setEditedTitle(e.target.value)}
              onKeyPress={(e) => e.key === "Enter" && handleEditSave()}
              rows={4}
              className="w-full p-3 rounded-lg bg-gray-700 text-white placeholder-gray-400 focus:outline-none focus:ring-2 focus:ring-indigo-500"
            />
            <div className="flex justify-end gap-2">
              <button
                onClick={() => setEditDialogOpen(false)}
                className="px-4 py-2 rounded-lg bg-gray-600 hover:bg-gray-500"
              >
                Cancelar
              </button>
              <button
                onClick={handleEditSave}
                className="px-4 py-2 rounded-lg bg-indigo-600 hover:bg-indigo-700 font-semibold"
              >
                Guardar
              </button>
            </div>
          </div>
        </div>
      )}
    </div>
  );
}

export default TodoList;
