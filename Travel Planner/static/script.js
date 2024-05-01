document.getElementById('travelForm').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent form submission

    const destination = document.getElementById('destination').value;
    const budget = document.getElementById('budget').value;
    const startDate = document.getElementById('startDate').value;
    const numDays = document.getElementById('numDays').value;
    const interest = document.getElementById('interest').value;  // Retrieve user's interests

    // Send trip planning request to backend
    fetch('/plan', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            destination: destination,
            budget: budget,
            startDate: startDate,
            numDays: numDays,
            Interest: interest  // Include the user's interests in the request payload
        })
    })
    .then(response => response.json())
    .then(data => {
        // Display trip results
        const tripResultsDiv = document.getElementById('tripResults');
        tripResultsDiv.innerHTML = `
            <h2>Trip Plan</h2>
            <p><strong>Destination:</strong> ${data.destination}</p>
            <p><strong>Accommodations:</strong> ${data.accommodations.join(', ')}</p>
            <p><strong>Activities:</strong> ${data.activities.join(', ')}</p>
            <p><strong>Itinerary:</strong> ${data.itinerary}</p>
        `;
        tripResultsDiv.style.display = 'block';
    })
    .catch(error => {
        console.error('Error:', error);
    });
});
