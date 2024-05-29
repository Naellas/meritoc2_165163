<?php
// Odbierz email z parametrów URL
$previewEmail = $_GET['email'];

// Połączenie z bazą danych
$database_path = "C:\Users\amaci\Desktop\Database1.accdb";
$conn = new COM("ADODB.Connection");

try {
    $conn->Open("Provider=Microsoft.ACE.OLEDB.12.0;Data Source=$database_path");

    // Zapytanie o szczegóły zamówień dla danego emaila
    $sql = "SELECT * FROM orders WHERE email = '$previewEmail'";
    $result = $conn->Execute($sql);

    if (!$result->EOF) {
        // Wyświetlanie szczegółów zamówień
        echo "<h3>Order Details for $previewEmail:</h3>";
        echo "<ul>";
        while (!$result->EOF) {
            $orderId = $result->Fields("order_id")->Value;
            $total = $result->Fields("total")->Value;
            echo "<li>Order ID: $orderId, Total: $total</li>";
            // Możesz dodać więcej szczegółów zamówienia tutaj
            $result->MoveNext();
        }
        echo "</ul>";
    } else {
        echo "No orders found for $previewEmail.";
    }

    $result->Close();
    $conn->Close();
} catch (com_exception $e) {
    echo "Error: " . $e->getMessage();
}
?>