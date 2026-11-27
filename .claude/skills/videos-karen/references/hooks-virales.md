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
1. Escribir la tabla de acciones por bloque (instrucción, punto 1) y mostrarla antes del código.
2. `bash $SK/scripts/nuevo-hook.sh <trabajo> "hooks virales/NNN - …"` (plantilla + voz + `words.js`).
3. Reescribir objetos (`D`, `O(...)`), rótulos y las funciones de escena en `index.html`.
4. `bash $SK/scripts/previa-hook.sh <trabajo> --hoja` y revisar todas las `hoja_N.png` (un cuadro por segundo).
5. `previa-hook.sh <trabajo>` con `run_in_background` → `SendUserFile` de `previa-720.mp4`.
6. Aprobado: guardar `index.html` y `words.js` en `hooks virales/NNN - …/graficos/` (sin mp4, gsap ni fuentes).

## Revisión
- **Nada vacío:** nunca >1 s con un solo objeto o un lado vacío.
- **Nada encimado:** rótulos, íconos y subtítulos no se tocan; la ✗ va aparte del texto; ≥20 px entre objetos.
- **Pivotes:** los grupos SVG giran y escalan desde su centro (`transformOrigin:'50% 50%'`); las barras desde la izquierda.
- **Corte limpio:** cada escena sale antes de que entre la siguiente.
- El aviso «Este video orienta y no diagnostica.» y la web cierran los últimos ≈1.5 s.
