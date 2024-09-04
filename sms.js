const express = require('express')
const twillio = require('twillio')
const dotenv = require('dotenv')
const app = express()

dotenv.config()



function sendSMS(){

    const client = new twillio(process.env.TWILIO_SID,process.env.TWILIO_AUTH_TOKEN)

    return client.messages
    .create({body:'issue',from:'9118433477',to:process.env.PHONE_NUMBER})
    .then(message=>{
        
        
        console.log(message,"message sent")})
    .catch(err => {
        console.log(err,"message not send")})
        

}
sendSMS()

app.listen(5000, ()=> console.log('listning at port 5000'))
