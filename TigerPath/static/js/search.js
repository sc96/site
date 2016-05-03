$(function() {
$('#course-search').on('submit', function(event){
	event.preventDefault();
	console.log("form submitted ya dumbass")
	search_courses();
});

function search_courses() {
    console.log("search_courses!") // sanity check
    console.log($('#course-search-text').val())
    $.ajax({
        url : "", // the endpoint
        type : "GET", // http method
        data : { the_query : $('#course-search-text').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
            $('#course-search-text').val(''); // remove the value from the input
            courses = json.matched_courses
            for (var x in courses){
            	for (var y in courses[x]){
            		console.log(courses[x][y]);
            	}
            	
            }
            console.log(json.matched_courses); // log the returned json to the console
             console.log("success"); // another sanity check
             for (var x in json.matched_courses) {
            		 $("#courses-found").prepend("<li><strong>"+json.matched_courses[x][0]+"</strong> - <em> "+json.matched_courses[x][1]+"</em> - <span> "something"</span></li>");
       		  }
    			console.log("success"); // another sanity check
		},	


        // handle a non-successful response
        error : function(xhr,errmsg,err) {
            $('#results').html("<div class='alert-box alert radius' data-alert>Oops! We have encountered an error: "+errmsg+
                " <a href='#' class='close'>&times;</a></div>"); // add the error to the dom
            console.log(xhr.status + ": " + xhr.responseText); // provide a bit more info about the error to the console
        }
    });
};
});

