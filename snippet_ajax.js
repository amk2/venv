$("#delete_student").click(function(){
    $.ajax({
      type: 'POST',
      url: "/_delete_student",
      data: {student_id: 1},
      dataType: "text",
      success: function(data){
                 alert("Deleted Student ID "+ student_id.toString());
               }
    });
});
