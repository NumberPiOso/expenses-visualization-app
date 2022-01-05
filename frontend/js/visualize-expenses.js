// Pablo Osorio
// 03/01/2022
// Custom defined functions for the API

const url = "http://127.0.0.1:8000"

const expenseList = document.querySelector('#ExpenseList');


const addMovesToList = async () => {
    const moves = await getAllMoves();
    for (const move of moves) {
        const newLI = document.createElement('LI');
        newLI.append(`<b>Type of move:</b> ${move.type_move} --> Value ${move.value}`);
        expenseList.append(newLI)
    }
}


const getAllMoves = async () => {
    try {
        const config = {}
        const res = await axios.get(`${url}/api/move/`, config)
        return res.data;
    } catch (e) {
        console.log(e)
    }

}

document.addEventListener('DOMContentLoaded', addMovesToList, false);
