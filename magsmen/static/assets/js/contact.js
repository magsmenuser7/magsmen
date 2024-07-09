// contact form 
$(document).on('submit', '#contactform', function(event){
    event.preventDefault();
     let name= $('#name').val()
     let email = $('#email').val()
     let phone =$('#phone').val()
     let subject = $('#subject').val()
     let message = $('#message').val()
     csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()
     
     let data = new FormData();
     data.append("name", name);
     data.append("email",email);
     data.append("phone",phone);
     data.append("subject",subject);
     data.append("message",message);
     data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)
     
   
   
     $.ajax({
           url:"/reach-us-out/",
           method: 'Post',
           processData:false,
           contentType:false,
           cache:false,
           mimeType:"multipart/form-data",
           data:data,
           
           success:function(data){
               $('#contactform')[0].reset();
               alert("sucessfully sending message")
            //    $('.returnmessage').append("Your message has been received, We will contact you soon.")
           },
           error:function(data){
            alert("Your message has been faild, please try agian.")
            //    $('.returnmessage').append("Your message has been faild, please try agian.")
           }
       })

})
    


$(document).ready(function(){
    $('#applybtn').click(function(){
        let name = $('#name').val()
        let email = $('#email').val()
        let phonenumber = $('#phonenumber').val()
        let selectcategory = $('#selectcategory').val()
        let location = $('#location').val()
        let file = $('#uploadfile')[0].files[0];
        let csrfmiddlewaretoken = $('input[name=csrfmiddlewaretoken]').val()

        if (name === '') {
            alert('Name field required');
            return; // Stop execution if validation fails
        }
        if (email === '') {
            alert('Email field required');
            return; // Stop execution if validation fails
        }
        if (!isValidEmail(email)) {
            alert('Invalid email format');
            return; // Stop execution if validation fails
        }
        if (phonenumber === '') {
            alert('Phone number required');
            return; // Stop execution if validation fails
        }
        if (!isValidPhone(phonenumber)) {
            alert('Invalid phone number format');
            return; // Stop execution if validation fails
        }
        if (selectcategory === 'select'){
            alert("Category field required")
            return;
        }
        if (location === 'location'){
            alert("Location field required")
            return;
        }
        if (!file){
            alert('Please upload a file');
            return;
        }


        // SubmitEvent()

        let data = new FormData();
        data.append("name", name),
        data.append("email",email),
        data.append("phonenumber",phonenumber),
        data.append("selectcategory",selectcategory),
        data.append("location",location),
        data.append("file",file),
        data.append('csrfmiddlewaretoken',csrfmiddlewaretoken)

        $.ajax({
            url:"/applyform/",
            method: 'POST',
            processData:false,
            contentType:false,
            cache:false,
            data:data,
            success:function(data, status,xhr){
                $('#apply-form')[0].reset();
                if(data.success === true){
                    alert("Job Form Applied success")
                    window.location.href ='/';
                }else{
                    alert(data.error)
                    window.location.href = '/applyform/'
                }
            },
            error:function(data){
                alert("fail, submitted data")
            }
            
        })
    
    });
});

function isValidEmail(email) {
    let emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailRegex.test(email);
}

function isValidPhone(phonenumber) {
    let phoneRegex = /^\d{10}$/;
    return phoneRegex.test(phonenumber);
}