fetch('https://my-vercel-project-mu-henna.vercel.app/api?name=Alice&name=Bob')
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Error:', error));
