import { toDate, parseISO, formatDistanceToNow } from 'date-fns';
import Vue from 'vue';

export const friendlyDate = Vue.filter('friendlyDate', (inputDate: string) => {
    return inputDate;
    // const inputD  = parseISO (inputDate);
    // const result = formatDistanceToNow(toDate(inputD), { addSuffix: true });
    // return result;
});
