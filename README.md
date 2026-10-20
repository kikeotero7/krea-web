# KREA Digital Studio · web oficial

Web de **KREA Digital Studio**, agencia de IA de Sevilla: agentes de IA y automatización, webs, apps y marca.

- Dirección final: **https://kreadigitalstudio.es** (la que enlaza el perfil de Instagram).
- Vista previa mientras se revisa: **https://nueva.kreadigitalstudio.es** (archivo `CNAME`).

## Qué hay en el repositorio

| Archivo | Para qué sirve |
|---|---|
| `index.html` | La web completa (portada, agentes, packs, calculadora, proyectos, preguntas, auditoría). |
| `assets/` | Imágenes de la web, la imagen para compartir en redes (`og-krea.jpg`) y el icono del móvil. |
| `asistente.php` | Agente **KREA IA**: responde con Claude Haiku. Si no hay servidor PHP o clave, la web contesta con respuestas guardadas y WhatsApp. |
| `configurar-ia.php` | Página para pegar la clave de la API de Claude una sola vez. Se guarda fuera de la web y la página queda bloqueada. |
| `contacto.php` | Envía el formulario de la auditoría gratuita a contacto@kreadigitalstudio.es. |
| `robots.txt`, `sitemap.xml`, `404.html` | Buscadores y página de error. |

## Gasto del agente de IA

Solo se paga cuando un visitante escribe en el chat. Límites incluidos:

- Modelo Claude Haiku, sin razonamiento extra y con respuestas cortas.
- 30 mensajes por visitante cada 10 minutos.
- Tope de 400 mensajes al día en toda la web; al llegar, el chat sigue con respuestas guardadas y WhatsApp.
- Recomendado: poner un límite de gasto mensual en console.anthropic.com → Billing → Limits.

## Publicar

**Vista previa (GitHub Pages, sin PHP):** Settings → Pages → Deploy from a branch → `main` / `(root)` → Custom domain `nueva.kreadigitalstudio.es` → Enforce HTTPS. En OVH → zona DNS de kreadigitalstudio.es: CNAME `nueva` → `kikeotero7.github.io.`

**Web definitiva con el agente de IA y el formulario (hosting con PHP):**

1. Subir todo el contenido del repositorio a la carpeta pública del dominio (`public_html`).
2. Abrir `https://kreadigitalstudio.es/configurar-ia.php`, pegar la clave de la API de Claude y pulsar «Guardar y activar».
3. Al compartir la web en Instagram o WhatsApp, actualizar la vista previa en https://developers.facebook.com/tools/debug/ («Volver a extraer»).

## Proyectos que aparecen en la web

Construcciones SGM (`sgm.kreadigitalstudio.es/portafolio/`), Aire (`aire.kreadigitalstudio.es`), Crazy Circus Tattoo, David Adanero, Velvet Contour, Rober Ruiz Tattoo, JP Fútbol y David Murias.
