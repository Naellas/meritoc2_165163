<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simple Store with Checkout</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <h1 class="storeheader">Welcome to Our Simple Store</h1>
    <div class="container">
        <div class="gallery">
            <?php
                // Połączenie z bazą danych MySQL na Azure
                $host = 'storedbserv.database.windows.net';
                $username = 'maciejczaplicki';
                $password = 'Claptrap10293847!@#';
                $dbname = 'oursimplestore-database';

                // Utworzenie połączenia
                $conn = new mysqli($host, $username, $password, $dbname);

                // Sprawdzenie połączenia
                if ($conn->connect_error) {
                    die("Connection failed: " . $conn->connect_error);
                }

                // Pobranie produktów z bazy danych
                $sql = "SELECT * FROM products";
                $result = $conn->query($sql);

                if ($result->num_rows > 0) {
                    // Wyświetlenie każdego produktu
                    while($row = $result->fetch_assoc()) {
                        echo '<div class="product">';
                        echo '<img src="' . $row['image_url'] . '" alt="' . $row['name'] . '">';
                        echo '<h2>' . $row['name'] . '</h2>';
                        echo '<p>' . $row['description'] . '</p>';
                        echo '<p>Price: $' . $row['price'] . '</p>';
                        echo '<button onclick="addToCart(\'' . $row['name'] . '\', ' . $row['price'] . ')">Add to Cart</button>';
                        echo '</div>';
                    }
                } else {
                    echo "0 results";
                }

                $conn->close();
            ?>
        </div>

        <aside class="sidebar">
            <div class="login-section">
                <h2>Login</h2>
                <label for="login-email">Email:</label>
                <input type="email" id="login-email" name="login-email">
                <label for="login-password">Password:</label>
                <input type="password" id="login-password" name="login-password">
                <button onclick="login()">Login</button>
            </div>        

            <div class="cart">
                <h2>Shopping Cart</h2>
                <ul id="cart-items">
                    <!-- Dynamic cart items will be added here -->
                </ul>
                <p>Total: <span id="cart-total">$0.00</span></p>
                <label for="email">Email:</label>
                <input type="email" id="email" name="email">
                <button class="checkout-btn" onclick="checkout()">Checkout</button>
            </div>
        </aside>
    </div>
    
    <script>
        let cartItems = [];
        let total = 0;

        function addToCart(productName, price) {
            // Sprawdź, czy przedmiot już istnieje w koszyku
            const existingItem = cartItems.find(item => item.name === productName);

            if (existingItem) {
                // Jeśli przedmiot już istnieje, zwiększ jego liczbę
                existingItem.quantity++;
                existingItem.totalPrice += price;
            } else {
                // Jeśli przedmiotu nie ma w koszyku, dodaj nowy
                cartItems.push({ name: productName, price: price, quantity: 1, totalPrice: price });
            }

            total += price;
            updateCart();
        }

        function updateCart() {
            const cartList = document.getElementById('cart-items');
            cartList.innerHTML = '';
            
            cartItems.forEach(item => {
                const li = document.createElement('li');
                li.textContent = `${item.name} (Quantity: ${item.quantity}) - $${item.totalPrice.toFixed(2)}`;
                cartList.appendChild(li);
            });
            
            document.getElementById('cart-total').textContent = `$${total.toFixed(2)}`;
        }

        function checkout() {
            const email = document.getElementById('email').value;

            if (cartItems.length === 0) {
                alert('Your cart is empty. Please add some items.');
            } else if (!email) {
                alert('Please enter your email address.');
            } else {
                const xhttp = new XMLHttpRequest();
                const params = `email=${email}&total=${total}&cartItems=${JSON.stringify(cartItems)}`; // Include cartItems as JSON string

                xhttp.onreadystatechange = function() {
                    if (this.readyState === 4 && this.status === 200) {
                        alert('Order placed successfully! Redirecting to checkout page...');
                        // Add redirect logic here if needed
                    }
                };

                xhttp.open("POST", "process_order.php", true);
                xhttp.setRequestHeader("Content-type", "application/x-www-form-urlencoded");
                xhttp.send(params);
            }
        }   
        
        function previewOrder() {
            const previewEmail = document.getElementById('preview-email').value;

            if (!previewEmail) {
                alert('Please enter your email address.');
                return;
            }

            const xhttp = new XMLHttpRequest();
            const params = `email=${previewEmail}`;

            xhttp.onreadystatechange = function() {
                if (this.readyState === 4 && this.status === 200) {
                    document.getElementById('order-details').innerHTML = this.responseText;
                }
            };

            xhttp.open("GET", `preview_order.php?${params}`, true);
            xhttp.send();
        }
    </script>
</body>
</html>
