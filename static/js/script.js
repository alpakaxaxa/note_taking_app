showName();

//gets executed when enter button is clicked (see index.html)
function submitName() {
    let nameElement = document.getElementById("name");
    let name = nameElement.value;
    if (name === "") {
        alert("Enter a name")
        return
    }
    localStorage.setItem("name", name);
    showName();
}

function showName() {
    let messageElement = document.getElementById("message");
    let greeting = "Welcome ";
    let name = localStorage.getItem("name");
    if (name === null) {
        let nameForm = document.getElementById("nameForm");
        nameForm.style.display = "block";
        //in order to concatenate message and name I think I have to assign "" to name
        name = "";
    } else {
        let nameForm = document.getElementById("nameForm");
        nameForm.style.display = "none";
    }
    let message = greeting + name;
    messageElement.innerHTML = message;
}