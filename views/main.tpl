%include header title='index@ ',version='(Bottle版)'

<div class="panel panel-default">
  <div class="panel-heading">
    <h3 class="panel-title">DAMA::用goo.gl缩址</h4>
  </div>
  <div class="panel-body">

<form class="navbar-form navbar-left" role="search"
    action="/goo" 
    method="post"  
    enctype="multipart/form-data">
<div class="input-group input-group-lg">

  <span class="input-group-addon">URI:</span>
  <input type="text" class="form-control" placeholder="网址"
        id="uri"
        name="uri">
</div>
  <button type="submit" class="btn btn-primary btn-lg">缩之</button>
</form>

  </div>
</div>



%include footer

