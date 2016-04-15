 var login = "{{ user }}"

  var CourseSearch = React.createClass({
    getInitialState: function() {
      return {
         value: 'COS 226',
         courses: []
      };
    },
    handleChange: function(ev) {
      ev.preventDefault();
      this.setState({value: ev.target.value});
    },
    handleClick: function(ev){
      ev.preventDefault();
      this.setState({value: ''});
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
        <h5>Add a class to a semester</h5>
            <div id="custom-search">
                <form onSubmit={this.submit}>
                <div className="input-group col-md-12">
                    <input type="text" className="form-control input-lg" placeholder="Type course (COS 126)" value={this.state.value} 
                    onClick={this.handleClick} onChange={this.handleChange}/>
                    <span className="input-group-btn">
                        <button  id="search-btn" className="btn btn-info btn-lg" type="button">
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
