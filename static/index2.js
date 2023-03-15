window.addEventListener('load', function() {
    var dragDropElement = document.getElementById("drop-zone");

    ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
          dragDropElement.addEventListener(eventName, function(e) {
            e.preventDefault();
            e.stopPropagation();
        }, false)
    });

    dragDropElement.addEventListener("drop", function(event) {
        var boxText = document.getElementById("texts")
        boxText.innerHTML = "Processing...";
        boxText.style.color = "black"
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
            var text = document.getElementById("texts");
            if(result.length == 0){
                text.innerHTML = "The Image Has No Text";
                text.style.color = "red";
                text.style.fontSize = "24px"
            }
            else{
                console.log(result)
                text.innerHTML = "<p> Result:<br><br>" + result + "</p>";
                text.style.color = "green"
                text.style.fontSize = "24px"
            }
        })
        // use the result to update the JavaScript variable
    
    });
    

});
