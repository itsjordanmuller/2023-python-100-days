document.addEventListener('DOMContentLoaded', function() {
  const categoryButtons = document.querySelectorAll('.category-button');

  categoryButtons.forEach(button => {
    button.addEventListener('click', function() {
      const category = this.getAttribute('data-category');
      fetchCategoryProducts(category);
    });
  });
});

function fetchCategoryProducts(category) {
  fetch(`https://fakestoreapi.com/products/category/${category}`)
    .then(response => response.json())
    .then(products => updateProductGrid(products))
    .catch(error => console.error('Error:', error));
}

function updateProductGrid(products) {
  const productGrid = document.querySelector('.product-grid');
  productGrid.innerHTML = ''; // Clear current products

  products.forEach(product => {
    // Create and append new product elements
    const productCard = `<div class="product-card">
      <img src="${product.image}" alt="${product.title}" class="product-image"/>
      <div class="product-info">
        <h3 class="product-title">${product.title}</h3>
        <p class="product-price">$${product.price}</p>
        <p class="product-category">${product.category}</p>
        <p class="product-description">${product.description}</p>
        <div class="product-rating">
          <span>Rating: ${product.rating.rate}</span>
          <span>(${product.rating.count} reviews)</span>
        </div>
        <a href="/product/${product.id}" class="product-detail-button">View Details</a>
      </div>
    </div>`;
    productGrid.innerHTML += productCard;
  });
}
