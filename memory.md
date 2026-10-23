# Memory — Preferencias y Aprendizajes

## Tono y comunicación

- Directo y eficiente, sin introducciones. Respuestas concisas, sin textos largos.
- Actualizar este archivo de forma proactiva cuando el usuario indique nuevas preferencias; confirmar en el chat.

## Videos de Karen

- Flujo con una aprobación por etapa (ver la skill). Orden desde el 17 oct 2026: transcripción → tabla → portada → video → copy → hecho. Cada etapa se envía y se espera su «aprobado».
- La portada va como primer cuadro del video y debe quedar entre y=300 y y=1620 (Instagram la recorta a 3:4). Ganchos cortos (≈30 caracteres máximo): los largos tapan la cara.
- Encuadre de ojos fijo en la línea del tercio superior (`encuadre.py`), sin seguimiento. El script sube el zoom solo si ella está muy abajo en el cuadro (08: 1.26).
- **Zooms:** punch-ins (1.0 ↔ 1.08, 0.3 s) en cambios de bloque solo si el zoom base es ≈1.15 (06). Con zoom base alto o ella muy cerca de la cámara, `"zooms": []` (08, 09, 10). Ante la duda, mostrar la prueba y preguntar. No usar otras transiciones.
- **Archivos de prueba:** siempre en 720p con `SendUserFile` (los de ≈70–90 MB no cargan en el visor); el guardado final es 1080p (`-crf 26`, ≈27–37 MB). No enviar un archivo hasta que el `ffmpeg` del render termine y `ffprobe` confirme la duración.
- **Identidad gráfica (17 oct 2026, pedido de Karen):** desde el 09, los videos nuevos llevan gancho, rótulo con cédula 11009616, escenas gráficas (máx. 40 % del video, 3 a 5 s cada una, transición de línea con nodo) y aviso «Este video orienta y no diagnostica.». Los 01 a 08 no se rehacen. La marca vive en `docs/marca/` del repo del portafolio. Sonido de marca: solo borrador, no usar.
- Los cambios aprobados se suben directo a `main`.

## Videos hechos (23 oct 2026)

- 01 a 05 y 07 entregados antes; 06 «Cambia la pregunta que te haces» (V8 de Drive); 08 «Otra vez sin encontrar tus llaves» (V9); 09 es el 08 con gráficos (misma toma y guion; se publica uno u otro, no ambos); 10 «Un lugar fijo para cada objeto» (V10).
- El V6 de Drive se descartó: era una regrabación del guion del 01.
- 08, 09 y 10 tratan el mismo tema (objetos que se pierden): no publicarlos seguidos.
- 11 «La hiperactividad en adultos se ve diferente» (V11, TDAH en adultos, zoom 1.15 con punch-ins; portada con cuadro de cierre sonriendo, elegido por Karen tras rechazar el primero).
- 12 «Antes de pensar en TDAH, tres preguntas» (V12, mismo tema que el 11; no publicarlos seguidos).
- 13 «3 frases que parecen ciertas sobre el TDAH» (V13, 3 mitos; mismo tema que 11 y 12, no publicarlos seguidos).
- Pendientes en Drive: **V14** (18 oct) y archivos nuevos del 21 oct: **15.1, 15.2, 16 y 17** (preguntar qué número/tema corresponde antes de asignar `NN`). Ninguno «Publicado»; cada `copy.md` trae un «Por confirmar con Karen» sin resolver.
- Antes de la etapa 1 de cada video, comparar la transcripción con los `guion.md` existentes por si es una regrabación.

- **Portadas:** si no le gusta el cuadro, mandar una hoja con 3 opciones (cuadros distintos, mismo gancho) y que elija; mirar a cámara con la boca cerrada sonriendo suele gustarle más.
- **Monitor/espera de render:** no usar `pgrep -f renderizar.sh` dentro de un bucle que mencione ese texto (se encuentra a sí mismo y nunca termina); mirar el log o `ls` del archivo final.

- **Tablas de elementos:** si Karen pide «algo nuevo» o rechaza una tabla, preguntar antes con `AskUserQuestion` (estilo, qué no convenció, protagonista, zooms) y rehacerla. En V12 aprobó: guía práctica, pastillas numeradas 1/2/3, ritmo pausado (≈14 elementos), solo 2 punch-ins y cierre con las 3 preguntas como checklist. Escenas `numero` (sin cifra de datos), `esquema` y `proceso` funcionan bien.
- Si cambia la tabla tras renderizar, se rehace el video completo y se vuelve a pedir el «aprobado».

- **Videos de mitos:** pastilla numerada por mito + escena `dividida` mito/realidad + destacados; cierre con pregunta a la audiencia (`icono: pregunta`). Si Whisper deja una frase incompleta, volver a transcribir el tramo y dejarla como la dijo, anotándola en «Por confirmar».
- **`ajustes` del spec:** la clave es el inicio con 2 decimales (`"60.60"`, no `"60.6"`).

## Repo

- Este repo se creó el 17 oct 2026 para sacar los videos del repo del portafolio (pesaban ~290 MB y ese repo es público). La skill `videos-karen` se movió aquí.
- Hecho el 17 oct 2026: se borraron `marketing/videos/` y `videos/` de todo el historial del repo del portafolio (`git filter-repo` + force-push a todas las ramas; el repo bajó de 290 MB a 21 MB). SHA anterior de `main`: `7e7b87a`. Cualquier clon antiguo del portafolio debe volver a clonarse.
- El `hyperframes check` a veces no abre el navegador («Browser session never ran», se agota el tiempo): si pasa, validar con `snapshot` y el render.
