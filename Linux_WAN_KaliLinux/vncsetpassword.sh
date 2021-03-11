#!/usr/bin/expect -f
spawn tightvncserver
expect "Password:"
send "{DEFAULTPASSWORD}\r"
expect "Verify"
send "{DEFAULTPASSWORD}\r"
expect "Would"
send -- "n\r"
expect eof
