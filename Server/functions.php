<?php
  if (isset($_POST['action'])) {

        switch ($_POST['action']) {

            case 'reset-Debt':
                $current_id = isset($_POST['user_id']) ? $_POST['user_id'] : null;
                resetDebt($current_id);
                break;

            case 'create-User':

                 $userFirstname = isset($_POST['user_firstname']) ? $_POST['user_firstname'] : null;
                 $userLastname = isset($_POST['user_lastname']) ? $_POST['user_lastname'] : null;
                 $userEmail = isset($_POST['user_email']) ? $_POST['user_email'] : null;
                 $userCardnumber = isset($_POST['user_cardnumber']) ? $_POST['user_cardnumber'] : null;



                createUser($userFirstname, $userLastname, $userEmail, $userCardnumber);
                break;

        }
    }

    function resetDebt($id) {
      $servername = "localhost";
      $username = "root";
      $password = "root";
      $dbname = "USER";
      //TODO $table= "USERS"

      // Create connection
      $conn = new mysqli($servername, $username, $password, $dbname);
      // Check connection
      if ($conn->connect_error) {
          die("Connection failed: " . $conn->connect_error);
      }

      $sql = "UPDATE USERS SET debt='0' WHERE id=$id";

      if ($conn->query($sql) === TRUE) {
          echo "Record updated successfully";
      } else {
          echo "Error updating record: " . $conn->error;
      }

      $conn->close();
      exit;

    }


    function createUser($firstname, $lastname, $email, $cardnumber) {
      $servername = "localhost";
      $username = "root";
      $password = "root";
      $dbname = "USER";

      //TODO Insert Card Number


      // Create connection
      $conn = new mysqli($servername, $username, $password, $dbname);
      // Check connection
      if ($conn->connect_error) {
          die("Connection failed: " . $conn->connect_error);
      }

      $sql = "INSERT INTO USERS (firstName, lastName, email)
              VALUES ( '$firstname', '$lastname', '$email')";

      if ($conn->query($sql) === TRUE) {
          echo "User inserted successfully";
      } else {
          echo "Error: User couldn't be added " . $conn->error;
      }

      $conn->close();
      exit;

    }



?>
