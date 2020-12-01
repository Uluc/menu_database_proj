class item{
    constructor(section, name, price, id){
        this.section = section;
        this.name = name;
        this.price = price;
        this.id = id;
        this.servings = 1;
        this.totalPrice = price;
    }

    cartHtml(){
        var html = `<tr id=${this.id}>
                    <td>${this.name}</td>
                    <td>$${this.price}</td>
                    <td>
                        <select id=serving${this.id} name="servings" id="servings" class="servings" onchange="changeServing(${this.id})">
                            <option value="1">1</option>
                            <option value="2">2</option>
                            <option value="3">3</option>
                            <option value="4">4</option>
                            <option value="5">5</option>
                            <option value="6">6</option>
                            <option value="7">7</option>
                            <option value="8">8</option>
                        </select>
                    </td>
                    <td id=total${this.id}>$${this.totalPrice}</td>
                    <td style="width: 1rem;">
                        <div class="btn btn-warning" onclick="return this.parentNode.parentNode.remove();"> Remove</div>
                    </td>
                </tr>`

        return html;
    }

}

function cartCosts(){
    var sum = 0;
    for (var i = 0; i < cart.length; i++) {
        sum+= Number(cart[i].totalPrice);
    }
    console.log(sum);
    $('#subTotal').html('$' + sum);
    $('#tax').html('$' + sum*.1);

}

function changeServing(id){
    var obj;
    for(var i = 0; i< cart.length; i++){
        if(cart[i].id == id){
            obj = cart[i];
            console.log(obj)
            obj.servings = document.getElementById(`serving${obj.id}`).value;
            obj.totalPrice = obj.price * obj.servings;
            console.log(obj)
            $(`#total${obj.id}`).html('$'+obj.totalPrice)
            break;
        }
    }
    cartCosts()
}

var cart = []
function addToCart(section, name, price, id){
    cart.push(new item(section, name, price, id))
}



(function($){
    $("#cartButton").click(function(){
        var html = "";
        for(var i = 0; i < cart.length; i++){
            html += cart[i].cartHtml();
        }
        $("#cartBody").html(html)
        cartCosts()
    })

})(jQuery)


