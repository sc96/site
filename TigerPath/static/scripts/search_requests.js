$(document).ready( function() {
    console.log("document is ready");
    $("search-btn").click( function(event) {
        event.preventDefault();
        console.log("Click thing worked");
        alert("You clicked the button using JQuery!");
    });
});