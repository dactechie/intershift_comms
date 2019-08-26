
export function getUsername(state) {
    // console.log (" getting usernamne from state ", state);
    return state.username;
}
export function getToken(state) {
    // console.log (" getting usernamne from state ", state);
    return state.token;  // or localStorage.getItem('token');
}
