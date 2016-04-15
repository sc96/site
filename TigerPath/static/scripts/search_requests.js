console.log("Printing the tango from Django");

$(document).ready( function() {
    console.log("document is ready");
    $("#search-btn").click( function(event) {
        console.log("Click thing worked");
        alert("You clicked the button using JQuery!");
    });
});