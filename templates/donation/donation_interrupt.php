{% extends 'userdashboard/basic.html' %}
{% load static %}
{% block content %}

<script async defer crossorigin="anonymous" src="https://connect.facebook.net/en_US/sdk.js#xfbml=1&version=v5.0&appId=790224518079845&autoLogAppEvents=1"></script>
  <div class="modal fade" id="myModal">
    <div class="modal-dialog modal-dialog-centered">
      <div class="modal-content">
      
        <!-- Modal Header -->
        <div class="modal-header">
          <h3 style="text-align:center">Donation Interrupted</h3>
            <button type="button" class="close" data-dismiss="modal">&times;</button>
       </div>
<!-- Modal body -->
      <div class="modal-body">
        <h4 style="text-align:center">Share us with your friends</h4>
      
          
        </div>
        <div>
        <a href="{% url 'userdashboard:u_Profile' %}">Go to home</a>
          <div class="fb-share-button" data-href="http://127.0.0.1:8000/" style="float: right;" data-layout="button" data-size="large"><a target="_blank" href="https://www.facebook.com/sharer/sharer.php?u=http%3A%2F%2F127.0.0.1%3A8000%2F&amp;src=sdkpreparse" class="fb-xfbml-parse-ignore">Share us with your friends</a>
        </div>
        </div>
      </div>
    </div>
  </div>
  
</div>


<script>
$(document).ready(function(){
  // Show the Modal on load
  $("#myModal").modal("show");
    
  // Hide the Modal
  $("#myBtn").click(function(){
    $("#myModal").modal("hide");
  });
});
</script>

{% endblock content %}