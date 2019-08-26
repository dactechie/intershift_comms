import { mutations, STORAGE_KEY } from './mutations'
import actions from './actions'

export default {
    state: {
        user: JSON.parse(window.localStorage.getItem(STORAGE_KEY) || '[]')
    },
    actions,
    mutations,
}