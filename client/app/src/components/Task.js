import React, { useState } from 'react';

const Task = () => {
    const [tasks, setTasks] = useState([]);
    const [newTask, setNewTask] = useState('');

    const addTask = () => {
        if (newTask.trim() !== '') {
            setTasks([...tasks, { text: newTask, completed: false }]);
            setNewTask('');
        }
    };

    const toggleTask = (index) => {
        const updatedTasks = [...tasks];
        updatedTasks[index].completed = !updatedTasks[index].completed;
        setTasks(updatedTasks);
    };

    const removeTask = (index) => {
        const updatedTasks = [...tasks];
        updatedTasks.splice(index, 1);
        setTasks(updatedTasks);
    };

    return (
        <div>
            <ul className="custom-list">
                {tasks.map((task, index) => (
                    <li className="custom-list"
                        key={index}
                        onClick={() => toggleTask(index)}
                        style={{ textDecoration: task.completed ? 'line-through' : 'none' }}
                    >
                        {task.text} {task.completed && '(Completed)'}
                        <button onClick={() => removeTask(index)}>Remove</button>
                    </li>
                ))}
            </ul>

            <div>
                <input
                    type="text"
                    value={newTask}
                    onChange={(e) => setNewTask(e.target.value)}
                    placeholder="Manually add a new task"
                />
                <button onClick={addTask}>Add Task</button>
            </div>
            <div>
                <input
                    type="text"
                    value={newTask}
                    onChange={(e) => setNewTask(e.target.value)} // this should actually call the task function
                    placeholder="feeling sluggish? input a topic, and let Furby whip up some tasks for you!"
                />
                <button onClick={addTask}>Add Task</button>
            </div>
        </div>
    );
};

export default Task;
