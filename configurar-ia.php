<?php
// Configuración única de la clave del Asistente KREA.
// La clave se guarda FUERA de la carpeta pública. Cuando ya existe, esta página queda bloqueada.
$dir = dirname(__DIR__) . '/krea-privado';
$keyFile = $dir . '/anthropic.key';
$msg = '';
if (is_readable($keyFile)) {
  $msg = 'El asistente ya está configurado. Para cambiar la clave hay que borrar el archivo krea-privado/anthropic.key desde el alojamiento.';
} elseif ($_SERVER['REQUEST_METHOD'] === 'POST') {
  $k = trim((string)($_POST['k'] ?? ''));
  if (!preg_match('/^sk-ant-[A-Za-z0-9_\-]{20,}$/', $k)) {
    $msg = 'La clave no tiene el formato esperado (empieza por sk-ant-). Revísala.';
  } else {
    if (!is_dir($dir)) mkdir($dir, 0700, true);
    file_put_contents($keyFile, $k);
    @chmod($keyFile, 0600);
    @file_put_contents($dir . '/.htaccess', "Require all denied\n");
    $msg = 'Listo. El Asistente KREA ya responde con inteligencia artificial. Esta página queda bloqueada.';
  }
}
?><!doctype html>
<html lang="es"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex,nofollow">
<title>Configurar asistente · KREA</title>
<style>body{margin:0;min-height:100vh;display:grid;place-items:center;background:#090909;color:#f4f0e7;font-family:system-ui,sans-serif;padding:20px}
.c{max-width:440px;width:100%;border:1px solid #caa43a;border-radius:8px;padding:28px;background:#12110f}
h1{font-size:20px;margin:0 0 10px}p{color:rgba(255,255,255,.7);font-size:14px;line-height:1.5}
input{width:100%;box-sizing:border-box;padding:12px;border-radius:6px;border:1px solid #444;background:#1a1814;color:#f4f0e7;font-size:14px}
button{margin-top:12px;width:100%;padding:13px;border:0;border-radius:6px;background:#caa43a;color:#090909;font-weight:700;font-size:14px;cursor:pointer}
.m{background:#1a1814;border-left:3px solid #caa43a;padding:10px 12px;margin-top:14px;font-size:14px}</style></head>
<body><div class="c"><h1>Asistente KREA · clave de IA</h1>
<?php if (!is_readable($keyFile)): ?>
<p>Pega aquí la clave de la API de Claude (Claude Console). Se guarda fuera de la web y no se vuelve a mostrar.</p>
<form method="post" autocomplete="off"><input name="k" type="password" placeholder="sk-ant-…" required><button>Guardar y activar</button></form>
<?php endif; ?>
<?php if ($msg): ?><div class="m"><?= htmlspecialchars($msg) ?></div><?php endif; ?>
</div></body></html>
