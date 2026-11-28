# Hooks virales: referencia

Para todo video de la carpeta `hooks virales/`. Karen **no sale**: voz en off clonada (ElevenLabs) y gráficos a **pantalla completa**.

## Receta vigente: estilo de referencias (aprobada con el 008 v2, 27 nov 2026)
Desde el 008 v2, todos los hooks siguientes usan este estilo. Las referencias están en `hooks virales/_referencias/`, con un `README.md`. La plantilla es `plantilla-hooks/index.html` (= `hooks virales/008 - …/graficos/index.html`) y `nuevo-hook.sh` la copia. El estilo ilustrado anterior (001–007) quedó en `plantilla-hooks-v1/` y solo se usa si lo piden.
- **Fondo:** cuadrícula fina lavanda sobre `#F7F4FA`. Paleta de Karen: ciruela `#2E2545`, lavanda, rosa, arena; verde `#1E9E6A` solo para «hecho» y rojo `#C0392B` solo para pausa o alerta.
- **Línea de tiempo:** línea vertical a la izquierda (x 100) con avatar y chip de paso numerado (`01 La tarea` … `05 Qué hacer`), uno por bloque del guion. Las marcas de la línea suben en cada cambio de paso.
- **Subtítulo arriba** (y 300–460, Outfit 62): frases de ≤6 palabras. Las palabras dichas se ven nítidas y las que siguen aparecen borrosas; la palabra clave va en un recuadro de selección lavanda con esquinas. No hay subtítulo abajo.
- **Contenido** (x 160–960, y 640–1420): tarjetas tipo app (documento, notificación, registro, ajuste con interruptor, cita «Agendar → Agendada», lista con palomitas), diagramas sencillos (anillo con nodos y contador 1/3→3/3) y comparación A/B lado a lado con «≠». Íconos SVG simples con trazo ciruela.
- **Hilo continuo:** el objeto del gancho (en el 008, el documento en blanco y el cronómetro) persiste o vuelve al final transformado (se llena). Hay contadores que suben (cronómetro, palabras, habilidades).
- **Movimiento:** las tarjetas entran desde abajo con `back.out(1.35)` y salen hacia arriba. Lo secundario se atenúa con desenfoque. Nada vacío más de 1 s.
- **Cierre:** el CTA va en una pastilla con botón; luego el aviso «Este video orienta y no diagnostica.» y la web. La portada usa el mismo estilo: chip, gancho con la parte clave en recuadro de selección y la tarjeta del gancho.
- **Tamaño de texto (Eduardo, 28 nov 2026):** se ve en TikTok, Reels y Shorts y lo ven adultos que quizá usan lentes: **ningún texto menor a 40 px** (rótulos de tarjeta ≥34 px, nombres e ítems 40–54 px, chip de paso 40 px). Mejor pocas tarjetas grandes que muchas chicas; los dibujos (carritos, íconos) también grandes. Revisar un cuadro a tamaño real, no solo la hoja de contacto.
- **Leyenda y cierre con datos (Eduardo, 28 nov 2026):** durante todo el video, pastilla fija «Neuropsicóloga Karen Trujillo» (y 190, 40 px) sobre el subtítulo; se apaga cuando entra el cierre. El cierre es una tarjeta de texto, sin avatar ni foto: aviso «Este video orienta y no diagnostica.» + «Karen Trujillo», «Neuropsicóloga · Cancún», «Cédula 11009616» y la web. Teléfono y WhatsApp solo en la bio y el copy. La voz termina antes: la duración del video es el fin de la última palabra + 2.1 s (el audio se rellena con silencio, `-af apad` en `render.cjs`) para que el cierre se lea unos 3 s; el último subtítulo se apaga 0.4 s después de la última palabra.
- Siguen vigentes la instrucción obligatoria (abajo, puntos 1–10) y los elementos nuevos en cada video: el estilo se comparte, pero el contenido de las tarjetas y de los diagramas cambia según el tema.


## Instrucción obligatoria (Eduardo, 27 nov 2026) — aplicarla en cada video
1. Propón una acción visual por bloque y después arma la animación.
2. Usa como máximo cuatro palabras por escena, aparte de los subtítulos.
3. Convierte las ideas en acciones y dibuja las analogías del guion tal cual, de forma literal.
4. Muestra las magnitudes con escala, enfoca lo importante y conserva elementos entre escenas para que se vea cómo se van transformando.
5. Sincroniza cada acción clave con la palabra que le corresponde y deja una imagen final clara en cada escena.

Para gráficos (HyperFrames, Remotion o la plantilla GSAP):
6. Define primero la duración en cuadros/tiempo, el fps y el formato del lienzo antes de escribir el código.
7. Respeta márgenes y zonas seguras para que los gráficos y el micro-copy no choquen con subtítulos ni bordes del encuadre.
8. Usa curvas de movimiento suaves y naturales, evitando cortes bruscos o efectos innecesarios que distraigan del dato o la idea central.
9. Estructura cada escena de forma modular y limpia para que sea fácil retocar tiempos, tamaños o textos después.
10. **Elementos nuevos en cada video** (Eduardo, 27 nov 2026): dibuja elementos gráficos nuevos para que el video no se parezca a los anteriores. Revisa la lista «Elementos ya usados» y no repitas sus dibujos ni metáforas principales; solo se comparten el estilo (fondo, colores, trazo, rótulos, subtítulos) y el aviso final. Al guardar, agrega a la lista los elementos del video nuevo.

## Elementos ya usados (no repetir)
- **001:** hoja de respuestas con checks, reloj, cabeza con bombilla, barra de avance → camino con banderín, engranajes Comprender/Atención/Memoria/Organización, señal de alerta, círculos Distracción ⊃ TDAH, etiqueta «No se esfuerza», caja «?» con lupa, hoja de evaluación (clipboard), regla de medir con ✗, rompecabezas Fortalezas/Dificultades/Apoyos, burbuja de comentarios con corazón.
- **002:** burbujas de regaño que caen, tarjetas de instrucciones (juguetes, zapatos, mochila), pelota, estrellas en zigzag y nube de lluvia, engranajes Atención/Memoria de trabajo/Autorregulación, niños mini, cerca de límites, etiqueta «Desobediente» → «?», adulto junto al niño con corazón, pasos 1-2-3 sobre camino con meta, corredor dando vueltas en círculo, casa.
- **003:** estrellitas de travesura, cartas boca abajo numeradas sobre una mesa, fila de cartas chicas, dos niños con burbujas que se interrumpen, boleto de turno, barras de actividad a medias, mochila que tira nota/lápiz/cuaderno, engranaje Autorregulación, líneas punteadas a conceptos, sello «No confirma TDAH», línea de tiempo con reloj/casa/escuela y lupa, piezas Desarrollo/Conducta/Contextos, lupa saltando entre travesuras con ✗, bombilla sobre el niño.
- **004:** pantalla dividida monitor/cuaderno con relojes de arena, control de videojuego, monedas «+10» y trofeo, niño con gorra y pupilas que se mueven, silla vacía, mariposa, ovillo que se desenrolla, medidores (velocímetros) de atención, chispas, rayo, frasco que se llena de monedas, escalera con pesa «kg», cajas apiladas, termómetro, balanza pluma/pesa, cerebro, etiquetas colgantes que se deshacen, linterna con haz, cuadros juego/escuela/rutina, gráfica de radar, visor de cámara, teléfono y avión de papel.
- **005:** hoja de «Tarea» que se arruga en bola y se alisa con carita feliz, reloj digital que corre (4:00→6:30, 0:20→1:45), lágrimas, estallido «!!», lápiz partido, notas adhesivas «¡Ya!/¡Apúrate!/¡Siéntate!», caras del niño y del adulto (lentes y chongo) con remolinos y gotas de sudor, laberinto con ficha, tarjetas revueltas 3-1-2, espiral, pergamino «???», montaña, signo «?» grande, pluma roja con marcas, poste con flechas «Exigir más/Comprender mejor», megáfono, camino de piedras con tablas de apoyo, binoculares, ventana de comentarios con puntos de «escribiendo».
- **006:** contador de clics y palitos de conteo, mensajes «Guarda tus juguetes» que se apagan, cubos ABC/carrito/patito con círculos punteados, escritorio con cuadernos, huellas y puerta, oreja que rebota ondas, pizarra con tarjetas de imán (cubo, cuaderno, zapato), banda transportadora y caja, diana, cajonera, montón de 20 tarjetitas → 3 tarjetas grandes numeradas, candados con llaves distintas, calendario semanal con palomitas, brújula, control de volumen con bocina, tren con vagones, caja de juguetes ordenada, refrigerador con notas de imán.
- **007:** tarjeta «2 + 3 =» con respuesta 5 y palomita, hoja de examen con borrador y «?», niño con globo de diálogo, pizarra de tiza (sol, nube, flecha), reloj analógico que avanza, muro de ladrillos, nota 4 en círculo rojo, garabato de frustración, estante con libro que entra y sale, símbolo ≠, ojo con pupila, bandeja con tres pelotas que rebotan, manómetro con vapor, libro con «zzz» y pesas tachados, cadena de tres eslabones (libro, archivero, lápiz y hoja) con marcador, tres exámenes con nota 5 e iconos, iceberg con la nota en la punta, signo «?» rojo, escritorio con lámpara.
- **008 (estilo de referencias):** documento «Tarea · Cuaderno» con cursor y contador de palabras, cronómetro 00:00→41:00, notificación «Ya, empieza la tarea», registro «Lo que pasa» con «↻ Se repite», etiqueta «Parece: sin ganas», anillo de funciones ejecutivas (Iniciar/Organizar/Dirigir, contador 3/3, Iniciar en pausa), tarjetas Opción A/B con «≠» y «¿Flojo?», tarjetas «Motivo 1-3», interruptor «TDAH · No es automático», semana con días marcados y áreas (Escuela, Casa, Ánimo), cita «Valoración especializada» Agendar→Agendada, «Flojo» tachado, lista Abrir/Leer/Escribir, pastilla «Compártelo con otra familia».
- **009 (estilo de referencias):** fichas «Niño A»/«Niño B» con avatar y etiqueta «∞ Autismo» (hilo de todo el video), llave «Mismo diagnóstico → Mismo espectro», rasgos en filas (habla mucho, busca compañía, se comunica distinto, prefiere jugar solo), pastilla «∞ Espectro», mezclador de 4 características con puntos A/B y muchos puntos más, molde punteado «Imagen esperada» con candados que se agrieta, rasgos marcados «sin ver» (3 sin ver), «≈?», historia de desarrollo (Bebé, 2, 4 años, Hoy), perfil con barras, galería de 9 niños, «Acompañar mejor», encuesta «¿Conocías esta diversidad?», «Compártelo con alguien».
- **010 (estilo de referencias):** ficha «Juego compartido» con tres niños y pelotas, ficha «Tu hijo» con cinco carritos de tamaños distintos (hilo: revueltos → fila → por tamaño → vuelven al final), «Misma actividad ×14», barra «Objetos ↔ Personas», «¿Algo está pasando?», «Juego → Desarrollo infantil», áreas Imaginación/Flexibilidad/Interacción con selección que salta, filas de fichas Variado vs «Se repite», ranuras 1/5 + «No confirma autismo», meta «Jugar como todos» que se desvanece, columnas «Su juego»/«Otras áreas» unidas, centro «Desarrollo integral», «Evaluación especializada» con palomitas, «Jugar como otros» prohibido, «Cada juego comunica», etiquetas de formas de juego, «Compártela en comentarios».
- **011 (estilo de referencias):** escenario con cortina que se abre y silueta de niño (hilo: vuelve abierta y a color), tres pistas con «?» (conversación, calendario, estrella), «Todos los días» con siete puntos, «¿Jugamos?» sin respuesta y «Regla no dicha», rutina 7:00/8:00/2:00 con «Malestar», ocho planetas con ×8, insignias 1·2·3, barras de intensidad por rasgo, cristal con máscara «Se adapta», pestañas «En público/En casa», nodos unidos a «?» con «Diagnóstico» apagado, hojas «Primeros años/Escuela/Hoy», constelación «Un conjunto», carpetas Comunicación social/Patrones, «Su niño · Necesidades», búsqueda «etiqueta» que se borra, lista Características, «Enviar a» con contactos.
- **012 (estilo de referencias):** mapa «La reunión» (cuatro niños unidos, el niño con una flecha que se detiene en «?», adulto «Cerca de ti»; hilo: vuelve con el camino verde ✓), patio con tres juegos «¿Juegas?» y salto, batería «Confianza» 0→80 %, etiqueta «HOLA, SOY Tímido», dos caminos (Timidez/Confianza vs. tres paradas «?») con «Pueden aparecer en autismo» y «Otras explicaciones», gráfica «Comodidad social» (Reservado vs. Persistente), círculos «Tímidos»/«Espectro» «No todos», red de compañeros «¿Qué ocurre?», anillos Desarrollo social/Comunicativo, flecha roja de obligar tachada, chips «Hablar/Jugar/Otros medios», botones «Necesita tiempo/Otras dificultades» y cuadro de comentario.

## Especificación (bloque `CFG` al inicio de la línea de tiempo)
- Lienzo 1080×1920 (9:16), 30 fps; duración = fin de la última palabra de `words.json` + 2.1 s (cierre con datos; desde el 008, el 001 usó +0.1 s). Audio: `voz.mp3` de la carpeta (receta de voz: guion con CTA hablado, Eleven v3, 1.10x).
- Zonas seguras: gráficos en x 60–1020 y en el escenario (`#stage`, página y 300–1250). Subtítulos en y 1290–1440, nada gráfico ahí.
- Curvas: entradas `back.out(1.35)`, movimientos `power3.inOut`, salidas `power2.in`; sin elásticos.
- Micro-copy: ≤4 palabras por momento visual. Excepción: el aviso final «Este video orienta y no diagnostica.» + web.

## Estilo
- Fondo degradado lavanda `#C6BCE2` → rosa `#F9DEE3`, dos círculos tenues en las esquinas.
- Subtítulos palabra por palabra con los tiempos reales de `words.json`: placas ciruela, Maven Pro 58, clave en lavanda; grupos de ≤3 palabras que cortan en signo o pausa >0.45 s.
- Dibujos a dos tintas (contorno ciruela 6 px, rellenos arena, rosa, blanco), filtro `#rough`; rótulos tipo calcomanía arena.
- Enfoque: lo secundario se desenfoca (`filter: blur`) y baja opacidad mientras lo importante actúa.

## Estructura del código
- Una función por escena (`escena1()`…`escenaN()`), cada una con un comentario arriba: **Acción**, **Persisten/se transforman** e **Imagen final**.
- `at('frase', desfase, n-ésima)` da el segundo exacto de la palabra en la voz; todos los picos de movimiento usan `at()`.
- Utilidades: `POP` (entrar), `OUT` (salir), `MV` (mover), `FROM` (desde-hasta), `SPIN` (girar).

## Ejemplo de transformaciones (001)
Hoja de respuestas → tarea · barra de avance → camino · bombilla → engranaje «Comprender» → viaja al niño · niño → hoja de evaluación · chips «Fortalezas/Dificultades» → piezas del rompecabezas · rompecabezas → burbuja de comentarios. Escala: «Memoria» y «Organización» son engranajes chicos; «TDAH» es un círculo chico dentro de «Distracción».

## Pasos (`SK=.claude/skills/videos-karen`, trabajo en el scratchpad)
1. Escribir la tabla de acciones por bloque (instrucción, punto 1) con elementos nuevos (punto 10) y mostrarla antes del código.
2. `bash $SK/scripts/nuevo-hook.sh <trabajo> "hooks virales/NNN - …"` (plantilla + voz + `words.js`).
3. Reescribir objetos (`D`, `O(...)`), rótulos y las funciones de escena en `index.html`.
4. `bash $SK/scripts/previa-hook.sh <trabajo> --hoja` y revisar todas las `hoja_N.png` (un cuadro por segundo).
5. `previa-hook.sh <trabajo>` con `run_in_background` → `SendUserFile` de `previa-720.mp4`.
6. **Portada** (aprobada con el 001): editar `<trabajo>/portada.html` (viene de la plantilla) con el estilo de los gráficos: fondo lavanda→rosa, etiqueta ciruela arriba (y 250), gancho en Outfit 112 con la segunda parte en calcomanía arena girada, y abajo el dibujo clave del video (y 850–1600) con ≤2 rótulos. `bash $SK/scripts/portada.sh <trabajo>` → revisar `portada.png` → `SendUserFile`.
7. Aprobados previa y portada: `bash $SK/scripts/final-hook.sh <trabajo> "hooks virales/NNN - …"`. Hace el **bucle** (el aviso final se funde 0.5 s en la portada) y pone la portada como **primer cuadro**; guarda `video.mp4`, `portada.png` y `graficos/` (index.html, words.js, portada.html; sin gsap ni fuentes). Revisar el cierre y mandar `loop-720.mp4`.

## Revisión
- **Nada vacío:** nunca >1 s con un solo objeto o un lado vacío.
- **Nada encimado:** rótulos, íconos y subtítulos no se tocan; la ✗ va aparte del texto; ≥20 px entre objetos.
- **Pivotes:** los grupos SVG giran y escalan desde su centro (`transformOrigin:'50% 50%'`); las barras desde la izquierda.
- **Corte limpio:** cada escena sale antes de que entre la siguiente.
- El aviso «Este video orienta y no diagnostica.» y la web cierran los últimos ≈1.5 s.
- **Bucle:** el último cuadro es la portada (igual que el primero); nada debe animarse en los últimos 0.5 s del HTML.
