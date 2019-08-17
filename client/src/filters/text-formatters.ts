
import Vue from 'vue';
import AuthManager from '../store/auth/auth';

export const seenByMe = Vue.filter('seenByMe', (seenUsernames: string[]) => {

    const currentLoggedInUser =  AuthManager.getLoggedInUser();

    const result =  seenUsernames.includes(currentLoggedInUser) ? 'seen' : 'unseen';
    // console.log(' Current username : ' + currentLoggedInUser + '. seen class ? '+ result );

    return result;
});
