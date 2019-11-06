function add_to_cart(item_id){
    let quantity = $(`#quantity_${item_id}`).val()
    console.log(quantity)
    console.log(item_id)
    var json_data = {}
    json_data["quantity"] = quantity
    json_data["item_id"] = item_id
    json_data["csrfmiddlewaretoken"] = $('[name="csrfmiddlewaretoken"]').val();
    
    $.ajax({
        url:"/add_to_cart/",
        method:"POST",
        type:"application/json",
        data:json_data,
        success: function(response){
            console.log(response)
            alert(response.message)
        }
    })
}