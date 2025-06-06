// Add confirmation for delete actions
document.addEventListener('DOMContentLoaded', function() {
    // Delete confirmation
    const deleteButtons = document.querySelectorAll('.btn-danger');
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this note?')) {
                e.preventDefault();
            }
        });
    });

    // Priority color update in forms
    const prioritySelect = document.getElementById('id_priority');
    if (prioritySelect) {
        prioritySelect.addEventListener('change', function() {
            // Remove all priority classes
            this.classList.remove('priority-high', 'priority-medium', 'priority-low');
            
            // Add appropriate class
            this.classList.add(`priority-${this.value}`);
        });
        
        // Initialize on load
        prioritySelect.classList.add(`priority-${prioritySelect.value}`);
    }

    // Date picker enhancement
    const dateInputs = document.querySelectorAll('input[type="datetime-local"]');
    dateInputs.forEach(input => {
        // Set min date to today
        const today = new Date().toISOString().slice(0, 16);
        input.min = today;
    });
});