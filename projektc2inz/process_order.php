<?php
// Odbierz dane z formularza
$email = $_POST['email'];
$total = $_POST['total'];
$cartItems = json_decode($_POST['cartItems'], true); // Decode cartItems JSON

// Połączenie z bazą danych PostgreSQL
$host = 'storedb.postgres.database.azure.com';
$port = '5432';
$dbname = 'postgres';
$user = 'auodswsanl';
$password = 'your_password';

$conn = pg_connect("host=$host port=$port dbname=$dbname user=$user password=$password");

if (!$conn) {
    echo "An error occurred.\n";
    exit;
}

try {
    // Rozpoczęcie transakcji
    pg_query($conn, "BEGIN");

    // Dodanie nowego wpisu do tabeli orders
    $sql = "INSERT INTO orders (email, total) VALUES ('$email', $total) RETURNING order_id";
    $result = pg_query($conn, $sql);
    
    if ($result) {
        $row = pg_fetch_assoc($result);
        $orderId = $row['order_id'];
    
        // Dodanie szczegółów koszyka do tabeli order_items
        foreach ($cartItems as $item) {
            $productName = pg_escape_string($item['name']);
            $price = $item['price'];
            $quantity = $item['quantity'];

            $sqlItems = "INSERT INTO order_items (order_id, product_name, price, quantity) VALUES ($orderId, '$productName', $price, $quantity)";
            $resultItems = pg_query($conn, $sqlItems);

            if (!$resultItems) {
                throw new Exception("Error inserting order items.");
            }
        }
        
        // Zakończenie transakcji
        pg_query($conn, "COMMIT");

        echo "Order placed successfully!";
    } else {
        throw new Exception("Error inserting order.");
    }
} catch (Exception $e) {
    // Wycofanie transakcji w przypadku błędu
    pg_query($conn, "ROLLBACK");
    
    echo "Error: " . $e->getMessage();
}

// Zamknięcie połączenia
pg_close($conn);
?>