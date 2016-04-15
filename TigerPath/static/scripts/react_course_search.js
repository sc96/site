 var login = "{{ user }}"

 var LikeButton = React.createClass({
  getInitialState: function() {
    return {liked: false};
  },
  handleClick: function(event) {
    this.setState({liked: !this.state.liked});
  },
  render: function() {
    var text = this.state.liked ? 'like' : 'haven\'t liked';
    return (
      <p onClick={this.handleClick}>
        You {text} this. Click to toggle.
      </p>
    );
  }
});

ReactDOM.render(
  <LikeButton />,
  document.getElementById('example')
);

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

        <div className="row">
        <div className="col-md-12">
        <h5>Search for your class</h5>
            <div id="custom-search">
                <form onSubmit={this.submit}>
                <div className="input-group col-md-12">
                    <input type="text" className="form-control input-lg" placeholder="COS 226" onClick={this.handleClick} onChange={this.handleChange}/>
                    <span className="input-group-btn">
                        <button  onClick={alert('You clicked the button using Javascript.')} className="btn btn-info btn-lg" type="button">
                            <i className="glyphicon glyphicon-search"></i>
                        </button>
                    </span>
                </div>
                </form>
            </div>
        </div> 
     </div>
      );
     }
  });



  var Courses = React.createClass({
    getInitialState: function() {
      return {
        matches: "{{all_courses}}"
      };
    },
    searchCourses: function(ev) {
      var matchedcourses = [];
      var all_courses = "{{all_courses}}"
      var j = 0;
      for (x in all_courses) {
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
      <CourseSearch username={login}/>,
      document.getElementById('message')
    );