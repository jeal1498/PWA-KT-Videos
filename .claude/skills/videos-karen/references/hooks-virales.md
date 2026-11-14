# Hooks virales: referencia

Para todo video de la carpeta `hooks virales/`. Receta aprobada con el 001 (14 nov 2026). Mientras Karen no grabe, solo se hace la parte gráfica y se entrega **una previa** (no la capa inferior aparte).

## Distribución (fija, de `hooks virales/PLANTILLA-DISTRIBUCION.md`)
- 1080×1920. Arriba 45 % (0 a 864): Karen; en la previa, hueco «Zona de Karen». Abajo 55 % (864 a 1920): gráficos.
- Subtítulos sobre la costura (top 842). Escena de gráficos: tarjeta en `#card` con `top:120px` y `scale(.9)`; todo termina antes de y≈1610.

## Estilo
- **Fondo C** (el que menos cansa la vista): degradado lavanda `#C6BCE2` → rosa `#F9DEE3`, sin tarjeta con borde, dos círculos tenues en las esquinas que no pasen detrás del contenido.
- **Subtítulos** como los con cara (36): palabra por palabra con rebote, placas ciruela con letra blanca Maven Pro 54, clave en lavanda; grupos de ≤3 palabras que cortan en coma o punto.
- Dibujos a dos tintas (contorno ciruela 6 px, rellenos arena, rosa, blanco), filtro `#rough`, entradas `elastic`; rótulos tipo calcomanía arena.

## Prompt de animación (por bloque)
1. Una acción visual clara antes de animar.
2. Textos en pantalla de ≤4 palabras (sin contar subtítulos).
3. Analogías literales: el concepto se vuelve acción (bombilla que se enciende, camino que no llega a la bandera, etiquetas que se despegan, lupa sobre una caja «?», pastel con una rebanada).
4. Escala para proporciones, mirada guiada a lo importante y objetos que se transforman de una escena a otra.
5. Acción sincronizada con la palabra clave y cada escena cierra con una imagen clara.

## Pasos (`SK=.claude/skills/videos-karen`, trabajo en el scratchpad)
1. `bash $SK/scripts/nuevo-hook.sh <trabajo>` (copia la plantilla del 001).
2. En `index.html`: `SEC` = las secciones del `guión.md` con `[inicio, fin, texto]` (tiempos del guion); `at(sec,'frase')` da el segundo de esa frase. Reescribir objetos (`D`, `O(...)`) y la línea de tiempo por bloques. Sin voz, los tiempos son estimados; se reajustan al audio real cuando Karen grabe.
3. `bash $SK/scripts/previa-hook.sh <trabajo> --hoja` y revisar todos los cuadros (uno por segundo).
4. `previa-hook.sh <trabajo>` con `run_in_background` → `SendUserFile` de `previa-720.mp4`.
5. Aprobado: guardar el fuente en `hooks virales/NNN - …/graficos/index.html` (sin mp4, gsap ni fuentes).

## Revisión (auditoría del 001)
- **Nada vacío:** nunca >1 s con un solo objeto o un lado de la escena vacío; usar casillas punteadas que luego se llenan, objetos apagados que se encienden o el objeto anterior que se transforma.
- **Nada encimado:** íconos dentro de pastillas HTML van en el HTML (en el SVG quedan tapados por el fondo blanco); líneas que salen de un círculo empiezan en su borde, no en el centro; la lupa entra junto a su objetivo, no encima de otro; la ✗ va aparte, no sobre el texto; líneas divisorias cortas que no crucen rótulos; ≥20 px entre bombilla, signos y barras.
- El aviso «Este video orienta y no diagnostica.» y la web cierran los últimos 3 s.
