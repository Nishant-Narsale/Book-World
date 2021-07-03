console.log('manual javascript working');
console.log("USER:",user);
updateBtns = document.getElementsByClassName("update-cart");

for (let i = 0; i < updateBtns.length; i++) {
    updateBtns[i].addEventListener('click',function(){
        var productId = this.dataset.product;
        var action = this.dataset.action;

        console.log("Book Id:", productId,"Action:", action);
        
        if (user === "AnonymousUser"){
            console.log("User is not authenticated...");
            alert("For using Cart functionality You should Login... Please go to Login page..");
        }
        else{
            console.log("User is authenticated.. sending data....");
            updateUserCart(productId,action)
        }
    })
    
}

function updateUserCart(productId,action){
    var url = "/updateItem/";

    fetch (url,{
        method : 'POST',
        headers : {
            'content-type' : 'application/json',
            'X-CSRFToken' : csrftoken
        },
        body : JSON.stringify({'productId':productId,'action':action})
    })

    .then((response) => {
        return response.json()
    })

    .then((data) => {
        console.log('data:',data)
    })
}