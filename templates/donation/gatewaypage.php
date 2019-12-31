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
    
        <table class="table" style="border-collapse: collapse; border: none;">
  <tbody>
    <tr style="border: none;">
      <th scope="row" style="border: none;">Transaction id :</th>
      <td style="border: none;">{{data.tid}}</td>
    </tr>
    <tr style="border: none;">
      <th scope="row" style="border: none;">Name &emsp;&emsp;&emsp;:</th>
      <td>{{user_name}}</td>
    </tr>
    <tr >
      <th scope="row" style="border: none;">Orphanage&emsp;&nbsp;:</th>
      <td>{{orphanage}}</td>
    </tr>
    <tr style="border: none;">
      <td style="border: none;"><div style="font-size:25px;padding:40px;"><table>
        <tr>
          
        </tr>
      </table>
  
  <h2>&emsp;Paypal</h2>
  {{ form.render }}</td>
  <td style="border: none;"> <div style="font-size:25px;padding:25px;margin-top:20px;">Amount:{{data.amount}} $</div> </td>  
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