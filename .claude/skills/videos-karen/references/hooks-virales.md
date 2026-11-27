# Hooks virales: referencia

Para todo video de la carpeta `hooks virales/`. Receta aprobada con el **001 v4 (27 nov 2026)**: Karen **no sale**; voz en off clonada (ElevenLabs) y gráficos a **pantalla completa**. Fuente de referencia: `hooks virales/001 - …/graficos/index.html` (= `plantilla-hooks/index.html`).

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

## Especificación (bloque `CFG` al inicio de la línea de tiempo)
- Lienzo 1080×1920 (9:16), 30 fps; duración = fin de la última palabra de `words.json` + 0.1 s (el 001: 60.1 s = 1803 cuadros). Audio: `voz.mp3` de la carpeta (receta de voz: guion con CTA hablado, Eleven v3, 1.10x).
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
