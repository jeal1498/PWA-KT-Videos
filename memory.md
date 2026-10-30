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

## Cómo le gusta editar (aprendido en V11 a V14)

- **Regla de trabajo:** al terminar cada video, actualizar `memory.md` y la skill con lo aprendido (preferencias, errores, trucos). No esperar a que lo pida.
- **Aprobaciones:** responde «Aprobado», «Continúa» o elige una opción por número/nombre. Si una opción es ambigua, tomar la lectura literal y decirlo en una línea.
- **Cuando rechaza una tabla** («dame algo nuevo», «más retenedor»): no repetir la anterior con retoques. Rehacerla con otra idea o preguntar antes con `AskUserQuestion`. Si pregunta «¿cuál es la diferencia?», responder con una tabla comparada corta.
- **Portada:** primero se elige el gancho entre 3 y luego el cuadro entre 3 (hoja con 3 portadas lado a lado). Prefiere cuadros con sonrisa leve o mirada serena a cámara; descartó uno hablando con la boca abierta.
- **Ritmo y retención:** quiere elementos que mantengan al espectador: gancho fuerte, algo en pantalla cada 3 a 5 s, pastillas numeradas como avance y cierre que repite los pasos. Pidió menos zooms en V12 (2 a 3) y aceptó 5 a 6 en V13 y V14.
- **Guiones:** respeta lo que Karen dice; corregir solo errores de Whisper, anotar el resto en «Por confirmar». Los videos de un mismo tema (11 a 14) llevan aviso de «no publicar seguidos».
- **Formatos que le funcionan:** guía práctica (pasos 1/2/3), mitos con escena `dividida`, mapas `esquema` y pasos `proceso`; cierre con pregunta para comentarios cuando ella la hace.
- **Respuestas:** cortas, con tabla cuando se compara o se muestra la tabla de elementos.

- **Karen visible (corrección de Eduardo en V15):** las escenas suman como máximo ≈30 % (aunque el tope duro sea 40 %) y entre escenas debe haber ≥3 s de Karen en cámara; ninguna racha de escenas pegadas debe pasar de ≈8 s. Antes de enseñar el video, correr `revisar.sh` y auditar el spec (racha sin Karen, % real con las duraciones finales). Las listas largas van como destacados sobre ella, no como escena.
- **Fusión de tomas (V15):** cuando Karen manda dos tomas del mismo guion y quiere «lo mejor de cada una»: transcribir ambas, elegir frase por frase (menos errores, mejor pausa, frase completa), minimizar los cambios de toma (2 fue lo ideal) y taparlos con escenas a pantalla completa porque el fondo cambia (seto verde / pared blanca). Se usa `scripts/fusionar.py`; encuadre por toma con `encuadre.py`; cortes en pausas con fundidos de 30 ms.
- **Portada de un video sin TDAH:** pedir/confirmar la etiqueta («Consejo de bienestar»). Eduardo prefiere ganchos muy cortos (≤25 caracteres) que llamen la atención («¿Qué me pasa?») y rechaza cuadros hablando con la boca abierta; si rechaza las 3 opciones, revisar ≈28 cuadros en una hoja y proponer otros 3.
- **Etiquetas de escena:** `servicio: adultos` pinta «TDAH ADULTOS»; usar `informativo` en videos que no hablan de TDAH.
- **Esperas:** no usar `pgrep -f` con un texto que aparezca en el propio comando del bucle; guardar el PID del script (`pgrep -f "^bash …/renderizar.sh"`) y esperar con `kill -0`.

- **Tomas con encuadre cercano (V16):** ella casi llena el cuadro aunque el zoom base sea 1.15; se pregunta y, si Eduardo dice sin zooms, `"zooms": []`. Con cámara cercana, todos los elementos van fuera de la cara (gancho arriba, cierre abajo).
- **Cierre:** que el aviso «Este video orienta y no diagnostica.» se vea ≥3 s: `url_en` ≈4 s antes del final (el aviso entra 0.1 s después) y chips cortos (≤3 palabras) para que no se parta en 3 líneas y choque con el subtítulo.
- **Anclas de `componer.py`:** la palabra buscada debe empezar *después* del tiempo dado; usar 0.1 a 0.3 s antes (por redondeos) y sin puntuación. Whisper puede saltarse palabras tras una pausa: volver a transcribir ese tramo y parchar `words.json`.
- **Etiquetas de `dividida`:** que se lean bien al decirlas (`Antes/Después`, `Elige/Sin convertirla`), no «De/A».
- **Portada rechazada dos veces (V15, V16):** Eduardo prefiere cuadros con sonrisa hablando o mirada abierta a cámara; mostrar 3 nuevos con una hoja de ≈24 cuadros revisada por mí.

- **Datos de Whisper a revisar siempre:** género/número que no concuerdan («rutina… lo abandonas») se dejan como suenan y se anotan; imperativo «revise» vs «revisa» se unifica con el trato de «tú» del video; frases con preguntas se puntúan con signos (`ajustes` con «¿Te», «ayuda?»).
- **Cierre de la serie V11 a V17:** los 7 videos son de TDAH adulto, rutinas y bienestar; avisar siempre qué videos se parecen para no publicarlos seguidos y proponer orden de subida si lo piden.

- **Calendario y página (23 oct 2026):** `index.html` + `web/data.json` (los genera `python3 -I scripts/exportar_web.py` desde `calendario.md` y cada `copy.md`; correrlo y commitear `web/` cada vez que cambie una fecha o un copy). Orden de subida aceptado por Eduardo para 11 a 17: **11, 16, 13, 17, 12, 15, 14** (25 a 31 oct); la numeración de carpetas no cambia, solo las fechas. Al terminar un video nuevo: guardar con `guardar.sh`, correr `exportar_web.py`, agregar su fila (descarga + copy IG/FB, TikTok, hashtags y título de YouTube, sacados de su `copy.md`) a `tabla-publicacion.md` y commitear `web/` en el mismo push.

## Videos hechos (23 oct 2026)

- 01 a 05 y 07 entregados antes; 06 «Cambia la pregunta que te haces» (V8 de Drive); 08 «Otra vez sin encontrar tus llaves» (V9); 09 es el 08 con gráficos (misma toma y guion; se publica uno u otro, no ambos); 10 «Un lugar fijo para cada objeto» (V10).
- El V6 de Drive se descartó: era una regrabación del guion del 01.
- 08, 09 y 10 tratan el mismo tema (objetos que se pierden): no publicarlos seguidos.
- 11 «La hiperactividad en adultos se ve diferente» (V11, TDAH en adultos, zoom 1.15 con punch-ins; portada con cuadro de cierre sonriendo, elegido por Karen tras rechazar el primero).
- 12 «Antes de pensar en TDAH, tres preguntas» (V12, mismo tema que el 11; no publicarlos seguidos).
- 13 «3 frases que parecen ciertas sobre el TDAH» (V13, 3 mitos; mismo tema que 11 y 12, no publicarlos seguidos).
- 14 «Esto explica toda mi vida» (V14; toca el mito 3 del 13, no publicarlos seguidos).
- 15 «Qué me pasa, cambia la pregunta» (V15 = fusión de 15.1 y 15.2; no habla de TDAH; parecido al 06, no publicarlos seguidos).
- 16 «Sientes que no avanzas, 3 preguntas» (V16; ubicación nueva con sofá morado, encuadre cercano y sin zooms aprobado por Eduardo; parecido a 12, 14 y 15).
- 17 «Abandonas tu rutina, 3 ideas» (V17; encuadre cercano y sin zooms, mismo estilo de guía numerada que 12, 14 y 16).
- **Todos los pendientes de Drive (V11 a V17) están hechos.** Antes de empezar otro video, listar la carpeta con `pageSize` alto y buscar archivos nuevos.
- Pendientes anteriores: ninguno (preguntar qué número/tema corresponde antes de asignar `NN`). Ninguno «Publicado»; cada `copy.md` trae un «Por confirmar con Karen» sin resolver.
- Antes de la etapa 1 de cada video, comparar la transcripción con los `guion.md` existentes por si es una regrabación.

- **Portadas:** si no le gusta el cuadro, mandar una hoja con 3 opciones (cuadros distintos, mismo gancho) y que elija; mirar a cámara con la boca cerrada sonriendo suele gustarle más.
- **Monitor/espera de render:** no usar `pgrep -f renderizar.sh` dentro de un bucle que mencione ese texto (se encuentra a sí mismo y nunca termina); mirar el log o `ls` del archivo final.

- **Tablas de elementos:** si Karen pide «algo nuevo» o rechaza una tabla, preguntar antes con `AskUserQuestion` (estilo, qué no convenció, protagonista, zooms) y rehacerla. En V12 aprobó: guía práctica, pastillas numeradas 1/2/3, ritmo pausado (≈14 elementos), solo 2 punch-ins y cierre con las 3 preguntas como checklist. Escenas `numero` (sin cifra de datos), `esquema` y `proceso` funcionan bien.
- Si cambia la tabla tras renderizar, se rehace el video completo y se vuelve a pedir el «aprobado».

- **Videos de mitos:** pastilla numerada por mito + escena `dividida` mito/realidad + destacados; cierre con pregunta a la audiencia (`icono: pregunta`). Si Whisper deja una frase incompleta, volver a transcribir el tramo y dejarla como la dijo, anotándola en «Por confirmar».
- **`ajustes` del spec:** la clave es el inicio con 2 decimales (`"60.60"`, no `"60.6"`).

- **Más retención (pedido en V14):** una escena mito/realidad en los primeros 5 a 9 s, pastillas numeradas 1/2/3 como avance, sin huecos de más de 2 s sin elemento en pantalla, destacados cortos y cierre que repite los pasos. Se ofrecen opciones con `AskUserQuestion` o una tabla comparada («cuál es la diferencia») antes de aprobar. «Opción 2» = la segunda de las que se listaron.
- Si dice «Continúa» ante una tabla o texto, se toma como aprobación y se avisa.
- El `renderizar.sh` termina antes que su `ffmpeg` final en el log: esperar al PID de `ffmpeg` y confirmar con `ffprobe`.

## Repo

- Este repo se creó el 17 oct 2026 para sacar los videos del repo del portafolio (pesaban ~290 MB y ese repo es público). La skill `videos-karen` se movió aquí.
- Hecho el 17 oct 2026: se borraron `marketing/videos/` y `videos/` de todo el historial del repo del portafolio (`git filter-repo` + force-push a todas las ramas; el repo bajó de 290 MB a 21 MB). SHA anterior de `main`: `7e7b87a`. Cualquier clon antiguo del portafolio debe volver a clonarse.
- El `hyperframes check` a veces no abre el navegador («Browser session never ran», se agota el tiempo): si pasa, validar con `snapshot` y el render.

## V20 → video 18 (27 oct 2026)

- 18 «¿Y si no era ansiedad?» (V20 de Drive, `20.mp4`, video respuesta a una pregunta sobre el 11; se sube el 27 oct). Encuadre cercano, sin zooms, 5 escenas (27 %). Parecido a 11 a 14: no publicarlo seguido. Fecha del 18 y del 13 coinciden (27 oct): Eduardo decide.
- Eduardo pide al terminar: actualizar la página (`exportar_web.py` + fila en `tabla-publicacion.md`) en el mismo flujo, sin esperar a que lo repita. Cuando avisa «se sube hoy», poner esa fecha en `calendario.md`.
- Portada: el gancho B («¿Y si no era {ansiedad}?», frase de ella) gustó; rechazó los 3 primeros cuadros y eligió el de sonrisa abierta (87.8 s, cierre del video). Los mejores cuadros suelen estar al final, cuando sonríe al despedirse.
- `ficha` con `titulo` largo se desborda: usar `titulo_tam` 86 desde el principio.
- Un master de 1080p sale a ≈66 MB y con la portada ≈87 MB: recomprimir a `-crf 28 -preset medium` (≈25 MB) antes de `guardar.sh`.
- `check` volvió a fallar sin navegador; `snapshot` basta. `encuadre.py` necesitó reinstalar mediapipe/opencv y las libs de apt.

## Versiones v2 sin cara (27 oct 2026, piloto con el 18)

- **Qué es:** por cada video pendiente (09 a 18) se hace una v2 sin la cara de Karen, para prueba A/B: **guion nuevo** (mismo tema, otro gancho, otros ejemplos), 100 % animación y voz clonada de Karen en ElevenLabs. Mientras no esté su voz, la provisional es la de Checa (Fernando Martínez, `dlGxemPxFMTY7iXagmOj`, velocidad 1.0), solo para pruebas.
- **Estilo elegido:** «propuesta 3, dibujo a dos tintas»: rellenos planos lavanda, rosa y arena con contorno ciruela profundo, trazo que vibra 12 veces por segundo (feTurbulence + feDisplacementMap), entradas con rebote elástico y palabras clave como calcomanía (arena, inclinada −2.5°, sombra lavanda). Textos fuera del filtro para que se lean limpios.
- **Personaje:** Open Peeps de DiceBear (CC0, sin atribución), `seed: 'Mar'`, `head: long`, piel arena, ropa lavanda, trazo ciruela. **Solo aparece donde suma** (gancho, momentos emocionales, cierre); el resto son gráficos. Cambia de cara en cada giro del guion (Preocupada → Tranquila). Sin manos: los gestos se hacen con movimiento.
- **No dibujar personajes a mano en SVG:** salieron feos tres veces. Usar una librería ilustrada y recolorear. Trampas: cada avatar necesita ids con prefijo (comparten `viewboxMask`) y no recolorear el blanco de dentro de `<mask>`.
- **Render:** HyperFrames (`npx hyperframes@0.8.163 render`), el audio se pega después con ffmpeg. Propuestas de estilo en clips de ≤6 s antes de hacer el video completo.
- **Voz clonada de Karen (30 oct 2026):** ElevenLabs `sSQiAF9Uq1K3xnyvFi8w`, ya en `VOZ_KAREN` de `voz.py`. El 19 se regeneró con ella.
- **Personaje (27 oct 2026):** se queda el genérico. Se probó un avatar de Karen en el mismo estilo (cabello a los hombros, sonrisa con dientes y labios rojos); está guardado en `avatar-karen.cjs` pero no se usa por ahora.
- **Audio Tags (30 oct 2026):** a Eduardo le gustó más la voz en Eleven v3 con tags, pero con los silencios recortados (máx. 0.35 s). Pocos tags, solo en giros emocionales. Antes de rehacer todo, prueba corta con comparación.

### ✅ Receta aprobada por Karen (30 oct 2026): así se hacen los videos de ahora en adelante

Karen vio el 19 y le gustó mucho. Las siguientes v2 (09 a 17) y los videos nuevos sin cara se hacen igual, sin volver a proponer estilos ni voces:
1. **Guion nuevo** del tema (≈190 palabras, ≈80 s) → aprobación.
2. **Voz de Karen en Eleven v3** con 4 a 6 Audio Tags solo en giros emocionales (`[pause]`, `[sighs]`, `[curious]`, `[softly]`, `[warmly]`) y silencios recortados: `voz.py guion.txt <trabajo> --modelo v3 --max-silencio 0.35`.
3. **Animación a dos tintas** (HyperFrames) con el personaje genérico solo donde suma, como en `v2-sin-cara/ejemplo-19/`.
4. Portada, copy y guardado con el flujo de siempre (una aprobación por etapa).
Todo el detalle está en `.claude/skills/videos-karen/v2-sin-cara/README.md`.
- **Calendario intercalado (30 oct 2026, Karen):** un día video sin cara (v2), al día siguiente video con Karen, y así. El 19 se sube el sáb 31 oct. Al planear fechas o el orden de las v2, respetar la alternancia (y que dos videos seguidos no repitan tema).
- **Publicados (30 oct 2026):** Karen ya subió todos los videos hasta el 18. Siguen: el 19 (sáb 31 oct, sin cara) y lo nuevo. Los días con Karen necesitan videos que ella grabe; las v2 sin cara salen de los temas 09 al 17.

### ⏳ PENDIENTE: hacer la v2 (sin cara) de TODOS los videos hechos hasta ahora

Pedido de Eduardo el 30 oct 2026. Con la receta aprobada (guion nuevo, voz de Karen en Eleven v3 con tags y silencios recortados, animación a dos tintas; ver `.claude/skills/videos-karen/v2-sin-cara/README.md`).

| Video original | v2 |
|---|---|
| 01 Organiza tus pendientes | pendiente |
| 02 No todo olvido es TDAH | pendiente |
| 03 Solo una tarea, no diez | pendiente |
| 04 10 minutos que se vuelven una hora | **hecha: es el 20** (plan lun 2 nov 2026) |
| 05 Planifica tu salida | pendiente |
| 06 Cambia la pregunta que te haces | pendiente |
| 07 Reducir todo a flojera no ayuda | **hecha: es el 21** (plan mar 4 nov 2026) |
| 08 Otra vez sin encontrar tus llaves (el 09 es el 08 con gráficos) | pendiente |
| 10 Un lugar fijo para cada objeto | pendiente |
| 11 La hiperactividad en adultos se ve diferente | pendiente |
| 12 Antes de pensar en TDAH, tres preguntas | pendiente |
| 13 3 frases que parecen ciertas sobre el TDAH | pendiente |
| 14 Esto explica toda mi vida | pendiente |
| 15 Qué me pasa, cambia la pregunta | pendiente |
| 16 Sientes que no avanzas, 3 preguntas | pendiente |
| 17 Abandonas tu rutina, 3 ideas | pendiente |
| 18 Y si no era ansiedad | **hecha: es el 19** |

- Cada v2 lleva su propio número (desde el 20) y su `guion.md` dice de qué video viene.
- Van en los días **sin cara** del calendario intercalado (un día sin cara, al siguiente con Karen).
- Al terminar cada una: marcar «hecha» aquí con su número.

- **v2 del 04 = video 20 «Solo voy a revisar un mensaje»** (30 oct 2026, hecho, plan lun 2 nov): receta aprobada de principio a fin, una aprobación por etapa. Fuente reutilizable en `v2-sin-cara/ejemplo-20/` (`build.py` con `sc()`, `anim.js`, `avs.json`; caras: awe, tired, hectic, suspicious, calm, smile). Render ≈6 min; `snapshot` con 22 tiempos revisa todo. Con tiempos directos, `warp.json` es identidad `[[0,0],[100,100]]`. Portada hecha en HTML + Playwright (`portada.py` es solo con foto). Tras revisar el snapshot, subir los textos `.q` si tapan el avatar. El `guardar.sh` empuja a `main`: en esta rama se guardó a mano. Siguen las v2 de 01 a 03, 05 a 08 y 10 a 17.
- **Avance v2 (30 oct 2026):** 2 de 17 hechas (19 = v2 del 18; 20 = v2 del 04). Faltan 15: 01, 02, 03, 05, 06, 07, 08, 10, 11, 12, 13, 14, 15, 16, 17. Calendario: 31 oct = 19, 1 nov = Karen, 2 nov = 20, 3 nov = Karen, 4 nov = siguiente v2 (número 21).
- **v2 del 07 = video 21 «Querer y arrancar no son lo mismo»** (30 oct 2026, hecho, plan mar 4 nov). Avance: 3 de 17 hechas (19, 20, 21); faltan 14: 01, 02, 03, 05, 06, 08, 10, 11, 12, 13, 14, 15, 16, 17. Fuente en `v2-sin-cara/ejemplo-21/`.
- **Lecciones del 21 (Eduardo):** (1) **No abrir el guion con `[pause]`**: un video no empieza en silencio. (2) **Sin cuadros vacíos:** en cada escena entran elementos desde el principio (tarjetas atenuadas que se encienden al decirlas, burbujas que se sustituyen); nunca más de ≈1.5 s con solo el título. Revisar con `snapshot` cada ≈3 s, sobre todo justo después del título de cada escena. (3) Revisar signos en portada (salió «=» donde iba «≠»).
