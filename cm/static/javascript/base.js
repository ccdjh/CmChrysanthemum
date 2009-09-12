  $(document).ready(function(){
    $("#commentForm").validate();
    $("#oneForm").validate();
    $("#aboutForm").validate();
    $("#listFrom").validate();
    $(".listFromTwo").rules("add", {
      required: true,
      minlength: 2
    });
    $("#adminForm").validate();
  });
