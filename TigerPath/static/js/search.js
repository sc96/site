$(document).ready(function () {
var CourseSearch = React.createClass({

  displayName: "CourseSearch",
  getInitialState: function() {
         return {
             value: 'select'
         }
  },
  handleChange: function(event) {
  this.setState({value: event.target.value});
  },

  render: function render() {
    return React.createElement(
      "div",
      null,
      React.createElement(
        "div",
        { className: "row" },
        React.createElement(
          "div",
          { className: "col-md-12" },
          React.createElement(
            "h5",
            null,
            "Add a class to a semester"
          ),
          React.createElement(
            "span",
            { id: "custom-search" },
            React.createElement(
              "form",
              { id: "course-search", className: "form-inline", action: true, method: "get" },
              React.createElement(
                "div",
                { className: "input-group col-md-12" },
                React.createElement("input", { type: "text", className: "form-control input-lg", placeholder: "Type course (e.g. COS 126)", defaultValue: "{{test}}", id: "course-search-text", name: "q", value: this.state.value, onChange: this.handleChange}),
                React.createElement(
                  "span",
                  { className: "input-group-btn" },
                  React.createElement(
                    "button",
                    { id: "search-btn", className: "btn btn-info btn-lg", type: "submit" },
                    React.createElement("i", { className: "glyphicon glyphicon-search" })
                  )
                )
              )
            )
          )
        ),
        " "
      ),
      " ",
      React.createElement("br", null)
    );
  }
});

ReactDOM.render(
      React.createElement(CourseSearch, null),
      document.getElementById('search-bar')
      );
});




$(function() {
	
$('#course-search').on('submit', function(event){
	event.preventDefault();
	search_courses();
});
$('#course-search-text').change(function(event){
	// event.preventDefault();
	search_courses();
});

function search_courses() {
    // console.log("search_courses!") // sanity check
    // console.log($('#course-search-text').val())
    $.ajax({
        url : "", // the endpoint
        type : "GET", // http method
        data : { the_query : $('#course-search-text').val() }, // data sent with the post request

        // handle a successful response
        success : function(json) {
        	var CSRF_TOKEN = getCookie('csrftoken');
            // $('#course-search-text').val(''); // remove the value from the input
            courses = json.matched_courses
            // for (var x in courses){
            // 	for (var y in courses[x]){
            // 		console.log(courses[x][y]);
            // 	}

            //}
            $('#courses-found').empty();
          	var html = "<div class='col-md-12'><p><br>Matched Courses</p><div class='list-group'>"; //Header
            for (var x in json.matched_courses){
             		var Fall = false;
             		var Spring = false;
             		var element = ""
             		//Conditional lists for adding
            		 if (courses[x][2] == 1 || courses[x][4] == 1){
            		 	Spring = true;
            		 }
            		 if (courses[x][3] == 1 || courses[x][5] == 1){
            		 	Fall = true;
            		 }
            		 
            		 element +=
				              "<span class='list-group col-md-12'>" +
				                  '<div class="btn-group" style="width: 100%">' +
				                    '<form class= "form-inline" action= "" method= "post"><input type="hidden" name="csrfmiddlewaretoken" value=' + CSRF_TOKEN + '>' + //{% csrf_token %}
				                      '<li class="list-group-item"><b>' + courses[x][0] + "</b>  " + courses[x][1] + " " + courses[x][2] + " ";
            		 
            		 if (Fall == true && Spring == true) {
            		 	element +=
            		 		'<select class="form-control" name="semester">' +
            		 		'<option>Freshman Fall</option>' +
                            '<option>Freshman Spring</option>' +
                            '<option>Sophomore Fall</option>' +
                            '<option>Sophomore Spring</option>' +
                            '<option>Junior Fall</option>' +
                            '<option>Junior Spring</option>' +
                            '<option>Senior Fall</option>' +
                            '<option>Senior Spring</option>' +
                            '</select>';
            		 } else if (Spring == true && Fall == false){
            		   	element +=
            		   		'<select class="form-control" name="semester">' +
            		   		'<option>Freshman Spring</option>' +
                            '<option>Sophomore Spring</option>' +
                           ' <option>Junior Spring</option>' +
                            '<option>Senior Spring</option>' +
                            '</select>';
            		 } else{
            		 	element+=
            		 		'<select class="form-control" name="semester">' +
            		   		'<option>Freshman Fall</option>' +
                           '<option>Sophomore Fall</option>' +
                            '<option>Junior Fall</option>' +
                            '<option>Senior Fall</option>' +
                            '</select>';
            		 }
            		 element +=
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
              ;   
              // console.log(element);
       		  html += element;         		 
       		  }
       		  html += "</div></div>"
       		  $("#courses-found").append(html);
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

// Needed to get CSRF token
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


});