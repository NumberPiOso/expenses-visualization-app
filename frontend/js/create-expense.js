// Pablo Osorio
// 05/01/2022
// Custom defined functions for the API

const url = "http://127.0.0.1:8000"

function handleSubmit(event) {
    event.preventDefault();

    const data = new FormData(event.target);
    const value = Object.fromEntries(data.entries());
    console.log(JSON.stringify(value));

    document.querySelector('#CreateExpense').reset(); // good enough ;)



}

const form = document.querySelector('#CreateExpense');
form.addEventListener('submit', handleSubmit);