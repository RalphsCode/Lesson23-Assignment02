console.log('JS is running')



async function getCupcakeInfo() {
    let response = await axios.get("/api/cupcakes");
    console.log("got:", response.data);
    console.log("flavor in function", response.data.cupcakes[0].flavor);
    let cupcake_data = response.data;
    
    body_tag = document.getElementById('body')
    console.log('the_cupcakes.cupcakes[0].flavor', cupcake_data.cupcakes[0].flavor);
    for (let cake of cupcake_data.cupcakes){
        let row = `<tr><td>${cake.flavor}</td><td>${cake.size}</td><td>${cake.rating}</td><td><img src=${cake.image} width=100px></td>`
        body_tag.innerHTML = body_tag.innerHTML + row;
    }
    

    return cupcake_data }

// window.addEventListener('load', getCupcakeInfo())


let the_cupcakes = getCupcakeInfo();
