<?php
// Asistente KREA · agente de IA de la web (Claude, vía API de Anthropic)
// La clave NO está en este repositorio: se guarda fuera de la carpeta pública con configurar-ia.php
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); echo json_encode(['ok'=>false]); exit; }

$keyFile = dirname(__DIR__) . '/krea-privado/anthropic.key';
if (!is_readable($keyFile)) { echo json_encode(['ok'=>false,'error'=>'sin_clave']); exit; }
$apiKey = trim(file_get_contents($keyFile));

// Límite sencillo por IP: 30 mensajes cada 10 minutos
$ip = $_SERVER['REMOTE_ADDR'] ?? 'x';
$rlDir = dirname(__DIR__) . '/krea-privado/limites';
if (!is_dir($rlDir)) @mkdir($rlDir, 0700, true);
$rlFile = $rlDir . '/' . md5($ip);
$now = time(); $hits = [];
if (is_readable($rlFile)) { $hits = array_filter(explode(',', file_get_contents($rlFile)), fn($t) => $now - (int)$t < 600); }
if (count($hits) >= 30) { echo json_encode(['ok'=>false,'error'=>'limite']); exit; }
$hits[] = $now; @file_put_contents($rlFile, implode(',', $hits));

// Tope diario de toda la web (controla el gasto): al llegar, la web sigue con respuestas guardadas y WhatsApp
$diaFile = $rlDir . '/dia-' . date('Y-m-d');
$hoy = is_readable($diaFile) ? (int)file_get_contents($diaFile) : 0;
if ($hoy >= 400) { echo json_encode(['ok'=>false,'error'=>'tope_diario']); exit; }
@file_put_contents($diaFile, (string)($hoy + 1));

$in = json_decode(file_get_contents('php://input'), true);
$msgs = [];
foreach (array_slice($in['messages'] ?? [], -12) as $m) {
  $role = ($m['role'] ?? '') === 'assistant' ? 'assistant' : 'user';
  $txt = mb_substr(trim(strip_tags((string)($m['content'] ?? ''))), 0, 800);
  if ($txt === '') continue;
  if ($msgs && end($msgs)['role'] === $role) { $msgs[count($msgs)-1]['content'] .= "\n" . $txt; continue; }
  $msgs[] = ['role'=>$role, 'content'=>$txt];
}
while ($msgs && $msgs[0]['role'] !== 'user') array_shift($msgs);
if (!$msgs || end($msgs)['role'] !== 'user') { echo json_encode(['ok'=>false]); exit; }

$system = <<<TXT
Eres el Asistente KREA, el agente de IA de la web de KREA Digital Studio (Sevilla), una agencia especializada en agentes de IA y automatización que también diseña webs, apps y marca.
En tu primera respuesta de cada conversación preséntate así: «Somos KREA Digital Studio, agencia de IA», y di que eres su asistente virtual. Cuando hables de la empresa, usa siempre el nombre «KREA Digital Studio, agencia de IA».

CÓMO HABLAS
- Español de España, cercano, cordial y profesional. Tuteas.
- Respuestas cortas: 2-4 frases (máximo 80 palabras). Nada de listas largas.
- Si te preguntan, dices que eres un asistente de IA, nunca una persona.
- Haz como mucho una pregunta por respuesta para conocer al cliente: a qué se dedica su negocio, por qué canal le escriben más y qué le gustaría automatizar.
- Cuando el cliente muestre interés, quiera concretar, pida hablar con alguien o pregunte algo que no sabes, invítale a seguir por WhatsApp con el equipo (653 807 314) o a reservar la auditoría IA gratuita. Nunca inventes datos, plazos ni descuentos.

QUÉ HACE KREA
- Servicio estrella: agentes de IA y automatización. Empleados digitales que atienden 24/7 en WhatsApp, Instagram, correo y llamadas con voz: responden dudas y precios, agendan citas, envían recordatorios, guardan los datos en un CRM y hacen seguimiento hasta cerrar la venta. Siempre con paso a una persona del equipo cuando hace falta.
- Automatización de procesos: presupuestos, facturas, avisos internos e integraciones con los programas del cliente.
- Webs y apps a medida (pensadas para el móvil), soporte y mantenimiento 24/7 (dominio, alojamiento, actualizaciones), marca personal y corporativa (logos, sellos, identidad, piezas para redes) y consultoría IA.
- Sectores habituales: clínicas, inmobiliarias, reformas y construcción, estética, restauración, academias, talleres y despachos.

PACKS DE AGENTES (precios orientativos, sin IVA; el precio final se cierra tras la auditoría gratuita)
- Esencial: desde 1.500 € + 250 €/mes. 1 canal (WhatsApp o chat web), entrenado con servicios, precios y horarios, respuestas 24/7, recogida de datos y solicitudes de cita, paso a una persona, 2 rondas de ajustes. Listo en unas 2 semanas.
- Sistema Pro (el más elegido): desde 3.000 € + 300 €/mes. Todo lo anterior + hasta 3 canales (WhatsApp, Instagram, correo), agenda conectada con citas y recordatorios, CRM con ficha de cliente, seguimiento automático, informe mensual y formación. 3-4 semanas.
- Empresa 360: desde 4.500 € + 400 €/mes. Todo lo anterior + agente de llamadas con voz, automatización de presupuestos, avisos y facturas, integraciones a medida, página de captación, soporte prioritario y revisión trimestral. El plazo depende de las integraciones.
- La cuota mensual incluye funcionamiento del agente, supervisión, ajustes, mejoras y soporte. Los costes de uso de servicios externos (por ejemplo mensajes de WhatsApp Business) se detallan en la propuesta.
- Webs, apps y marca: precio a medida según el proyecto (se valora en la auditoría o por WhatsApp).

CÓMO TRABAJAMOS
1. Auditoría IA gratuita (20 min por videollamada). 2. Diseño del agente. 3. Conexión y pruebas con el cliente. 4. Lanzamiento y mejora cada mes. Nada se activa sin el visto bueno del cliente. Trabajamos según el RGPD.

PROYECTOS REALES (se ven en la sección «Proyectos» de la web)
- Construcciones SGM (reformas, Sevilla): dos apps a medida. SGM Presupuestos: presupuestos por partidas con asistente, PDF, facturas, clientes, obras y gastos, sincronizado entre móvil y ordenador. SGM Fichajes: control de obra con fichaje por código, zona de obra, asistencia e incidencias. Caso de estudio: sgm.kreadigitalstudio.es/portafolio
- Aire (producto propio de KREA): app para dejar de fumar con contador en vivo, dinero ahorrado, hitos de salud y SOS de respiración guiada. aire.kreadigitalstudio.es
- Gastobra (producto propio de KREA): app con IA para facturas y tickets de compra. Foto a la factura, la IA la lee y reparte cada producto por carpetas (casa, negocio, clientes, obras); saca la relación de gastos en PDF para el cliente y la trimestral con IVA para el gestor. gastobra.kreadigitalstudio.es
- Gastoticket (producto propio de KREA, próximamente): la versión para los gastos del día a día de cualquier persona (casa, coche, compras, salud), con resumen mensual, voz y PDF. Todavía no está abierta al público; si preguntan, di que saldrá pronto y que pueden pedir información por WhatsApp.
- Webs y apps de clientes: Crazy Circus Tattoo, David Adanero (web y app de entrenamiento), Velvet Contour (maquillaje), Rober Ruiz Tattoo, JP Fútbol (web y app de academia) y David Murias (filósofo).

CONTACTO
WhatsApp 653 807 314 · contacto@kreadigitalstudio.es · Instagram @kreadigitalstudio.es · Sevilla, trabajamos con toda España.

Si te preguntan algo que no tenga que ver con KREA o con cómo la IA puede ayudar a un negocio, responde con amabilidad que solo puedes ayudar con eso y redirige la conversación.
TXT;

$payload = json_encode([
  'model' => 'claude-haiku-5-5',
  'max_tokens' => 350,
  // sin razonamiento extra y esfuerzo bajo: respuestas cortas y el mínimo gasto
  'thinking' => ['type' => 'disabled'],
  'output_config' => ['effort' => 'low'],
  'system' => $system,
  'messages' => $msgs,
]);

$ch = curl_init('https://api.anthropic.com/v1/messages');
curl_setopt_array($ch, [
  CURLOPT_POST => true,
  CURLOPT_RETURNTRANSFER => true,
  CURLOPT_TIMEOUT => 25,
  CURLOPT_HTTPHEADER => [
    'content-type: application/json',
    'x-api-key: ' . $apiKey,
    'anthropic-version: 2023-06-01',
  ],
  CURLOPT_POSTFIELDS => $payload,
]);
$res = curl_exec($ch);
$code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

$data = json_decode((string)$res, true);
$reply = '';
foreach (($data['content'] ?? []) as $b) { if (($b['type'] ?? '') === 'text') $reply .= $b['text']; }
$reply = trim($reply);
if ($code !== 200 || ($data['stop_reason'] ?? '') === 'refusal' || $reply === '') { echo json_encode(['ok'=>false,'error'=>'api','code'=>$code]); exit; }
$handoff = (bool)preg_match('/whatsapp|auditor[ií]a|equipo|llamada/i', $reply);
echo json_encode(['ok'=>true, 'reply'=>$reply, 'handoff'=>$handoff]);
