export const state = () => ({
    
    // api : 'https://proxylizer.aifrruislabs.com/api/v1',

    api : 'http://127.0.0.1:8000/api/v1',
    
    auth_user: '',

    auth_token: '',

    is_authenticated: false,

})

export const mutations = {
    //Store Auth Data
    store_auth_data(state, auth_data) {
        state.auth_user = auth_data.auth_user
        state.auth_token = auth_data.auth_token
        state.is_authenticated = true 
    }, 
    
    //Clear Auth Data
    clear_auth_data(state) {
        state.auth_user = ''
        state.auth_token = ''
        state.is_authenticated = false
    },

}
