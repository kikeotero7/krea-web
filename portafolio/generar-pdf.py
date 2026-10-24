"""Genera portafolio/KREA-Portafolio.html para imprimir en PDF (A4 horizontal).

Uso: python3 portafolio/generar-pdf.py <carpeta-de-fuentes>
y después se imprime el HTML a PDF con Chromium (ver README).
Para añadir o cambiar un proyecto, se edita la lista PROYECTOS.
"""
import html
import pathlib
import sys

RAIZ = pathlib.Path(__file__).resolve().parent.parent
ASSETS = RAIZ / "assets"
FUENTES = pathlib.Path(sys.argv[1]).resolve()

# (imagen, sector, nombre, tipo, frase, bloques, etiquetas, dirección interna, estado)
# Las direcciones de los proyectos no se publican en el PDF: los enlaces son privados.
PROYECTOS = [
    ("p-sgm-2026.webp", "Construcción y reformas · Sevilla", "Construcciones SGM", "App a medida",
     "Dos aplicaciones a medida que organizan la empresa de Sergio.",
     [("SGM Presupuestos", "Presupuestos por partidas con asistente, PDF para el cliente, facturas, clientes, obras y gastos, con los datos en la nube entre móvil y ordenador."),
      ("SGM Fichajes", "Control de obra con fichaje por código, zona de la obra, asistencia e incidencias.")],
     ["App de gestión", "Presupuestos y facturas", "Fichajes", "Datos en la nube"], "sgm.kreadigitalstudio.es/portafolio/", "Online"),
    ("p-aire.webp", "Producto propio de KREA · Salud", "Aire · Deja de fumar", "App instalable",
     "Nuestra app para dejar de fumar, un día cada vez.",
     [("En el móvil", "Contador en vivo, dinero ahorrado, hitos de salud, diario y metas, en modo claro y oscuro."),
      ("SOS", "Respiración guiada de 3 minutos para cada antojo."),
      ("Venta", "Web de venta, prueba gratuita, pago único y licencias.")],
     ["App instalable", "Web de venta", "Pagos y licencias"], "aire.kreadigitalstudio.es", "Online"),
    ("p-gastobra.webp", "Producto propio de KREA · Facturas con IA", "Gastobra", "App con IA",
     "Facturas y tickets de compra ordenados con una foto.",
     [("Lectura con IA", "Haces una foto, la IA lee tienda, fecha, productos, base, IVA y total, y repartes cada producto entre tus carpetas tocando o con la voz."),
      ("Para el gestor", "Relación de gastos en PDF para el cliente y relación trimestral con el IVA real de cada factura.")],
     ["Lectura con IA", "Voz", "PDF e IVA trimestral", "Datos en la nube"], "gastobra.kreadigitalstudio.es", "Online"),
    ("p-gastoticket.webp", "Producto propio de KREA · Gastos del día a día", "Gastoticket", "App con IA",
     "De la familia de Gastobra, para los gastos de cualquier persona.",
     [("Una foto al ticket", "La IA lo lee y lo reparte entre Casa, Coche, Compras o Salud."),
      ("Cuánto gastas", "Resumen de cada mes frente al anterior, en qué tipo de cosas y PDF de gastos.")],
     ["Lectura con IA", "Resumen mensual", "Voz", "PDF"], "En prueba privada · lanzamiento en 2027", "Próximamente"),
    ("p-adanero.webp", "Entrenamiento personal", "David Adanero", "App y web",
     "App y web para un entrenador personal, preparador físico y readaptador.",
     [("App", "Su espacio de trabajo: resumen del día con cómo llega cada cliente, agenda, sesiones, planes, progreso, readaptación, informes y cobros, con vista para sus clientes."),
      ("Web", "Servicios, grupos, método y reserva de cita.")],
     ["App de gestión", "Clientes y planes", "Agenda y cobros", "Web"], "david-adanero.kreadigitalstudio.es", "Online"),
    ("p-jpfutbol-app.webp", "Tecnificación deportiva · Sevilla", "JP Fútbol", "App y web",
     "App y web para una academia de tecnificación de fútbol.",
     [("App", "Para el equipo técnico y las familias: grupos del día, asistencia, plan de cada sesión, fichas de jugadores, avisos y packs y pagos."),
      ("Web", "Presenta la academia: técnica, preparación física y porteros. Ahora en presentación privada con código de acceso.")],
     ["App de academia", "Asistencia y sesiones", "Packs y pagos", "Web"], "jpfutbol-web.kreadigitalstudio.es", "En presentación"),
    ("p-velvet.webp", "Atelier de maquillaje", "Velvet Contour", "Marca y web",
     "Marca y web para un atelier de maquillaje a domicilio.",
     [("Marca", "Logotipo, sellos y fotografía de portada."),
      ("Web", "Novias, madrinas, invitadas y eventos, técnicas, orientador de estilo y reserva de cita.")],
     ["Logo y sellos", "Web", "Reservas"], "velvet.kreadigitalstudio.es", "Online"),
    ("p-crazycircus.webp", "Estudio de tatuaje · Andorra", "Crazy Circus Tattoo", "Web",
     "Web con identidad de circo para un estudio de tatuaje, piercing y streetwear.",
     [("Web", "Equipo, tatuajes, joyas, tienda, prints y reservas, en español y catalán, con asistente de citas.")],
     ["Web", "Tienda", "Citas", "Dos idiomas"], "crazycircus.kreadigitalstudio.es", "Online"),
    ("p-roberruiz.webp", "Tatuaje · Triana, Sevilla", "Rober Ruiz Tattoo", "Web",
     "Portfolio para un tatuador de Triana.",
     [("Web", "Trabajos, vídeos del proceso, sobre él y reserva de cita por WhatsApp o Instagram.")],
     ["Web portfolio", "Vídeos", "Citas"], "roberruiz.kreadigitalstudio.es", "Online"),
    ("p-murias.webp", "Filosofía práctica · Andorra", "David Murias", "Marca personal",
     "Web de marca personal para un filósofo y asesor filosófico.",
     [("Web", "Filosofía práctica, consultas, conferencias y divulgación, con un tono sereno y editorial.")],
     ["Marca personal", "Web"], "david-murias.kreadigitalstudio.es", "Online"),
]

e = html.escape
N = len(PROYECTOS)


def enlace(url):
    if "." in url.split(" ")[0] and "/" not in url[:8]:
        return f'<a href="https://{e(url)}">{e(url)}</a>'
    return e(url)


paginas = []
indice = "".join(f"<li><span>{i + 1:02d}</span><b>{e(p[2])}</b><i>{e(p[3])}</i></li>" for i, p in enumerate(PROYECTOS))
paginas.append(f"""<section class="page cover">
<img class="logo" src="file://{ASSETS}/logo-krea-oscuro.webp" alt="">
<div class="cv"><p class="eyebrow">Agencia de IA · Sevilla</p>
<h1>Portafolio<span class="script">de proyectos.</span></h1>
<p class="lead">Apps propias y a medida, webs, marca y agentes de IA para empresas, comercios y profesionales.</p></div>
<ol class="index">{indice}</ol>
<div class="foot"><span>© 2026 KREA Digital Studio · Todos los derechos reservados</span><span>Octubre 2026</span></div>
</section>""")
for i, (img, meta, nombre, tipo, frase, bloques, etiquetas, url, estado) in enumerate(PROYECTOS):
    bl = "".join(f'<div class="bl"><b>{e(t)}</b><p>{e(d)}</p></div>' for t, d in bloques)
    tg = "".join(f"<span>{e(t)}</span>" for t in etiquetas)
    cls = "" if estado == "Online" else " soon"
    paginas.append(f"""<section class="page proj">
<div class="shot"><img src="file://{ASSETS}/{img}" alt=""></div>
<div class="txt"><p class="num">{i + 1:02d} <em>/ {N:02d}</em></p>
<p class="eyebrow">{e(meta)}</p><h2>{e(nombre)}</h2><p class="kind">{e(tipo)}</p>
<p class="lead">{e(frase)}</p>{bl}<div class="tags">{tg}</div>
<p class="url"><span class="st{cls}">{e(estado)}</span>Demostración privada bajo petición</p></div>
<div class="foot"><span>© 2026 KREA Digital Studio · Portafolio</span><span>{i + 2}</span></div>
</section>""")
paginas.append(f"""<section class="page marca">
<div class="cv"><p class="eyebrow">Marca personal y corporativa</p><h1 class="small">Identidades<span class="script">que se reconocen.</span></h1></div>
<div class="mgrid">
<figure><div class="shot"><img src="file://{ASSETS}/marca-velvet.webp" alt=""></div><figcaption><b>Velvet Contour</b><span>Marca corporativa · logotipo, tres sellos y paleta cobre, chocolate y crema</span></figcaption></figure>
<figure><div class="shot"><img src="file://{ASSETS}/marca-murias.webp" alt=""></div><figcaption><b>David Murias</b><span>Marca personal · emblema DM en negro y dorado, nombre, lema, retrato, paleta y tipografía editorial</span></figcaption></figure>
</div>
<div class="foot"><span>© 2026 KREA Digital Studio · Portafolio</span><span>{N + 2}</span></div>
</section>""")
paginas.append(f"""<section class="page end">
<img class="logo" src="file://{ASSETS}/logo-krea-oscuro.webp" alt="">
<div class="cv"><p class="eyebrow">Qué hacemos</p><h1 class="small">Un mismo estudio<span class="script">para todo lo digital.</span></h1></div>
<div class="svc">
<div><b>Agentes de IA</b><p>Atienden WhatsApp, Instagram, correo y teléfono, y agendan citas 24/7.</p></div>
<div><b>Apps a medida</b><p>Presupuestos, fichajes, facturas, clientes o citas desde el móvil.</p></div>
<div><b>Webs</b><p>Rápidas, pensadas para el móvil y preparadas para captar clientes.</p></div>
<div><b>Marca</b><p>Logos, sellos, identidad y piezas para redes.</p></div></div>
<div class="contact">
<div><span>WhatsApp</span><b>653 807 314</b></div>
<div><span>Correo</span><b>contacto@kreadigitalstudio.es</b></div>
<div><span>Instagram</span><b>@kreadigitalstudio.es</b></div>
<div><span>Web</span><b><a href="https://kreadigitalstudio.es">kreadigitalstudio.es</a></b></div></div>
<p class="legal">© 2026 KREA Digital Studio. Diseño, textos, capturas e imágenes protegidos. Prohibida su copia o reproducción, total o parcial, sin autorización por escrito.</p>
<div class="foot"><span>Auditoría IA gratuita · 20 minutos por videollamada</span><span>{N + 3}</span></div>
</section>""")

css = f"""
@font-face{{font-family:Oswald;src:url(file://{FUENTES}/Oswald.ttf);font-weight:200 700}}
@font-face{{font-family:Manrope;src:url(file://{FUENTES}/Manrope.ttf);font-weight:200 800}}
@font-face{{font-family:Cormorant;src:url(file://{FUENTES}/Cormorant-Italic.ttf);font-style:italic;font-weight:300 700}}
@page{{size:297mm 210mm;margin:0}}
:root{{--ink:#090909;--ink2:#13120f;--ivory:#f4f0e7;--muted:rgba(244,240,231,.66);--line:rgba(244,240,231,.16);--gold:#caa43a;--gold-l:#e0c46d}}
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:var(--ink);-webkit-print-color-adjust:exact;print-color-adjust:exact}}
body{{font-family:Manrope,sans-serif;color:var(--ivory);font-size:10.5pt;line-height:1.55}}
a{{color:inherit;text-decoration:none}}
.page{{width:297mm;height:210mm;position:relative;overflow:hidden;page-break-after:always;background:var(--ink);padding:16mm 18mm}}
.page:last-child{{page-break-after:auto}}
.eyebrow{{font-size:8pt;letter-spacing:.22em;text-transform:uppercase;color:var(--gold);font-weight:700}}
h1,h2{{font-family:Oswald,sans-serif;font-weight:600;text-transform:uppercase;line-height:1}}
.script{{display:block;font-family:Cormorant,serif;font-style:italic;font-weight:600;text-transform:none;color:var(--gold);font-size:.6em;margin-top:2mm}}
.foot{{position:absolute;left:18mm;right:18mm;bottom:9mm;display:flex;justify-content:space-between;font-size:7.5pt;letter-spacing:.14em;text-transform:uppercase;color:var(--muted);border-top:1px solid var(--line);padding-top:3mm}}
.logo{{width:52mm;display:block}}
.cover .cv{{position:absolute;left:18mm;top:58mm;width:150mm}}
.cover h1{{font-size:62pt;margin-top:5mm}}
.cover .lead{{color:var(--muted);font-size:11.5pt;margin-top:8mm;max-width:120mm}}
.index{{position:absolute;right:18mm;top:34mm;width:92mm;list-style:none;border-top:1px solid var(--line)}}
.index li{{display:grid;grid-template-columns:10mm 1fr auto;align-items:baseline;gap:3mm;padding:2.6mm 0;border-bottom:1px solid var(--line)}}
.index span{{font-size:8pt;color:var(--gold);letter-spacing:.08em}}
.index b{{font-family:Oswald,sans-serif;font-weight:500;text-transform:uppercase;font-size:12pt}}
.index i{{font-style:normal;font-size:8pt;color:var(--muted)}}
.cover::after{{content:"";position:absolute;left:0;bottom:0;width:100%;height:2.2mm;background:var(--gold)}}
.proj{{display:grid;grid-template-columns:165mm 1fr;gap:12mm;align-items:center;padding-bottom:22mm}}
.shot{{border:1px solid var(--line);border-radius:2mm;overflow:hidden;aspect-ratio:16/10;background:var(--ink2)}}
.shot img{{width:100%;height:100%;object-fit:cover;object-position:top;display:block}}
.txt{{display:flex;flex-direction:column;gap:2.6mm}}
.num{{font-family:Oswald,sans-serif;font-size:22pt;color:var(--gold);font-weight:500;line-height:1}}
.num em{{font-style:normal;font-size:10pt;color:var(--muted)}}
.proj h2{{font-size:27pt}}
.kind{{font-family:Cormorant,serif;font-style:italic;font-weight:600;color:var(--gold-l);font-size:15pt;line-height:1;margin-top:-1mm}}
.proj .lead{{font-size:11pt;margin-top:1mm}}
.bl{{border-left:1.5px solid var(--gold);padding-left:3.5mm}}
.bl b{{font-size:9pt;letter-spacing:.06em;text-transform:uppercase}}
.bl p{{color:var(--muted);font-size:9.5pt}}
.tags{{display:flex;flex-wrap:wrap;gap:1.6mm;margin-top:1mm}}
.tags span{{font-size:7.8pt;border:1px solid var(--line);border-radius:10mm;padding:.8mm 2.8mm}}
.url{{font-size:9pt;display:flex;align-items:center;gap:2.5mm;margin-top:1.5mm}}
.url a{{border-bottom:1px solid var(--gold)}}
.st{{font-size:7pt;letter-spacing:.14em;text-transform:uppercase;border:1px solid var(--line);border-radius:10mm;padding:.6mm 2.4mm;display:inline-flex;align-items:center;gap:1.4mm;flex:none}}
.st::before{{content:"";width:1.6mm;height:1.6mm;border-radius:50%;background:#3ddc84}}
.st.soon::before{{background:var(--gold)}}
.end .cv{{margin-top:16mm}}
.end h1.small{{font-size:40pt;margin-top:4mm}}
.svc{{display:grid;grid-template-columns:repeat(4,1fr);gap:1px;background:var(--line);border:1px solid var(--line);margin-top:12mm}}
.svc div{{background:var(--ink);padding:5mm}}
.svc b{{font-family:Oswald,sans-serif;font-weight:500;text-transform:uppercase;font-size:13pt;display:block;margin-bottom:1.5mm}}
.svc p{{color:var(--muted);font-size:9pt}}
.contact{{display:grid;grid-template-columns:repeat(4,1fr);gap:6mm;margin-top:12mm}}
.contact span{{display:block;font-size:7.5pt;letter-spacing:.18em;text-transform:uppercase;color:var(--gold);font-weight:700}}
.contact b{{font-size:11pt;font-weight:600}}
.marca h1.small{{font-size:34pt;margin-top:3mm}}
.mgrid{{display:grid;grid-template-columns:1fr 1fr;gap:8mm;margin-top:9mm}}
.mgrid figure{{margin:0}}
.mgrid figcaption{{margin-top:3mm;display:flex;flex-direction:column}}
.mgrid figcaption b{{font-family:Oswald,sans-serif;font-weight:500;text-transform:uppercase;font-size:13pt}}
.mgrid figcaption span{{font-size:8.5pt;color:var(--muted)}}
.legal{{margin-top:12mm;font-size:8pt;color:var(--muted);max-width:200mm}}
"""
salida = pathlib.Path(__file__).resolve().parent / "KREA-Portafolio.html"
salida.write_text(f'<!doctype html><html lang="es"><head><meta charset="utf-8"><title>Portafolio KREA Digital Studio</title><style>{css}</style></head><body>{"".join(paginas)}</body></html>', encoding="utf-8")
print(salida)
