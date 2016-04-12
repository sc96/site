var login = "{{ user }}"
var CourseSearch = React.createClass({
   getInitialState: function() {
    return {
       value: 'COS 226',
       courses: []
    };
  },
  handleChange: function(ev) {
    this.setState({value: ev.target.value});
  },
  handleClick: function(ev){
    if (this.state.value == 'COS 226'){
          this.setState({value: ''})}
  },
  submit: function(ev) {
    ev.preventDefault();
    var matchedCourses = <Courses query={this.state.value} username={this.props.username}/>
    this.setState({value: '', courses: ["hi"].concat(matchedCourses)});

  },
  render: function() {
    return (
      <div>
      <div>{this.state.user}
      </div>
      Add a Course:
      <form onSubmit={this.submit}>
        <input type="text" value={this.state.value}
          onClick={this.handleClick}
          onChange={this.handleChange} />
        <input type="submit" value="Search" />
      </form>
      <div>
      {this.state.courses}
      </div>
      </div>
    );
   }
});

var Courses = React.createClass({
  getInitialState: function() {
    return {
      matches: ["wow"]
    };
  },
  searchCourses: function(ev) {
    var matchedcourses = [];
    var stuff = "{{all_courses}}"
    var j = 0;
    for (x in stuff) {
      if (j > 10) {break;}
      matchedcourses.push(x);
      j = j + 1;
    }
    this.setState({matches: matchedcourses});
  },

  render: function() {
    return (
      <div>{this.state.matches}</div>
    );
   }
});

ReactDOM.render(
    <CourseSearch username="login"/>,
    document.getElementById('message')
  );
