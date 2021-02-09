<?php

$username = $_REQUEST['username'];
$password = $_REQUEST['password'];

$mysqli = new mysqli('localhost','erp','passworderp', 'erp');

if ($mysqli -> connect_errno) {
  echo "Failed to connect to MySQL: " . $mysqli -> connect_error;
  exit();
}

$sql = "SELECT * FROM users WHERE username = \"" .  $username . "\" AND password = \"" . $password . "\"";
$result = $mysqli -> query($sql);

$AuthResult = "";
$redirURL   = "";


if($result && $result->num_rows == 0){

	$AuthResult = "Wrong Credentias";
	$redirURL = "login.php?error";

} else {

	session_start();
	$AuthResult = "LOGIN OK";
	$redirURL = "index.php";
	$_SESSION['username'] = "Admin";
}

if ( $_REQUEST['debug'] == "on" || $_REQUEST['DEBUG'] == "on" ) {

	print "<br><br> DEBUG </br><br>";
	print var_dump($result);

	print($AuthResult);
	print "<br>Rows:" . $result -> num_rows;
	print "<Br><Br>" . $sql . "<br><br> <b>Query Result:</b> <br><br>";

	while ($row = $result->fetch_assoc()) {
		echo $row['username'] . " - " . $row['password'] . "<br>";
	}

	die();

} else {
	$mysqli -> close();
	header("Location:" . $redirURL);
}
