console.log("Printing the tango from Django");
$(document).ready( function() {

    $("#about-btn").click( function(event) {
        alert("You clicked the button using JQuery!");
    });
});

$(document).ready( function() {
    console.log("document is ready");
    $("#search-btn").click( function(event) {
        event.preventDefault();
        console.log("Click thing worked");
        alert("You clicked the button using JQuery!");
    });
});