#!/usr/bin/env python3
print("Content-Type: text/html \n")
print("""
<!DOCTYPE html>
<html>
<head>
<title>HTML SignUp Form</title>
</head>
<body bgcolor="lightyellow">
<h1><center>Game.Net</center></h1>
    <fieldset style='width:800px; height:320px; margin:auto; border-color: yellow'> 
    <legend align='right'> Main page</legend>
    <table style='width:790px; height:310px; margin:auto;' bgcolor=lightblue>       
        <tr align="center">           
            <td>
                <form>
                    <p>If you have not signed up click here!</p>
                    <button type="submit" formaction="http://workshop.sps.nyu.edu/~ba2500/python/Final%20Project/signin_page.py">Sign up</button>
                </form>
            </td>
        </tr>
    </table>
</body>
""")
