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
