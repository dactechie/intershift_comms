import { distanceInWordsToNow } from 'date-fns';
import Vue from 'vue';

export const friendlyDate = Vue.filter('friendlyDate', (inputDate: string) => {
    const result = distanceInWordsToNow(inputDate);
    return result;
});
