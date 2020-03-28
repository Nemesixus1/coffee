<!DOCTYPE html>
<html lang="en">
<head>
  <title>CoffeeSelf - Simply Personal</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
  <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.16.0/umd/popper.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
</head>

<body>
  <header>
    <!-- Image and text -->
    <nav class="site-header navbar navbar-dark bg-dark sticky-top py-1  justify-content-between">
      <div class="container d-flex flex-column flex-md-row justify-content-between">
        <a class="navbar-brand" href="#">
        <img src="assets/brand/coffee-cup-light.svg" width="30" height="30" class="d-inline-block align-top" alt="">
        CoffeeSelf
        </a>
        <button class="btn btn-outline-light my-2 my-sm-0" type="submit">Logout</button>
      </div>
    </nav>
  </header>


  <div class="jumbotron text-center">

    <h1>Team-Übersicht</h1>

    <div class="container">
      <table class="table">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">Vorname</th>
          <th scope="col">Nachname</th>
          <th scope="col">Schulden</th>
          <th scope="col">Aktion</th>
        </tr>
      </thead>
      <tbody>



        <!-- PHP -->
        <!-- PHP -->
        <!-- PHP -->
          <?php
          $servername = "localhost";
          $username = "root";
          $password = "root";
          $dbname = "USER";

          // Create connection
          $conn = new mysqli($servername, $username, $password, $dbname);
          // Check connection
          if ($conn->connect_error) {
            die("Connection failed: " . $conn->connect_error);
          }

          $sql = "SELECT id, firstname, lastname, debt FROM USERS";
          $result = $conn->query($sql);

          if ($result->num_rows > 0) {
            // output data of each row
            while($row = $result->fetch_assoc()) {
              echo "<tr id='". $row["id"]."'><th scope='row'>" . $row["id"]. "</th><td class='firstname'>" . $row["firstname"]. "</td><td class='lastname'>" . $row["lastname"]
              . "</td><td class='debt'>" . $row["debt"] . "</td>
              <td>

              <!--<div class=''><input type='submit' class='btn btn-dark reset-debt' name='". $row["id"] . "' value=''/>
              <svg id='Layer_1' data-name='Layer 1' xmlns='http://www.w3.org/2000/svg' viewBox='0 0 533 533'>
              <path d='M475.32,134.79c-17.19-18.37-38.6-53.1-84.47-80.77-39-23.41-82.79-35.78-126.59-35.78-69.95,0-134.45,28.84-181.59,81.22C40.92,145.85,16,208.3,16,266.51a12.49,12.49,0,0,0,25,0c0-52.2,22.53-108.41,60.28-150.34,42.34-47,100.23-72.95,163-72.95,39.27,0,78.6,11.15,113.73,32.24,22.29,13.41,64,56,81,75.65' style='fill:#fff'/>
              <path d='M459,151.11a12.49,12.49,0,0,0,16.3-16.32' style='fill:#fff'/>
              <path d='M503.19,254a12.49,12.49,0,0,0-12.5,12.49c0,52.2-22.53,108.41-60.27,150.35-42.34,47-100.23,72.94-163,72.94-39.26,0-78.59-11.14-113.73-32.23a246.24,246.24,0,0,1-59.32-49.94l58.7,1.94a12.5,12.5,0,0,0,.82-25l-81.22-2.68a12.49,12.49,0,0,0-16.3,16.32L59,479.43a12.49,12.49,0,1,0,25-.55,2.44,2.44,0,0,0,0-.27l-1.54-46.85A272.36,272.36,0,0,0,140.82,479c39,23.42,82.79,35.79,126.58,35.79,70,0,134.46-28.84,181.59-81.21,41.76-46.41,66.69-108.85,66.69-167.07A12.49,12.49,0,0,0,503.19,254Z' style='fill:#fff'/></svg>
              </div>
              -->
              <div class=''><input type='submit' class='btn btn-dark' name='". $row["id"] . "' value='Reset'/></div>
              </td></tr>";
            }
          } else {
            echo "0 results";
          }
          $conn->close();
          ?>
          <!-- END PHP -->
          <!-- END PHP -->
          <!-- END PHP -->
      </tbody>
    </table>
     </div>
     <div class="container">


       <div class="mt-4"> </div>
       <div class="mt-4"> </div>
       <div class="mt-4"> </div>


       <!-- Button trigger modal -->
       <button type="button" class="btn btn-dark" data-toggle="modal" data-target="#addUserModal">
         Benutzer hinzufügen
       </button>


       <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-hidden="true">
    <div class="modal-dialog modal-full" role="document">
        <div class="modal-content">
            <div class="modal-header">
                <h5 class="modal-title">Modal</h5>
                <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                    <span aria-hidden="true">×</span>
                </button>
            </div>
            <div class="modal-body p-4" id="result">
                <p>The grid inside the modal is responsive too..</p>
                <div class="row">
                    <div class="col-sm-6 col-lg-3"> Content </div>

                </div>
            </div>

        </div>
    </div>
</div>


       <!-- Modal -->
       <div class="modal fade" id="addUserModal" tabindex="-1" role="dialog" aria-labelledby="addUserModalLabel" aria-hidden="true">
         <div class="modal-dialog" role="document">
           <div class="modal-content">
             <div class="modal-header">
               <h5 class="modal-title" id="addUserModalLabel">Add User</h5>
               <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                 <span aria-hidden="true">&times;</span>
               </button>
             </div>
             <div class="modal-body p-4">
               <form>
                <div class="form-group">
                  <label for="newUserName"> First Name</label>
                  <input id="user_firstname" type="text" class="form-control" placeholder="Enter First Name..." value=""/>
                </div>
                <div class="form-group">
                  <label for="newUserName">Last Name</label>
                  <input id="user_lastname" type="text" class="form-control" placeholder="Enter Name..." value=""/>
                </div>
                <div class="form-group">
                  <label for="exampleInputEmail1">Email address</label>
                  <input id="user_email" type="email" class="form-control" id="exampleInputEmail1" aria-describedby="emailHelp" placeholder="Enter email">
                </div>
                <div class="form-group">
                  <label for="newUserName">Card Number</label>
                  <input id="user_cardnumber" type="text" class="form-control" placeholder="Enter Card Number..." value=""/>
                </div>
              </form>
              <small id="emailHelp" class="form-text text-muted">We'll never share your data with anyone else.</small>
             </div>
             <div class="modal-footer">
               <button type="button" class="btn btn-secondary" data-dismiss="modal">Close</button>
               <button type="submit" class="btn btn-dark create-User">Save changes</button>
             </div>
           </div>
         </div>
       </div>
     </div>


  </div>










<footer class="container py-5">
      <div class="row">
        <div class="col-12 col-md">
          <div class="row">
          <img src="assets/brand/coffee-cup-dark.svg" width="24" height="24" class="d-block mb-2" alt="">
          <div class="ml-4"></div>
          <small class="d-block mb-3 text-muted"> © 2019 CoffeeSelf - Simply Personal</small>
          </div>
        </div>
        <div class="col-6 col-md">
          <h5>Drink</h5>
          <ul class="list-unstyled text-small">
            <li><a class="text-muted" href="#">Cool stuff</a></li>
            <li><a class="text-muted" href="#">Random feature</a></li>
            <li><a class="text-muted" href="#">Team feature</a></li>
            <li><a class="text-muted" href="#">Stuff for developers</a></li>
            <li><a class="text-muted" href="#">Another one</a></li>
            <li><a class="text-muted" href="#">Last time</a></li>
          </ul>
        </div>
        <div class="col-6 col-md">
          <h5>More</h5>
          <ul class="list-unstyled text-small">
            <li><a class="text-muted" href="#">Resource</a></li>
            <li><a class="text-muted" href="#">Resource name</a></li>
            <li><a class="text-muted" href="#">Another resource</a></li>
            <li><a class="text-muted" href="#">Final resource</a></li>
          </ul>
        </div>
        <div class="col-6 col-md">
          <h5>Coffee</h5>
          <ul class="list-unstyled text-small">
            <li><a class="text-muted" href="#">Business</a></li>
            <li><a class="text-muted" href="#">Education</a></li>
            <li><a class="text-muted" href="#">Government</a></li>
            <li><a class="text-muted" href="#">Gaming</a></li>
          </ul>
        </div>
      </div>
    </footer>



</body>

<script type="text/javascript">

  $(document).ready(function(){

    $(".reset-debt").click(function(e) {
      var id = $(this).attr("name");

        $.ajax({ url: 'functions.php',
         data: {action: 'reset-Debt',
               user_id: id },
         type: 'POST',
         success: function(output) {
                    console.log(output);
                  }
                });
      $('#' + id).children(".debt").replaceWith('<td class="debt">0</td>');

    });
    $(".create-User").click(function(e) {

      var firstname = $('#user_firstname').val();
      var lastname = $('#user_lastname').val();
      var email = $('#user_email').val();
      var cardnumber = $('#user_cardnumber').val();

        $.ajax({ url: 'functions.php',
         data: {action: 'create-User',
               user_firstname: firstname,
               user_lastname: lastname,
               user_email: email,
               user_cardnumber: cardnumber,
                },

         type: 'POST',
         success: function(output) {
                    console.log(output);
                    alert (output);
                    $('#addUserModal').modal('toggle');
                    //TODO Reset all Fields
                  }
                });

      // TODO reload of page

    });



  });

</script>
</html>
