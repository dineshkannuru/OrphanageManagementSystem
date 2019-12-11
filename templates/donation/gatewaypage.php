{% extends 'userdashboard/basic.html' %}
{% load static %}
{% block content %}
<script>
        sidebar_shift("sidebar-donate")
</script>
      
      
    <div class="col-sm">
      <div class="p-3 mb-2 bg-light text-dark">
        <h4>Your order details:</h4>
        <table class="table">
  <tbody>
    <tr>
      <th scope="row">Transaction id :</th>
      <td>{{data.tid}}</td>
    </tr>
    <tr>
      <th scope="row">Name &emsp;&emsp;&emsp;&ensp;:</th>
      <td>{{user_name}}</td>
    </tr>
    <tr>
      <th scope="row">Orphanage&emsp;&nbsp;:</th>
      <td>{{orphanage}}</td>
    </tr>
    <tr>
      <td><div style="font-size:25px;padding:50px;"><table>
        <tr>
          
        </tr>
      </table>
        <h3>Mode of payment:</h3>
  <h2>Paypal</h2>
  {{ form.render }}</td>
  <td> <div style="font-size:25px;padding:50px;">Amount:{{data.amount}} $</div> </td>  
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