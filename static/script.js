// Vote for a choice
async function vote(choice) {
    try {
        const response = await fetch('/api/vote', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ choice })
        });

        const data = await response.json();

        if (data.success) {
            // Add voted animation
            const button = document.getElementById(`vote-${choice}`);
            button.classList.add('voted');
            setTimeout(() => button.classList.remove('voted'), 500);

            // Update results
            updateResults();
        }
    } catch (error) {
        console.error('Error voting:', error);
    }
}

// Fetch and update results
async function updateResults() {
    try {
        const response = await fetch('/api/results');
        const data = await response.json();

        document.getElementById('python-percentage').textContent =
            data.percentages.python + '%';
        document.getElementById('javascript-percentage').textContent =
            data.percentages.javascript + '%';
        document.getElementById('total-votes').textContent = data.total;
    } catch (error) {
        console.error('Error fetching results:', error);
    }
}

// Initialize and auto-refresh results
updateResults();
setInterval(updateResults, 2000);
