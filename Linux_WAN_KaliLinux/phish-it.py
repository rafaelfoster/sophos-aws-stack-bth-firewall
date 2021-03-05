#!/usr/bin/python3

import os
import time
import smtplib
from pyfiglet import Figlet
from termcolor import colored
import email, smtplib

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

victim_addr = ""

custom_fig = Figlet(font='alligator2')
print(custom_fig.renderText('Phish'))
print(custom_fig.renderText('it'))

time.sleep(1)

print("\n\n")

custom_fig = Figlet(font='banner')
print(custom_fig.renderText('For Sophos BTH training only'))

def main():
    cont_menu = True
    while cont_menu:
            print ("""
1) Phishing attack
0) Exit/Quit
            """)
            option = input("What would you like to do? ")

            if option=="1":
                menu_1_phishing()
            elif option=="0":
                print("\n\n")
                custom_fig = Figlet(font='cosmic')
                print(custom_fig.renderText('See Ya'))
                print(colored("\nHappy Hacking! ;)\n\n\n", "green"))
                break
            elif option != "":
                print("\nNot Valid Choice Try again")

def menu_1_phishing():
    cont_menu = True
    while cont_menu:
        print ("""
1) Send malicious attachment
2) Send malicious link
0) Back to main menu
        """)
        option_menu1 = input("What would you like to do? ")
        if option_menu1=="1":
            option_menu1_set = True
            cmd_option_menu1 = "weaponized_pdf"
        elif option_menu1=="2":
            option_menu1_set = True
            cmd_option_menu1 = "malicious_url"
        elif option_menu1=="0":
                break
        elif option_menu1 != "":
                print("\nNot Valid Choice Try again")

        if option_menu1_set:
            phishing_shell(cmd_option_menu1)

def phishing_shell(cmd_option):
    run_shell = True
    global victim_addr

    print(colored("\n[*] - ", "cyan") + "Now set the victim's email address\n")

    while run_shell:
        default_ps1 = "sendMail(" + colored("phishing_attack/" + cmd_option, "red") + ") > "
        shell_command = input(default_ps1)
        if "set" in shell_command.lower():
            print("{} => {}".format(shell_command.split(" ")[1],shell_command.split(" ")[2]))
            victim_addr = shell_command.split(" ")[2]
        elif shell_command.lower() == "run":
            if victim_addr is None:
                print(colored("\n[~]", "red") + "User email not defined!\n")
            else:
                if cmd_option == "weaponized_pdf":
                    send_pdf(victim_addr)
                elif cmd_option == "malicious_url":
                    send_url(victim_addr)
                return True
        elif shell_command.lower() == "exit":
            break

        else:
            print(colored("\n[~]", "red") + "Command unknown! Are you sure you're a hacker?\n")

def send_pdf(victim_addr):
    print(colored("\n[*] - ", "cyan") + "We'll send a pretty cool file for they play with :) \r")
    attachment = "/usr/share/set/resume_jsmith.pdf"
    return sendMail(victim_addr, "Data Center opportunity - Resume John Smith", template_weaponized_file, attachment)

def send_url(victim_addr):
    global template_malicous_url
    print(colored("\n[*] - ", "cyan") + "We'll send a very decent URL! (Hope they click on it :D )")
    
    if sendMail(victim_addr, "Google Drive - Resume John Smith", template_malicous_url):
        print( colored("\n[+] - Done! ", "green") + "User should receive our toy anytime soon")    

def sendMail(smtp_receivers, subject = "TESTE EMAIL" , body = "", attachment = None):
    print(colored("\n[*] - ", "cyan") + "Sending the email address to " + colored(victim_addr, "yellow"), end =" ", flush=True)
    for i in range(1,4,1):
        print(".", end ="", flush=True)
        time.sleep(1)
    smtp_sender = "johnsmith@gmail.com"
    smtp_server_addr = "mail.evilcorp.com"
    smtp_server_port = 587
    
    header = '''From: John Smith <johnsmith@gmail.com>
To: <%s>
MIME-Version: 1.0
Subject: %s
Content-type: text/html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
</head>
''' % (smtp_receivers, subject)
    footer = "</body></html>"
    MailMsg = '''%s
%s
%s
''' % (header, body.encode("UTF-8"), footer)

    msg = MIMEMultipart()
    msg.attach(MIMEText(MailMsg, "plain"))
    msg.attach(MIMEText(open(attachment).read()))

    try:
        smtpObj = smtplib.SMTP(smtp_server_addr, smtp_server_port)

        try:
            smtp_auth_user
        except NameError:
            smtp_auth_required = False
        else:
            if smtp_server_tls:
                smtpObj.ehlo()
                smtpObj.starttls()
                smtpObj.ehlo

        smtpObj.sendmail(smtp_sender, smtp_receivers, msg.as_string())
        smtpObj.close()
        print("")
        print( colored("\n[+]Done!!", "green") + " - Email successfully sent!")
        return True
    except Exception as e:
        print(colored("\n[~]", "red") + "Error: unable to send email:  %s" % (e))
        return False
        
        
template_weaponized_file = """
Dear HR,

Please find attached a copy of my resume with detailed work experience fir the Data Center Operations Technician position posted on your linkedin.

Can we schedule a meeting to discuss my insights and ideas on making managing Data Center operations more efficient, while boosting all major KPI's?

Sincerely,

John Smith

Senior Infrastructure Architect
<a href="linkedin.com/in/johnsmith">linkedin.com/in/johnsmith</a>
<a href="mailto:johnsmith@gmail.com">johnsmith@gmail.com</a>
+1 555-000-1234
"""

template_malicous_url = """
<body bgcolor="#F5F5F5" style="margin:0; padding:0; line-height:0; font-size:0;">

<!-- WRAP & PADDING -->
<table class="mobile-background" style="background:#F5F5F5;" width="100%" cellpadding="0" cellspacing="0" border="0">
<tbody>
	<tr>
		<td class="mobile-wrapper-padding" style="line-height:0; font-size:0; padding: 3px 20px 0px 20px;">

<!-- FORCE 600px in Gmail App & ALIGNMENT via WRAP -->
<table align="center" width="600" style="width:600px;" class="responsive-table">
<tbody>
<tr>
<td class="mobile-hide" style="min-width:600px;"><img alt="Sophos" src="http://images.go.sophos.com/EloquaImages/clients/Sophos/%7B18a6c571-6c5d-481c-a065-9b566a0b8932%7D_gmail-single-pixel.gif" width="600" height="1" style="display: block; max-height: 1px; min-height: 1px; min-width: 600px; width: 600px;"></td>
</tr>
<tr>
<td style="line-height:0; font-size:0;">

<!-- Body Copy -->
<table width="100%" align="center" bgcolor="#ffffff" border="0" cellpadding="0" cellspacing="0" style="border-left:1px solid #f0f0f0;border-right:1px solid #f0f0f0">
	<tr>
    	<td class="mobile-padding" style="padding:24px 32px 24px 32px;background:#fff;border-right:1px solid #eaeaea;border-left:1px solid #eaeaea">

         	<table border="0" cellpadding="0" cellspacing="0">

                <tr>
                  <td dir="ltr" style="padding:0px 0 0 0; font-size:18px; color: #66747e; line-height:24px; font-family: Calibri, Helvetica, sans-serif;   text-align: justify;text-justify: inter-word;">
						<div style="font-size:14px;line-height:18px;color:#444"><a href="mailto:johnsmith@gmail.com" style="color:inherit;text-decoration:none" target="_blank">johnsmith@gmail.com</a> shared this file with you:</div>

						<br>

						<div style="font-size:18px;display:table"><div style="display:table-row;border-bottom:4px solid #fff"><span style="display:table-cell"><div style="height:32px"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAgAAAAIACAYAAAD0eNT6AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAN1wAADdcBQiibeAAAABl0RVh0U29mdHdhcmUAd3d3Lmlua3NjYXBlLm9yZ5vuPBoAAB90SURBVHja7d0JlCR1fcDxX8997Mmy7MXCuotcEqIIymGEsF4RIooIiiheSDwSkyiYYBTxERUx8cCHCkESDCAqBpCIF4gHeCwgcoPcuyyLBPaeq69U9Y7GwAI72z0z1V2fz0ul8flsZn7dU/9vV3dXFarVatC6lq9c1Z/cHJxsS5Jt/ma2qaYEk+O+B1b8+MX77X2QSTAZCgKgJRf92cnNq5Lt1cn2kmTrMRXInhtuui1mTp8mAhAA1LXodyU3b0+2o5Nt/2RrMxXIfgCkRACTwSLR/At/IdnekPzj7cl2ZrK9yOMKzWX12nUH/uTn111tEggAtnTxT9/bX5ZsFyTbYhMBEQACoLUX/rnJ9p3kH69MtuebCIgAEACtv/jvNfqq/y9MA0QACIB8LP6vS25+mmzbmwaIABAArb/wpx/0+2jyjxclW5+JgAgAAZCDxT+5+Y9kOznZCiYCIgAEQD58JNneZAwgAkAA5OfV/xGjr/wBESACEAA5WfzTT/unh/4d9gdEAAIgJ4v/3OTm0vCBP0AEIABy5ezwVT9ABCAAcvXq/6Dk5lCTAEQAAiA/i3/6fv+nTAIQAQiAfDky2fYxBkAEIADy8+q/K7n5uEkAIgABkC9vD5f0BUQAAiB3jjYCQAQgAHJk+cpVs5Ob/U0CEAEIgHx5lccCEAEIgPx5tREAIgABkCPLV67qT25eYhKACEAA5MvBydZjDIAIQADkyxIjAEQAAiB/5hsBIAIQAAIAQAQgAAQAgAhAAAgAABGAABAAACIAAdCcphoBIAIQAACIAAQAACIAAQCACEAAACACEAAAiAAEAAAiAAEAgAhAAAAgAgQAAIgAAQAAIkAAACACEAAAiAAEAAAiAAEAgAhAAAAgAhAAAIgABAAAIgABAIAIQAAAIAIQAACIAAQAACIAAQCACEAAACACEAAAiAAEAAAiQAAAgAgQAAAgAgQAAIgAAQAAIkAAAIAIEAAAIAIEAACIAAEAACJAAAAgAkSAAABABCAAABABCAAARAACAAARgAAAQAQgAAAQAQgAAEQAAgAAESAAAEAECAAAEAECAABEgAAAABEgAABABAgAABABAgAARIAAAAARIAAAQAQIAAAQAQIAAESAAAAAESAAAEAECAAAEAECAABEgAAAQAQgAAAQAQgAAESAAAAAESAAAEAECAAAEAECAIB6tLfZBYsAAQCQO52dHYYgAgQAQP4CoNMQRIAAAMhdAHQ4AiACBABADo8ACAARIAAAchgA3gIQAQIAIHe6uwSACBAAALkzdUp/tBUKBiECBABAnrS1tcXUqVMMQgQIAIC8mTFtqiGIAAEAkDfTBYAIEAAA+dPR0R5T+vsMQgQIAIC8mTljuiGIAAEAkDfbbjMjuru6DEIECACAPCkUCjF/7nYGIQIEAEDezJwxLfr7eg1CBAgAgLxZMG+OIYgAAQCQN+m3AZwXQAQIAIAc2mH7+dHlGgEiQAAA5Et6XoAlixbWThOMCBAAADnS29MTixbONwgRIAAA8mbG9Gkxb85sgxABAgAgb9IA2GamswSKAAEAkDuLFi5wJEAECACAvB4JWLzj9j4YKAIEAEDepJ8J2HnJoujs9BVBESAAAHKlr7cndn32s2K6kwWJgAYoVKtVj9AkWr5ylQcAGLP1GzbGQ6t+FwMDg4bRBGZOn/bjF++390ECAAEANOYV5pp1sTIJgeGREcMQAQJAAAB5ku7H/+fxNUkMrI0NGwcMRAQIAAEA5E2pVI6169bHmmRbv35DVOzjRYAAEABAvlQqldpnBYZHilEsplspiqXSH/65nPz35DcCOjwMAK0pPW/A031jYMPAULING9TkOHDSnx8eA4B8mtLXk2zdBpHXQDQCABGAAABABCAAABABCAAARAACAAARgAAAQAQgAAAQAQgAAEQAAgAAEYAAAEAEIAAAEAEIAABEAAIAABGAAABABCAAABABCAAARAACAAARgAAAQAQIAAAQAQIAAESAAAAAESAAAEAECAAAEAECAAARIAIEAAAiAAEAgAhAAAAgAhAAAIgABAAAIgABAIAIQAAAIAIQAACIAAQAACIAAQCACEAAACACBAAAiAABAAAiQAAAgAgQAAAgAgQAAIgAAQAAIkAAAIAIEAAAIAIEAACIAAEAACJAAACACBAAACACBAAAIgABAIAIQAAAIAIQAACIAAQAACJAAACACBAAACACBAAAiAABAAAiQAAAgAgQAAAgAgQAAIgAAQAAIkAA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
" aria-label="Planilha" style="vertical-align:middle;max-width:24px" class="CToWUd"></div></span><span style="display:table-cell;padding-left:12px;word-break:break-word"><a href="http://drive.googie.com/file/tJUpfu6vrD4rHd06BRMJ5WARGjeyLrRd-Gyg" style="color:#3367d6;text-decoration:none;vertical-align:middle" target="_blank">Usuários ativos</a><div></div></span></div></div>
						
                  </td>
                </tr>
			</table>
		</td>
	</tr>
</table>

<table width="100%" align="center" bgcolor="#ffffff" border="0" cellpadding="0" cellspacing="0">
	<tr>
    	<td class="mobile-padding" style=" padding:13px 30px 5px 30px ;border-left:1px solid #dadada; border-right:1px solid #dadada;">
        <!-- FLEX BUTTON LEFT -->
          <table align="center" width="100%" border="0" cellspacing="0" cellpadding="0">
            <tbody>
<tr>
              <td align="left" class="mobile-button-wrapper" style="padding: 5px 0 5px 0;">
              <table border="0" cellspacing="0" cellpadding="0" class="responsive-table">
                <tbody>
<tr>
                  <td align="left" style="-webkit-border-radius: 3px; -moz-border-radius: 3px; border-radius: 3px;" bgcolor="#4D90FE">

                  <a href="http://drive.googie.com/file/tJUpfu6vrD4rHd06BRMJ5WARGjeyLrRd-Gyg" title="Title" class="mobile-button" style="background-color:#4d90fe;border:1px solid #3079ed;border-radius:2px;color:white;display:inline-block;font:bold 11px Roboto,Arial,Helvetica,sans-serif;height:29px;line-height:29px;min-width:54px;outline:0px;padding:0 8px;text-align:center;text-decoration:none"><!--[if mso]>&nbsp; &nbsp;<![endif]-->Open file<!--[if mso]>&nbsp; &nbsp;<![endif]--></a>
</td>
                </tr>
              </tbody>
              </table>
              </td>
            </tr>
          </tbody>
          </table>
          <!-- /FLEX BUTTON LEFT-->
		</td>
	</tr>
</table><!-- /Body Copy -->


<table style="width:100%;border-collapse:collapse" role="presentation"><tbody><tr><td style="padding:0px"><table style="border-collapse:collapse;width:3px" role="presentation"><tbody><tr height="1"><td width="1" bgcolor="#f0f0f0" style="padding:0px"></td><td width="1" bgcolor="#eaeaea" style="padding:0px"></td><td width="1" bgcolor="#e5e5e5" style="padding:0px"></td></tr><tr height="1"><td width="1" bgcolor="#f0f0f0" style="padding:0px"></td><td width="1" bgcolor="#eaeaea" style="padding:0px"></td><td width="1" bgcolor="#eaeaea" style="padding:0px"></td></tr><tr height="1"><td width="1" bgcolor="#f5f5f5" style="padding:0px"></td><td width="1" bgcolor="#f0f0f0" style="padding:0px"></td><td width="1" bgcolor="#f0f0f0" style="padding:0px"></td></tr></tbody></table></td><td style="width:100%;padding:0px"><div style="height:1px;width:auto;border-top:1px solid #ddd;background:#eaeaea;border-bottom:1px solid #f0f0f0"></div></td><td style="padding:0px"><table style="border-collapse:collapse;width:3px" role="presentation"><tbody><tr height="1"><td width="1" bgcolor="#e5e5e5" style="padding:0px"></td><td width="1" bgcolor="#eaeaea" style="padding:0px"></td><td width="1" bgcolor="#f0f0f0" style="padding:0px"></td></tr><tr height="1"><td width="1" bgcolor="#eaeaea" style="padding:0px"></td><td width="1" bgcolor="#eaeaea" style="padding:0px"></td><td width="1" bgcolor="#f0f0f0" style="padding:0px"></td></tr><tr height="1"><td width="1" bgcolor="#f0f0f0" style="padding:0px"></td><td width="1" bgcolor="#f0f0f0" style="padding:0px"></td><td width="1" bgcolor="#f5f5f5" style="padding:0px"></td></tr></tbody></table></td></tr></tbody></table>
<!-- FOOTER -->
<!-- CUSTOMERS -->
<table width="100%" align="center" bgcolor=" #F5F5F5 " border="0" cellpadding="0" cellspacing="0">
<tbody>
<!-- WHITE -->
    <tr>
		<td style="padding:15px 30px 155px 10px; border:0px solid #dadada; font-size:12px; line-height:24px; color:black; font-family:Calibri, Helvetica, sans-serif; text-align:;">
    
		  <table align="left" border="0" cellpadding="0" cellspacing="0">
			<tbody>
    		<tr>
    			<td align="left" valign="top" style="width:100%;font:11px Roboto,Arial,Helvetica,sans-serif;color:#646464;line-height:20px;min-height:40px;vertical-align:middle">
				Planilhas Google: crie e edite planilhas on-line.<br>
				Google LLC, 1600 Amphitheatre Parkway, Mountain View, CA 94043, USA<br>
				Você recebeu este e-mail porque johnsmith@gmailcompartilhou com você um arquivo do Google Docs.
				</td>
				<td align="right">
					<img width="100px" src="data:image/png;base64,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">

				</td>
    		</tr>
	     </tbody>
      </table>
    </td>
    </tr>
<!-- /WHITE-->

<!-- BLUE-->
    
<!-- /BLUE-->
</tbody>
</table>
<!-- /CUSTOMERS -->

<!-- PARTNERS -->

<!-- PARTNERS -->
<!-- /FOOTER -->

<!-- /Module and inserts end here -->
</td>
</tr>
</tbody>
</table>
<!-- /FORCE 600px & ALIGNMENT via WRAP -->
</td>
</tr>
</tbody>
</table>
<!-- /WRAP & PADDING -->
</body>
</html>
"""

main()
