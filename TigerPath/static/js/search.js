$(function() {
$('#course-search').on('submit', function(event){
	event.preventDefault();
	console.log("form submitted ya dumbass")
	search_courses();
});

function search_courses() {
    console.log("search_courses!") // sanity check
    console.log($('#course-search-text').val())
    console.log("Is it the same as?")
    console.log($('#course-search').val())
};


});