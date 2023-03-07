function uploadFile(){
    const btn = document.querySelector(".button");
    btn.classList.add("button--loading");


    let photo = document.getElementById("file_input_hidden").files[0];
    let formData = new FormData();
        
    formData.append("file", photo);
    fetch("/display", {
        method: 'POST',
        body: formData
    }).then(response => response.json())
    .then(data => { var result = data.result;
        var text = document.getElementById("texts");
        if(result.length == 0){
            text.innerHTML = "The Image Has No Text";
            text.style.color = "red";
            text.style.fontSize = "24px"
            btn.classList.remove("button--loading");
        }
        else{
            console.log(result)
            text.innerHTML = "<p> Result:<br><br>" + result + "</p>";
            text.style.color = "green"
            text.style.fontSize = "24px"
            btn.classList.remove("button--loading");
        }
    })
    // use the result to update the JavaScript variable
    
}
function resetText(){
    var text = document.getElementById("texts");
    text.innerHTML = "Text";
    text.style.color = "black";
    
}