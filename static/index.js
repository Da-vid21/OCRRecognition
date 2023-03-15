window.addEventListener('load', function() {
    var dragDropElement = document.getElementById("drag_drop");

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
          dragDropElement.addEventListener(eventName, function(e) {
            e.preventDefault();
            e.stopPropagation();
        }, false)
    });

    dragDropElement.addEventListener("drop", function(event) {
        var boxText = document.getElementById("output-text");
        boxText.innerHTML = "Processing...";
        boxText.style.color = "white"
        event.stopPropagation();
        event.preventDefault();

        var dt = event.dataTransfer;
        var files = dt.files;
        var url = "/display";
        var formData = new FormData();
        formData.append('file', files[0]);

        fetch(url, {
            method: 'POST',
            body: formData
        }).then(response => response.json())
        .then(data => { var result = data.result;
            var text = document.getElementById("output-text");
            
            if(result.length == 0){
                text.innerHTML = "The Image Has No Text";
                text.style.color = "red";
                text.style.fontSize = "24px"
            }
            else{
                console.log(result)
                text.innerHTML = result + "</p>";
                text.style.color = "#0bf90b"
                text.style.fontSize = "24px"
                title.innerHTML = "Result";
                title.style.color = "#0bf90b"
                
            }
        })
        // use the result to update the JavaScript variable
    
    });
    

});
function uploadFile() {
    const btn = document.querySelector(".button");
    btn.classList.add("button--loading");
  
    let photo = document.getElementById("file_input").files[0];
    let formData = new FormData();
  
    formData.append("file", photo);
    fetch("/display", {
      method: 'POST',
      body: formData
    }).then(response => response.json())
    .then(data => { var result = data.result;
        var text = document.getElementById("output-text");
        if(result == "<Response 440 bytes [200 OK]>"){
            text.innerHTML = "The Image Has No Text";
            text.style.color = "red";
            text.style.fontSize = "24px"
            btn.classList.remove("button--loading");
        }
        else{
            
            text.innerHTML = result;
            text.style.color = "#0bf90b"
            text.style.fontSize = "24px"
            btn.classList.remove("button--loading");
            const textHeight = text.clientHeight;
            
        }
    })
}
  
function resetText(){
    var text = document.getElementById("output-text");
    text.innerHTML = "Drag and Drop in the box";
    text.style.color = "white";
    
}
function copyToClipboard() {
    var copyText = document.getElementById("output-text");
    var copyButton = document.getElementById("copy-button");
    console.log(copyText);
    if(copyText.innerHTML == "Drag and Drop in the box" || copyText.innerHTML == "The Image Has No Text"){
        copyButton.innerHTML = "Nothing to copy!";
    }
    else{
        navigator.clipboard.writeText(copyText.innerText);
        copyButton.innerHTML = "Copied to Clipboard!";
    }
}
  

