<?php
// Odbierz dane z formularza
$email = $_POST['email'];
$total = $_POST['total'];
$cartItems = json_decode($_POST['cartItems'], true); // Decode cartItems JSON

// Połączenie z bazą danych
$database_path = "C:\\Users\\amaci\\Desktop\\Database1.accdb"; // Double backslashes for file path
$conn = new COM("ADODB.Connection");

try {
    $conn->Open("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=$database_path");

    // Dodanie nowego wpisu do tabeli orders
    $sql = "INSERT INTO orders (email, total) VALUES ('$email', $total)";
    $conn->Execute($sql);

    // Pobierz identyfikator ostatniego dodanego zamówienia
    $result = $conn->Execute("SELECT MAX(order_id) AS last_id FROM orders");
    $orderId = $result->Fields('last_id')->Value;

    // Dodanie szczegółów koszyka do tabeli order_items
    foreach ($cartItems as $item) {
        $productName = $item['name'];
        $price = $item['price'];
        $quantity = $item['quantity'];
    
        // Debugging output (commented out to avoid unexpected output)
        // echo "Inserting: $productName, $price, $quantity into order_id: $orderId";
    
        $sqlItems = "INSERT INTO order_items (order_id, product_name, price, quantity) VALUES ($orderId, '$productName', $price, $quantity)";
        $conn->Execute($sqlItems);
    }

    echo "Order placed successfully!";
} catch (com_exception $e) {
    echo "Error: " . $e->getMessage();
}

// Zamknięcie połączenia
$conn->Close();
?>