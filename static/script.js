console.log('JS is running')


window.onload = async function getCupcakeInfo() {
    let response = await axios.get("/api/cupcakes");
    console.log("got:", response.data);
    
    let cupcake_data = response.data;
    
    body_tag = document.getElementById('body')
    console.log('the_cupcakes.cupcakes[0].flavor', cupcake_data.cupcakes[0].flavor);
    for (let cake of cupcake_data.cupcakes){
        let row = `<tr><td>${cake.flavor}</td><td>${cake.size}</td><td>${cake.rating}</td><td><img src=${cake.image} width=100px></td>`
        body_tag.innerHTML = body_tag.innerHTML + row;
    }
    return cupcake_data }

// let the_cupcakes = getCupcakeInfo();

button = document.getElementById("btn_new_cupcake")
button.addEventListener('click', (evt) => {
    evt.preventDefault();
    get_new_cupcake_data();
}) // End addEventListener



async function send_data(new_cupcake) {
    await axios.post("/api/cupcakes", new_cupcake, {
        headers: {
            'Content-Type': 'application/json' // Needed for the post query
          }
    })
  .then(response => {
    console.log(response.data); // Handle successful response
    window.location.href = '/';
    })
  .catch(error => {
    console.error(error); // Handle error
  });
}

function get_new_cupcake_data() {
    form_content = document.getElementById('form_new_cupcake');
        const new_cupcake = {};
        new_cupcake.flavor = $('#flavor').val();
        new_cupcake.size = $('#size').val();
        new_cupcake.rating = $('#rating').val();
        new_cupcake.image = $('#image').val();
        const new_cupcake_JSON = JSON.stringify(new_cupcake);
        console.log('NEW CUPCAKE:', new_cupcake_JSON);
        send_data(new_cupcake_JSON);
    }  // END get_data()
