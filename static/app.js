document.addEventListener("DOMContentLoaded", function () {
    const taskList = document.getElementById("taskList");
    const editTaskForm = document.getElementById("editTaskForm");
    const taskIdInput = document.getElementById("taskId");
    const editTitleInput = document.getElementById("editTitle");
    const editDescriptionInput = document.getElementById("editDescription");

    // Handle delete button clicks
    taskList.addEventListener("click", async function (e) {
        console.log("Botón eliminar presionado");
        
        if (e.target.classList.contains("delete-btn")) {
            const taskId = e.target.getAttribute("data-task-id");
            console.log("Task ID to delete:", taskId);  // Verifica el ID
            console.log(`/delete_task/${taskId}`);
            try {
                // Realiza la solicitud DELETE al backend
                console.log("Enviando solicitud DELETE...");
                const response = await fetch(`/delete_task/${taskId}`, { method: "DELETE" });

                // Si la respuesta es exitosa (status 200-299)
                if (response.ok) {
                    console.log("Tarea eliminada exitosamente");
                    window.location.reload();  // Recarga la página para actualizar la lista de tareas
                } else {
                    console.log("Error status:", response.status); // Muestra el código de estado
                    // Si hay algún error en la respuesta
                    const errorData = await response.json();
                    console.error("Error eliminando la tarea:", errorData.detail);
                }
            } catch (error) {
                // Captura y muestra cualquier error que ocurra durante la solicitud
                console.error("Error en la solicitud:", error);
            }
        }
    });


    // Handle edit button clicks
    taskList.addEventListener("click", function (e) {
        if (e.target.classList.contains("edit-btn")) {
            const taskId = e.target.getAttribute("data-task-id");
            const taskElement = e.target.parentElement;
            const taskText = taskElement.querySelector("span").textContent.split(" - ");

            taskIdInput.value = taskId;
            editTitleInput.value = taskText[0];
            editDescriptionInput.value = taskText[1];
        }
    });


    // Manejar la actualización de la tarea cuando se envíe el formulario
    editTaskForm.addEventListener("submit", async function (e) {
        e.preventDefault();

        const taskId = taskIdInput.value;
        const updatedTitle = editTitleInput.value;
        const updatedDescription = editDescriptionInput.value;

        try {
            const response = await fetch(`/update_task/${taskId}`, {
                method: "PUT",
                headers: {
                    "Content-Type": "application/json",
                },
                body: JSON.stringify({
                    title: updatedTitle,
                    description: updatedDescription
                }),
            });

            if (response.ok) {
                console.log("Tarea actualizada exitosamente");
                window.location.reload();  // Recarga la página para mostrar los cambios
            } else {
                const errorData = await response.json();
                console.error("Error actualizando la tarea:", errorData.detail);
            }
        } catch (error) {
            console.error("Error en la solicitud:", error);
        }
    }); 

});
