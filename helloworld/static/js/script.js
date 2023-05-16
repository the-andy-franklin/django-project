document.addEventListener('DOMContentLoaded', function() {
  const newQuoteButton = document.getElementById('new-quote-button');
  const quoteText = document.getElementById('quote-text');
  const authorText = document.getElementById('author-text');

  newQuoteButton.addEventListener('click', function() {
      fetchNewQuote();
  });

  function fetchNewQuote() {
      fetch('https://api.quotable.io/quotes/random')
          .then(response => response.json())
          .then(data => {
              const { content, author } = data[0];
              quoteText.innerText = content;
              authorText.innerText = '- ' + author;
          })
          .catch(error => {
              console.log('Error:', error);
              quoteText.innerText = 'Failed to fetch a new quote.';
          });
  }
});