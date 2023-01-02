// console.log(fetch("https://dog.ceo/api/breeds/image/random"))
fetch('https://reqres.in/api/user/')
    .then(res => res.json())
    .then(data => console.log(data))