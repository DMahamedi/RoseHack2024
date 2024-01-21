console.log("This is a popup!")

document.addEventListener('click', async (e) => {
    const article = e.target.closest('article');
    console.log('click');
    if (article) {
        const text = article.textContent.trim();
        try {
            const response = await fetch('http://localhost:5000/classify', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ text: text }),
            });
            const result = await response.json();
            console.log('Classification Result:', result.class);
            // Do something with the classification result
        } catch (error) {
            console.error('Error:', error);
        }
    }
});