# Videos grabados por Karen (con cara): referencia

Leer solo cuando haya un video nuevo de Karen en Drive. El estilo no cambia: subtítulos sobrios, tarjetas por idea, escenas gráficas y cierre sobrio. Desde el 09 llevan gancho, rótulo con cédula 11009616, escenas y aviso; los 01 a 08 no se rehacen.

## Pasos (`SK=.claude/skills/videos-karen`, trabajo en el scratchpad)
1. **Preparar** (≈4 min): `bash $SK/scripts/preparar.sh <original.mp4> <trabajo>`. Recodifica a 1080×1920 (respeta la rotación), nivela a −16 LUFS y transcribe con Whisper *medium* (`words.json`). Usar el original de Drive, no el de WhatsApp (viene a 386×686).
2. **Encuadre de ojos:** `python3 $SK/scripts/encuadre.py <trabajo>`. Zoom fijo 1.15 con los ojos en el tercio superior, sin seguimiento; revisar `tercios.png`. Una vez por entorno: `pip install mediapipe opencv-python-headless`, `apt-get update && apt-get install -y libegl1 libgles2 libgl1`.
3. **Revisar la transcripción:** comparar con los `guion.md` existentes (el V6 de Drive era una regrabación del 01). Corregir solo errores de Whisper; lo demás va a «Por confirmar». Si hay un hueco largo entre palabras, volver a transcribir el tramo (`vad_filter=False`, `condition_on_previous_text=False`, audio como arreglo numpy) y parchar `words.json`. Concordancias raras se dejan como suenan y se anotan; el imperativo se unifica con el «tú» del video; preguntas con signos.
4. **Spec** (partir de `ejemplos/video17-spec.json`; todos los tipos de escena en `ejemplos/video-escenas-spec.json`) → `python3 $SK/scripts/componer.py <trabajo> spec.json` → `public/index.html` y `subtitulos.json`.
5. **Portada** con foto: `python3 $SK/scripts/portada.py --estilo 1 --video <trabajo>/public/input-video.mp4 --tiempo <s> --hook "Frase con {palabra}" --sub "…" --tag "Consejo para TDAH" --salida <trabajo>/portada.png`. Los mejores cuadros suelen estar al final (sonrisa de despedida); evitar la boca abierta. Si no gusta, hoja con 3 cuadros nuevos.
6. **Vistazo, render y QC:** `armar.sh <trabajo> --vistazo`, luego `armar.sh <trabajo>` en segundo plano, `copy.py` y `qc.py <trabajo>`.
7. **Dos tomas del mismo guion:** transcribir ambas, elegir frase por frase con pocos cambios de toma (2 es lo ideal), `scripts/fusionar.py` (cortes en pausas, fundidos de 30 ms), encuadre por toma y tapar los cambios con escenas a pantalla completa si cambia el fondo.

## Elementos del spec
- `pastillas` (con `n` numeradas o sin `n` como etiqueta), `antes_despues` (`etiquetas`, `tachar:false`), `alarma` (también temporizador), `listas` (chips por palabra), `destacados`, `cierre` (`icono:"pregunta"` o bookmark, `chips_anclas`, `titulo_tam`, `url_en`, `aviso`), `zooms`, `gancho` (`texto`, `ini`, `fin`; placa arriba en y=300), `nametag.cedula`.
- `escenas`: `ficha` (`titulo`, `texto`, `etiqueta`, `icono`, `titulo_tam` 86), `lista`, `dividida` (`mito`, `realidad`, `etiqueta_mito`, `etiqueta_realidad`; etiquetas que se lean al decirlas, como «Antes/Después»), `proceso` (pasos anclados dentro de 5 s; si están separados ≈15 s, usar pastillas), `numero` (solo cifras reales: 5.0 y 18 reseñas; sin cuenta animada), `esquema` (máx. 4 nodos). `servicio`: `infantil`, `autismo`, `adultos` (pinta «TDAH ADULTOS») o `informativo` para videos sin TDAH.
- **Anclas:** `["escribe", 22]` = primera «escribe» que empieza después de 22 s; usar 0.1 a 0.3 s antes y la palabra sin puntuación.
- `ajustes`: `{"16.46": "acercar", "16.72": null}`; la clave es el inicio con 2 decimales (`"60.60"`). Números dictados «1.» → «Uno.».
- La duración del spec es la de `input-video.mp4` (ffprobe), no la de la última palabra.

## Reglas de composición
- **Karen visible:** escenas ≤≈30 % del video, ≥3 s de Karen entre escenas, ninguna racha de escenas de más de ≈8 s. Listas largas como destacados sobre ella. Escenas de 3 a 5 s, una idea, ≤12 palabras.
- Tarjetas en y≈1050 a 1380, entran justo antes de su primer elemento y no se solapan; el rótulo (0.5 a ≈3 s) no coincide con una tarjeta ni el gancho con una pastilla.
- **Zooms:** punch-ins 1.0↔1.08 en 0.3 s en cambios de bloque solo si el zoom base es ≈1.15; con zoom base alto o ella cerca de la cámara, `"zooms": []`. Con cámara cercana, todo fuera de la cara (gancho arriba, cierre abajo). Ante la duda, preguntar.
- **Retención:** gancho fuerte, algo en pantalla cada 3 a 5 s, sin huecos de más de 2 s, pastillas 1/2/3, una escena mito/realidad en los primeros 5 a 9 s si aplica, cierre que repite los pasos y pregunta cuando ella la hace.
- **Cierre:** `url_en` ≈4 s antes del final para que el aviso se vea ≥3 s; chips de ≤3 palabras.
- Ganchos de portada de ≤30 caracteres (los largos tapan la cara), de lo que ella dice; sin «siempre» ni «todos».
- Sonido de marca: solo borrador, no usar.

## Estilo aprobado con el 36 (12 nov 2026): aplicarlo a los videos con cara
Orden: `preparar.sh` → `encuadre.py` → spec → `recortar.py` → `color.sh` → animación → `componer.py` → vistazo cada 1 s → render.
- **Subtítulos palabra por palabra** con rebote: `"subs_palabra": true` en el spec.
- **Layout dividido:** `"layout": "split"`. Gráficos arriba (escenario lavanda de y≈330 a 900), Karen abajo y subtítulos en la costura. El gancho va encima del escenario; el cierre sube a la zona de gráficos.
- **Escenario animado por bloques** (`"custom"`): una acción visual por bloque, máximo 4 palabras en pantalla, analogías dibujadas literal (embudo que se atasca, carriles, compuerta, pared, dominós), escala para magnitudes y los mismos objetos que se transforman entre bloques. Ejemplo completo en `ejemplos/video36-bloques.py`. La zona de gráficos nunca se queda vacía más de ≈1 s; cada bloque con su zoom (`ZM`) para llenar el escenario.
- **Silencios:** `recortar.py` corta toda pausa de más de 0.5 s (deja 0.15 s por lado) y remapea spec, palabras y anclas; tramos donde ella calla sonriendo van en `--extra`. El 36 bajó de 83.5 a 74.3 s.
- **Color grading:** `color.sh <trabajo>` aplica `assets/karen.cube` (de `grade.py`) solo al video de ella. Correctivo primero: camisa blanca neutra, piel ≈67 % de luz sobre la línea de piel (≈123 a 125° en el vectorescopio), curva suave con hombro en blancos, fondo morado y turquesa un poco menos saturado, sombras con un toque ciruela. Nada de viñeta, afilado ni saturación general (Karen rechazó ese primer intento). Revisar con `scopes.py`. La portada se hace con `--foto` de un cuadro con el mismo LUT.
- Opción más simple, sin escenario: `"referencias"` (iconos de `REF` en tarjeta arena junto a ella).

## Trampas técnicas (36)
- GSAP en SVG gira y escala desde la esquina superior izquierda: poner `transformOrigin:'50% 50%'` (el ejemplo lo hace con `.zo`). Para pivotes exactos (dominós) animar el atributo `transform` con `attr:{transform:'translate(x y) rotate(a)'}`.
- Física creíble (cosas que caen, se apilan o se atoran): calcularla (posiciones tangentes, simulación cuadro a cuadro con `shapely`) y no a ojo; si no, «vuelan» o se enciman.
- Los trazos con `stroke-dasharray` dejan un punto visible antes de dibujarse: `opacity:0` hasta que empieza el `DRAW`.
- Correr los scripts con `python3 -I`: sin `-I`, el `copy.py` de `scripts/` tapa el módulo `copy` de Python y cualquier script que importe numpy falla con el uso de `copy.py`.
- `encuadre.py` (mediapipe) necesita `apt-get update && apt-get install -y libegl1 libgles2 libgl1`.
- Antes de entregar: `armar.sh <trabajo> --vistazo 1` y revisar todas las hojas (huecos, encimados, cortes en bordes, objetos flotando).
