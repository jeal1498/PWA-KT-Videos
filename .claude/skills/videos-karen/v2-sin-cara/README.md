# Videos v2 sin cara (versión B para prueba A/B)

Aprobado por Eduardo el 27 oct 2026 con el 19 (v2 del 18). Se repite igual para las v2 del 09 al 17.

**Qué es:** el mismo tema de un video ya hecho, con **guion nuevo** (otro gancho, otros ejemplos, otra estructura), sin la cara de Karen: 100 % animación a dos tintas y voz clonada de Karen. Lleva su propio número y carpeta (`19 - … (v2 sin cara)`), y su `guion.md` dice de qué video viene. No publicarla seguida de su versión A.

## Flujo (las mismas etapas con una aprobación cada una)

1. **Guion nuevo** (etapa 1): escribirlo en el chat (≈190 palabras ≈ 75 s), con «Cómo se diferencia del original» en 4 líneas y «Por confirmar con Karen» (ejemplos que ella no dijo). Respetar las reglas de siempre: orienta, no diagnostica.
2. **Voz:** `python3 -I voz.py guion.txt <trabajo>` → `voz.mp3` y `words.json` con tiempos por palabra (ElevenLabs *with-timestamps*; la clave `ELEVENLABS_API_KEY` no tiene permiso de *speech-to-text*). Voz de Karen: pasar su `voice_id` como tercer argumento. **Mientras no esté, provisional = Fernando Martínez** (`dlGxemPxFMTY7iXagmOj`, la voz de Checa) y se marca en el copy.
3. **Tabla de elementos** (etapa 2): `Segundo · Frase · Escena · Personaje`, con los tiempos de `words.json`. Escenas de 3 a 7 s, una idea cada una.
4. **Portada** (etapa 3): 3 ganchos, eligen uno; tipográfica con ilustración (sin cuadro de Karen), zona segura y=300–1620.
5. **Video** (etapa 4): copiar `ejemplo-19/` a la carpeta de trabajo, cambiar escenas en `build.py` y tiempos en `anim.js`, generar las caras con `avatares.cjs` (el 19 usa `avs.json duda:suspicious preocupada:concerned tranquila:calm sonrisa:smile preocupada2:concerned sonrisa2:smile`; una clave por aparición), y:
   ```
   python3 build.py                                  # → public/index.html
   npx --yes hyperframes@0.8.163 snapshot public --at t1,t2,…   # revisar la hoja
   npx --yes hyperframes@0.8.163 render public --fps 30 -o mudo.mp4   # ≈9 min por 75 s; no cortar su salida con | head
   ffmpeg -i mudo.mp4 -i voz.mp3 -t <dur> -c:v copy -c:a aac -b:a 160k -movflags +faststart master.mp4
   bash ../scripts/portada_primer_cuadro.sh master.mp4 portada.png final.mp4   # ≈17 MB
   ```
   `public/` lleva `gsap.min.js` y `fonts/` (de `assets/`). Prueba en 720p con `SendUserFile`.
6. **Copy** (etapa 5) con la plantilla de siempre; en «Relación»: «Versión B del NN para prueba A/B». En «Por confirmar»: voz provisional, guion del editor y el personaje ilustrado.
7. **Hecho** (etapa 6): carpeta, calendario («por definir»), `tabla-publicacion.md` y `exportar_web.py`, en un solo commit.
8. **Cuando llegue la voz de Karen:** regenerar con `voz.py … <voice_id>`, ajustar en `anim.js` los tiempos que se muevan (revisar con `snapshot`), volver a renderizar y reemplazar `video.mp4` de la carpeta (un commit).

## Estilo «dos tintas» (propuesta 3, elegida por Karen y Eduardo)

- **Gráficos:** rellenos planos lavanda `#C6BCE2`, rosa `#F9DEE3` y arena `#F5E7D6` con contorno ciruela profundo `#2E2545` de 6 a 8 px; check en verde `#10b77f`. Fondo ciruela con resplandor radial, viñeta y garabatos (destellos y ondas) que se mecen.
- **Trazo que vibra:** filtro `#rough` (`feTurbulence` + `feDisplacementMap` escala 6) con la semilla cambiando 12 veces por segundo. Los textos van **fuera** del filtro.
- **Movimiento:** entradas con `elastic.out(1,0.55)`, ramas y líneas que se dibujan, la nube se revienta en burbujas. Palabras clave como **calcomanía**: arena, inclinada −2.5°, sombra lavanda `7px 8px`.
- **Transición:** la línea con nodo de la marca, hecha a mano, entre escenas.
- **Personaje:** Open Peeps de DiceBear (CC0, sin atribución), `seed: 'Mar'`, `head: long`. **Solo donde suma:** gancho, momentos emocionales y cierre (4 de 13 escenas en el 19). Cambia de cara en cada giro del guion (cruce de 0.25 s entre dos avatares). Sin manos: gestos con movimiento (asentir, negar, inclinar, temblar, respirar, rebote).
- **Caras útiles:** problema → `concerned`, `concernedFear`, `fear`, `hectic`, `tired`; duda → `suspicious`, `solemn`, `blank`, `serious`; «¡ah!» → `awe`, `driven`; solución → `calm`, `smile`, `smileBig`, `eyesClosed`; explicar → `explaining`.

## Trampas que ya costaron tiempo

- **No dibujar personajes a mano en SVG**: salieron feos tres veces. Librería ilustrada y recolorear.
- En HTML, un atributo sin comillas pegado a `/>` (`opacity=.55/>`) deja el elemento abierto y se traga todo lo que sigue: **siempre comillas**.
- Dos elementos con el mismo `id` en la página (por ejemplo la línea de transición y una rama) se pisan las animaciones.
- En GSAP, `fromTo` muestra su estado inicial desde el cuadro 0 (`immediateRender`): para algo que aparece después, `immediateRender:false`.
- `page.evaluate(()=>tl.seek(t))` sin llaves intenta serializar el timeline y se cuelga; con HyperFrames no hace falta.
