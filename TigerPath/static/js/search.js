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
            $('#courses-found').before("<div class='row'><p><br>Matched Courses</p>"); //Header
          	$("#courses-found").append("<div class='list-group'>");
             for (var x in json.matched_courses){
             		var Fall = false;
             		var Spring = true;
            		 $("#courses-found").append(
				              "<span class='list-group col-md-12'>" +
				                  '<div class="btn-group" style="width: 100%">' +
				                    '<form class= "form-inline" action= "" method= "post">{% csrf_token %}' +
				                      '<li class="list-group-item">' + courses[x][0] + " " + courses[x][1] + " " + courses[x][2] +
				                        '<select class="form-control" name="semester">');
            		 //Conditional lists for adding
            		 if (courses[x][2] == 1 || courses[x][4] == 1){
            		 	Spring = true;
            		 }
            		 if (courses[x][3] == 1 || courses[x][5] == 1){
            		 	Fall = true;
            		 }
            		 if (Fall == true && Spring == true) {
            		 	$("#courses-found").append(
            		 		'<option>Freshman Fall</option>' +
                            '<option>Freshman Spring</option>' +
                            '<option>Sophomore Fall</option>' +
                            '<option>Sophomore Spring</option>' +
                            '<option>Junior Fall</option>' +
                            '<option>Junior Spring</option>' +
                            '<option>Senior Fall</option>' +
                            '<option>Senior Spring</option>');
            		 } else if (Spring == true && Fall == false){
            		   	$("#courses-found").append(
            		   		'<option>Freshman Spring</option>' +
                            '<option>Sophomore Spring</option>' +
                           ' <option>Junior Spring</option>' +
                            '<option>Senior Spring</option>');
            		 } else{
            		 	$("#courses-found").append(
            		   		'<option>Freshman Fall</option>' +
                           '<option>Sophomore Fall</option>' +
                            '<option>Junior Fall</option>' +
                            '<option>Senior Fall</option>');
            		 }
            		 $("#courses-found").append(
            		 	'</select>' +
                       '<select class="form-control" name ="COSreq">' +
                            '<option>N/A</option>' +
                            '<option>Theory</option>' +
                            '<option>Systems</option>' +
                            '<option>Applications</option>' +
                            '<option>Other</option>' +
                        '</select>' +
                        '<input type="hidden" name="listing" value='+ courses[x][0] +'>' +
                        '<input type="submit" class="btn btn-info" value="Add Class">' +
                      '</li>' +
                    '</form>' +
                  '</div>' +
              '</span>'
              );            		 
       		  }
       		  $("#courses-found").append('</div>');
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


                            {% if x.F15 or x.F16 %}
                            <option>Freshman Fall</option>
                            {% endif %}                             
                            {% if x.S15 or x.S16 %}
                            <option>Freshman Spring</option>
                            {% endif %}
                            {% if x.F15 or x.F16 %}
                            <option>Sophomore Fall</option>
                            {% endif %}
                            {% if x.S15 or x.S16 %}
                            <option>Sophomore Spring</option>
                            {% endif %}
                            {% if x.F15 or x.F16 %}
                            <option>Junior Fall</option>
                            {% endif %}
                            {% if x.S15 or x.S16 %}
                            <option>Junior Spring</option>
                            {% endif %}
                            {% if x.F15 or x.F16 %}
                            <option>Senior Fall</option>
                            {% endif %}
                            {% if x.S15 or x.S16 %}
                            <option>Senior Spring</option>
                            {% endif %}
                        </select>
                        <select class="form-control" name ="COSreq">
                            <option>N/A</option>
                            <option>Theory</option>
                            <option>Systems</option>
                            <option>Applications</option>
                            <option>Other</option>
                        </select>
                        <input type="hidden" name="listing" value={{x.listings}}>
                        <input type="submit" class="btn btn-info" value="Add Class">
                      </li>
                    </form>
                  </div>
              </span>
              {% endfor %}
              </div>
        {% endif %}