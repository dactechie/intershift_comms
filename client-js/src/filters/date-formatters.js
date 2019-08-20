import { distanceInWordsToNow, format } from 'date-fns';
import Vue from 'vue';

export const friendlyDate = Vue.filter('friendlyDate', (inputDate) => {
    
    const result = distanceInWordsToNow(inputDate) + " ago. \n(" + format(inputDate, "ddd, d MMM") +")";
    return result;
});
