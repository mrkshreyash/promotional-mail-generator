import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

sender_email = "sender@email.com"
password = "xxxx xxxx xxxx xxxx"

receiver_email = "receiver@email.com"
subject = "Testing Promotional Mail through Python !"

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = receiver_email
message['Subject'] = subject


html = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            body{
                font-family: Arial, sans-serif;
                background-color: #f4f4f4;
                margin: 0;
                padding: 0;
            }
            
            .container{
                background-color: #ffffff;
                width: 600px;
                margin: 20px auto;
                padding: 20px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }
            
            .header{
                background-color: #007bff;
                color: #ffffff;
                padding: 10px;
                text-align: center;
                border-radius: 8px 8px 0 0;
            }
            
            .content{
                margin: 20px 0;
                text-align: center;
            }
            
            .footer{
                text-align: center;
                font-size: 12px;
                color: #888888;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1> Welcome to the Pure Technology.</h1>
            </div>
            <div class="content">
                <h3 style="color: red;">NOTE: This mail is TEST mail and sent from the Python program.</h3>
                <p style="text-align:justify;">
                    We can utilize the power of <b>HTML, CSS and Python</b> to send the mails to receivers in this format. <br>
                    It will be professional way to send mails to the receivers like we send the task details to the candidates.<br>
                    We can utilize this product in other way also.
                </p>
                <hr>
                <p>This is not the final program. The product is in the initial phase of developement.</p>
                <p style="color: green;">I have better ideas in my mind to utilize the power of <b>HTML, CSS with Python </b> to create a exceptional product like this. </p>
                <a href="https://puretechnology.in/"><b>Visit Our Website</b></a>
            </div>
            
            <div class="footer">
                <p>
                    <strong>AND HERE IS THE SMALL DEMO FROM MY SIDE.</strong>
                    <p><i>Let me know your thoughts on this idea.</i></p>
                </p>
            </div>
            
            <div class="content">
                <p>
                    <hr>
                    <b>Thanks and Warm Regards,</b><br>
                    Shreyash A. Kamble<br>
                    (Jr. AI Developer Intern)
                </p>
            </div>
            
        </div>
    </body>
</html>
"""

message.attach(MIMEText(html, "html"))

with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
    server.login(sender_email, password)
    server.send_message(message)

print("Email sent successfully !")
