let fetchResult = false;

document.addEventListener('click', async (e) => {
    const article = e.target.closest('article');
    if (article) {
        const text = article.textContent.trim();
        console.log(text);

        // Prepare the data to be sent in the request
        const data = { text: text };

        // Send a POST request to the FastAPI backend
        try {
            const response = await fetch('http://127.0.0.1:8000/predict', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(data),
            });

            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }

            const result = await response.json();
            // console.log('Probability:', result.probability);
            // Update the variable with the boolean value
            fetchResult = result.probability;
            console.log('Probability:', fetchResult);

            if (!fetchResult) {
                article.style.color = 'black';
            }

        } catch (error) {
            console.error('Error sending data to the server:', error);
        }
    }
});
