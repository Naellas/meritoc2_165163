<?php
// Odbierz dane z formularza
$email = $_POST['email'];
$total = $_POST['total'];
$cartItems = json_decode($_POST['cartItems'], true); // Decode cartItems JSON

// Połączenie z bazą danych MySQL na Azure
                $host = 'simplestoredatabase.mysql.database.azure.com';
                $username = 'maciejczaplicki';
                $password = 'Claptrap10293847!';
                $dbname = 'oursimplestore-database';

// Utworzenie połączenia
$conn = new mysqli($host, $username, $password, $dbname);

// Sprawdzenie połączenia
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

try {
    // Rozpoczęcie transakcji
    $conn->begin_transaction();

    // Dodanie nowego wpisu do tabeli orders
    $sql = "INSERT INTO orders (email, total) VALUES ('$email', $total)";
    $conn->query($sql);

    // Pobranie identyfikatora ostatnio dodanego zamówienia
    $orderId = $conn->insert_id;

    // Dodanie szczegółów koszyka do tabeli order_items
    foreach ($cartItems as $item) {
        $productName = $conn->real_escape_string($item['name']);
        $price = $item['price'];
        $quantity = $item['quantity'];

        $sqlItems = "INSERT INTO order_items (order_id, product_name, price, quantity) VALUES ($orderId, '$productName', $price, $quantity)";
        $conn->query($sqlItems);

        if (!$conn->affected_rows) {
            throw new Exception("Error inserting order items.");
        }
    }

    // Zakończenie transakcji
    $conn->commit();

    echo "Order placed successfully!";
} catch (Exception $e) {
    // Wycofanie transakcji w przypadku błędu
    $conn->rollback();
    
    echo "Error: " . $e->getMessage();
}

// Zamknięcie połączenia
$conn->close();
?>