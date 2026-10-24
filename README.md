# KREA Digital Studio · web oficial

Web de **KREA Digital Studio**, agencia de IA de Sevilla: agentes de IA y automatización, webs, apps y marca.

- Dirección final: **https://kreadigitalstudio.es** (la que enlaza el perfil de Instagram).

## Qué hay en el repositorio

| Archivo | Para qué sirve |
|---|---|
| `index.html` | La web completa (portada, agentes, packs, calculadora, proyectos, preguntas, auditoría). |
| `assets/` | Imágenes de la web, la imagen para compartir en redes (`og-krea.jpg`) y el icono del móvil. |
| `asistente.php` | Agente **KREA IA**: responde con Claude Haiku. Si no hay servidor PHP o clave, la web contesta con respuestas guardadas y WhatsApp. |
| `configurar-ia.php` | Página para pegar la clave de la API de Claude una sola vez. Se guarda fuera de la web y la página queda bloqueada. |
| `contacto.php` | Envía el formulario de la auditoría gratuita a contacto@kreadigitalstudio.es. |
| `robots.txt`, `sitemap.xml`, `404.html`, `.htaccess` | Buscadores, página de error y protección del sitio. |
| `portafolio/` | Portafolio web (`/portafolio/`) y en PDF. |
| `.github/workflows/publicar-ovh.yml` | Botón para publicar en el hosting de OVH. |

## Gasto del agente de IA

Solo se paga cuando un visitante escribe en el chat. Límites incluidos:

- Modelo Claude Haiku, sin razonamiento extra y con respuestas cortas.
- 30 mensajes por visitante cada 10 minutos.
- Tope de 400 mensajes al día en toda la web; al llegar, el chat sigue con respuestas guardadas y WhatsApp.
- Recomendado: poner un límite de gasto mensual en console.anthropic.com → Billing → Limits.

## Publicar (hosting de OVH, igual que Gastobra y Gastoticket)

La web se publica en el hosting de OVHcloud, en la carpeta del dominio principal (`www/`), con el botón de GitHub Actions. No se usa GitHub Pages: el repositorio es privado.

**Una sola vez:**
1. GitHub → `krea-web` → Settings → General → Danger Zone → **Change visibility → Private**.
2. GitHub → `krea-web` → Settings → Secrets and variables → Actions → **New repository secret**: nombre `OVH_FTP_PASSWORD`, valor la contraseña FTP del hosting (la misma que en Gastobra).
3. OVH → Hosting → **Multisitio**: comprobar que `kreadigitalstudio.es` y `www.kreadigitalstudio.es` apuntan a la carpeta `www`, con SSL. Si es otra carpeta, cambiar `server-dir` en `.github/workflows/publicar-ovh.yml`.

**Cada vez que se quiera publicar:** GitHub → Actions → «Publicar en OVH (kreadigitalstudio.es)» → **Run workflow**.

**Después de publicar:**
- Abrir `https://kreadigitalstudio.es/configurar-ia.php`, pegar la clave de la API de Claude y pulsar «Guardar y activar».
- Actualizar la vista previa de Instagram y WhatsApp en https://developers.facebook.com/tools/debug/ («Volver a extraer»).

## Protección (estándar KREA)

- Repositorio **privado**: el código no se ve en GitHub.
- `.htaccess`: siempre https, sin listado de carpetas, la web no se puede meter dentro de otra página y los archivos internos no se sirven.
- Aviso de © y cláusula de propiedad intelectual en el pie y en «Privacidad y cookies»; las imágenes no se pueden guardar con clic derecho ni arrastrar.
- Una web pública siempre se puede ver y guardar desde el navegador; estas medidas impiden el acceso al código fuente del repositorio y dificultan la copia, y el aviso legal deja constancia de la autoría.

## Portafolio en PDF

`portafolio/KREA-Portafolio-2026.pdf`. Para regenerarlo tras cambiar `portafolio/generar-pdf.py`: `python3 portafolio/generar-pdf.py <carpeta-con-las-fuentes-Oswald-Manrope-Cormorant>` y se imprime `portafolio/KREA-Portafolio.html` a PDF con Chromium (A4 horizontal, con fondos).

## Proyectos que aparecen en la web

Construcciones SGM, Aire, Gastobra, Gastoticket (próximamente), David Adanero (se muestra su app), JP Fútbol (app y web), Velvet Contour, Crazy Circus Tattoo, Rober Ruiz Tattoo y David Murias.

**Solo imágenes:** en la web, en el portafolio y en su PDF los proyectos no llevan enlaces ni direcciones, y el agente KREA IA no las da. Quien quiera verlos pide una demostración.
