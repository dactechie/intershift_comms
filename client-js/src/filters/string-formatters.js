
import Vue from 'vue';

export const properFirstname = Vue.filter('properFirstname', (username) => {

    let fName = username.substr(0, username.indexOf('.')); 
    return fName.charAt(0).toUpperCase() + fName.substr(1).toLowerCase();
 
});