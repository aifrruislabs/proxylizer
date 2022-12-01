export default function(context) {
    
    console.log("Auth Middleware")

    var auth_stat = context.store.state.is_authenticated

    if (auth_stat == false) {

        var auth_user = context.store.state.auth_user
        var auth_token = context.store.state.auth_token

        //Get Auth User    
        if (auth_user == "") {
            auth_user = context.route.query['auth_user']
            if (auth_user == undefined) {
                auth_user = ""
            }
        }
        
        //Get Auth Token
        if (auth_token == "") {
            auth_token = context.route.query['auth_token']
            if (auth_token == undefined) {
                auth_token = ""
            }
        }

        //Check if Auth User is not Empty
        if ( auth_user !== "" ) {

            //Check if Auth Token is not Empty
            if (auth_token != "") {

                //Validate Token
                return context.redirect('/noch/?auth_user='+auth_user+'&auth_token='+auth_token)
                
            }else {
                return context.redirect('/noch')
            }

        }else {
            return context.redirect('/noch')
        }

    }else {
        console.log("Authenticated")
        context.next
    }
}