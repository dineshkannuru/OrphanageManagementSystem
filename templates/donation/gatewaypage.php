{% extends 'userdashboard/basic.html' %}
{% load static %}
{% block content %}
<script>
        sidebar_shift("sidebar-donate")
</script>
<div class="col-6">
  <div class="card">
  <div class="card-header">
    <center><h4>Donation details</h4><center>
  </div>
  <div class="card-body">
    <div class='container'>
      <div class='row'>
        <div class='column'>
      <div >
    
        <table class="table">
  <tbody>
    <tr>
      <th scope="row">Transaction id :</th>
      <td>{{data.tid}}</td>
    </tr>
    <tr>
      <th scope="row">Name &emsp;&emsp;&emsp;:</th>
      <td>{{user_name}}</td>
    </tr>
    <tr>
      <th scope="row">Orphanage&emsp;&nbsp;:</th>
      <td>{{orphanage}}</td>
    </tr>
    <tr>
      <td><div style="font-size:25px;padding:40px;"><table>
        <tr>
          
        </tr>
      </table>
  
  <h2>&emsp;Paypal</h2>
  {{ form.render }}</td>
  <td> <div style="font-size:25px;padding:25px;margin-top:20px;">Amount:{{data.amount}} $</div> </td>  
  </tr>
  
  </div>
  </tbody>
</table>
  </div>
    </div>
          
      </div>
      </div>
</div>
        
            <!-- content ends here-->
{% endblock content %}