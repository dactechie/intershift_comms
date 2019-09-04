
export default  {
    getUsername: function (state) {
    // console.log (" getting usernamne from state ", state);
    return state.username;
},
 getToken: function(state) {
    // console.log (" getting usernamne from state ", state);
    return state.token;  // or localStorage.getItem('token');
},
 getLoggedInUser: function(state) {
    // console.log (" getting usernamne from state ", state);
    return  JSON.parse(localStorage.getItem('user')) //state.user[0];
}
}