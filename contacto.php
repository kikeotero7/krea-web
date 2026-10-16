<?php
// Formulario de auditoría IA · KREA Digital Studio
header('Content-Type: application/json; charset=utf-8');
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo json_encode(['ok'=>false]); exit; }
if (!empty($_POST['web'])) { echo json_encode(['ok'=>true]); exit; } // trampa antispam

function campo($k, $max = 2000) {
  $v = isset($_POST[$k]) ? trim((string)$_POST[$k]) : '';
  $v = str_replace(["\r", "\0"], '', $v);
  return mb_substr($v, 0, $max);
}
$nombre   = campo('nombre', 120);
$email    = campo('email', 160);
$negocio  = campo('negocio', 160);
$telefono = campo('telefono', 40);
$interes  = campo('interes', 80);
$pack     = campo('pack', 40);
$mensaje  = campo('mensaje', 3000);

if ($nombre === '' || !filter_var($email, FILTER_VALIDATE_EMAIL) || empty($_POST['acepto'])) {
  http_response_code(422); echo json_encode(['ok'=>false]); exit;
}

$para    = 'contacto@kreadigitalstudio.es';
$asunto  = '=?UTF-8?B?' . base64_encode('Nueva auditoría IA · ' . $nombre) . '?=';
$cuerpo  = "Nueva solicitud de auditoría IA desde la web\n\n"
         . "Nombre: $nombre\nCorreo: $email\nTeléfono: $telefono\nNegocio: $negocio\n"
         . "Quiere automatizar: $interes\nPack: $pack\n\nMensaje:\n$mensaje\n\n"
         . "Fecha: " . date('d/m/Y H:i') . "\n";
$cabeceras = "From: KREA Digital Studio <no-reply@kreadigitalstudio.es>\r\n"
           . "Reply-To: " . preg_replace('/[\r\n]/', '', $email) . "\r\n"
           . "MIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\n";

$ok = @mail($para, $asunto, $cuerpo, $cabeceras);
echo json_encode(['ok' => (bool)$ok]);
