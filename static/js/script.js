// document.addEventListener('DOMContentLoaded', function () {
//     const buttons = document.querySelectorAll('.filter-btn');
//     const products = document.querySelectorAll('.product');

//         buttons.forEach(button => {
//             button.addEventListener('click', () => {
//                 const filter = button.getAttribute('data-filter');
                
//                 products.forEach(product => {
//                     product.style.display = 'none';
//                 });

//                 if (filter === 'all') {
//                     products.forEach(product => {
//                         product.style.display = 'block';
//                     });
//                 } else {
//                     const filteredProducts = document.querySelectorAll(`.${filter}`);
//                     filteredProducts.forEach(product => {
//                         product.style.display = 'block';
//                     });
//                 }
//             });
//         });
//     });

