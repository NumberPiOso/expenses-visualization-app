// Pablo Osorio
// 05/01/2022
// Custom defined functions for the API

const url = "http://127.0.0.1:8000"

const postMove = async (move) => {
    try {
        // console.log(move)
        move_renamed_keys = {
            type_move: move["inputType"],
            value: move["inputValue"],
            description: move["inputDescription"]
        }
        const config = {}
        const res = await axios.post(`${url}/api/move/`, move_renamed_keys)
        return res.data;
    } catch (e) {
        console.log(e)
    }

}

const addSuccesfullNote = () => {
    var element = document.querySelector("#savedMoveNote");
    element.classList.remove("d-none")
    element.textContent = "Movement saved";
}


function handleSubmit(event) {
    event.preventDefault();

    // Save move
    const form_data = new FormData(event.target);
    const move_input = Object.fromEntries(form_data.entries());
    succesfull_move = postMove(move_input);

    // reset form
    document.querySelector('#CreateExpense').reset(); // good enough ;)

    // Add succesful note
    addSuccesfullNote();
}


const form = document.querySelector('#CreateExpense');
form.addEventListener('submit', handleSubmit);