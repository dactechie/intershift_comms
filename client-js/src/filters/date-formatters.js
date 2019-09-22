import { formatRelative } from 'date-fns';
import Vue from 'vue';

const baseDate = new Date();
export const friendlyDate = Vue.filter('friendlyDate', (inputDate) => {
    const d = new Date(inputDate)
    const result = formatRelative(d, baseDate)
    // distanceInWordsToNow(inputDate) + " ago. \n(" + format(d, 'do MMMM') +")";
    return result;
});
