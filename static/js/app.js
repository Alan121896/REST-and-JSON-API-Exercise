// $(document).ready(function () {
//     // Function to get cupcakes from the API and update the list on the page
//     function updateCupcakeList() {
//       axios.get('/api/cupcakes')
//         .then(response => {
//           const cupcakes = response.data.cupcakes;
//           const cupcakeList = $('#cupcake-list');
//           cupcakeList.empty();
  
//           cupcakes.forEach(cupcake => {
//             const cupcakeItem = `
//               <li>
//                 <strong>${cupcake.flavor}</strong> - ${cupcake.size} - Rating: ${cupcake.rating}
//                 <img src="${cupcake.image}" alt="${cupcake.flavor}" width="100">
//               </li>
//             `;
//             cupcakeList.append(cupcakeItem);
//           });
//         })
//         .catch(error => console.error(error));
//     }
  
//     // Call the updateCupcakeList function on page load
//     updateCupcakeList();
  
//     // Handle form submission to add a new cupcake
//     $('#cupcake-form').submit(function (event) {
//       event.preventDefault();
  
//       const flavor = $('#flavor').val();
//       const size = $('#size').val();
//       const rating = parseFloat($('#rating').val());
//       const image = $('#image').val();
  
//       axios.post('/api/cupcakes', { flavor, size, rating, image })
//         .then(response => {
//           console.log('Cupcake added:', response.data.cupcake);
//           // Clear form fields after successful submission
//           $('#flavor').val('');
//           $('#size').val('');
//           $('#rating').val('');
//           $('#image').val('');
  
//           // Update the cupcake list to show the newly added cupcake
//           updateCupcakeList();
//         })
//         .catch(error => console.error(error));
//     });
//   });




//   const BASE_URL = "http://localhost:5000/api";


// /** given data about a cupcake, generate html */

// function generateCupcakeHTML(cupcake) {
//   return `
//     <div data-cupcake-id=${cupcake.id}>
//       <li>
//         ${cupcake.flavor} / ${cupcake.size} / ${cupcake.rating}
//         <button class="delete-button">X</button>
//       </li>
//       <img class="Cupcake-img"
//             src="${cupcake.image}"
//             alt="(no image provided)">
//     </div>
//   `;
// }


// /** put initial cupcakes on page. */

// async function showInitialCupcakes() {
//   const response = await axios.get(`${BASE_URL}/cupcakes`);

//   for (let cupcakeData of response.data.cupcakes) {
//     let newCupcake = $(generateCupcakeHTML(cupcakeData));
//     $("#cupcakes-list").append(newCupcake);
//   }
// }


/** handle form for adding of new cupcakes */

$("#new-cupcake-form").on("submit", async function (evt) {
  evt.preventDefault();

  let flavor = $("#form-flavor").val();
  let rating = $("#form-rating").val();
  let size = $("#form-size").val();
  let image = $("#form-image").val();

  const newCupcakeResponse = await axios.post(`${BASE_URL}/cupcakes`, {
    flavor,
    rating,
    size,
    image
  });

  let newCupcake = $(generateCupcakeHTML(newCupcakeResponse.data.cupcake));
  $("#cupcakes-list").append(newCupcake);
  $("#new-cupcake-form").trigger("reset");
});


/** handle clicking delete: delete cupcake */

$("#cupcakes-list").on("click", ".delete-button", async function (evt) {
  evt.preventDefault();
  let $cupcake = $(evt.target).closest("div");
  let cupcakeId = $cupcake.attr("data-cupcake-id");

  await axios.delete(`${BASE_URL}/cupcakes/${cupcakeId}`);
  $cupcake.remove();
});


$(showInitialCupcakes);