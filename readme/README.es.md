# Koji — JLPT Study Agent

Prepara el JLPT N5–N1 con tu propio libro y en tu idioma. Resuelve una pregunta difícil, elige tareas que encajen en tu día y retoma donde lo dejaste.

## Empieza con una pregunta

**En un chat de IA que ya uses:** sube o pega la [guía de Koji](../agent/COACH.md) y envía tu pregunta. Incluye la frase, las opciones y tu respuesta cuando hagan falta. Usa un fragmento breve o una foto legible que el chat pueda procesar.

> Sigue esta guía de Koji. Explícame en español. Elegí B, pero el solucionario dice C. Aquí están el texto y mi razonamiento. ¿Por qué es mejor C?

**En Codex o Claude Code con acceso a archivos:** [descarga este repositorio](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), descomprímelo y abre la carpeta. Pide:

> Lee AGENTS.md y ayúdame a estudiar con Koji. Explícame en español y guarda mis notas en español. Aquí está mi pregunta del libro.

Puedes escribir cualquiera de estas peticiones en tu idioma. No necesitas un servidor de Koji, una aplicación aparte, instalar Python ni una clave API del proyecto. Necesitas acceso a un asistente de IA que pueda leer la guía; sus límites y costes siguen siendo aplicables.

## O elige qué estudiar hoy

Dile a Koji qué sección del libro tienes abierta y cuánto tiempo tienes. Añade tu nivel objetivo del JLPT si aún no lo conoce.

> Estoy preparando el N3. Estoy al principio de esta sección de gramática y tengo 25 minutos. Ayúdame a elegir qué estudiar hoy.

Koji propone dónde empezar, dónde parar y un reparto del tiempo que incluye repaso, preguntas y un cierre breve. El título de un libro no basta para deducir sus páginas o contenido. Puedes empezar con una sección antes de preparar un plan para todo el examen.

## Termina con un solo mensaje

> He terminado las preguntas 1–4 en 18 minutos. Necesité una pista en la 3. La siguiente es la 5.

Koji resume lo que hiciste realmente, lo que sigue sin estar claro y dónde retomar. Hacer una pregunta no cuenta automáticamente como error; una respuesta con pista se distingue de una respuesta independiente.

Con acceso funcional a los archivos, Koji guarda y comprueba tu registro actual en `local/CURRENT.md`, junto con notas de las sesiones. En un chat normal, te entrega una nota de estudio actualizada y breve para que la guardes. Generar una nota no equivale a guardarla automáticamente en tu equipo.

## Vuelve y continúa

> Continuemos. Hoy tengo 15 minutos.

Conserva la misma carpeta de estudio o proporciona tu última nota guardada en el chat nuevo. Koji utiliza evidencias anteriores relevantes para sugerir un repaso breve y la siguiente tarea del libro. Por ejemplo, antes de avanzar puede comprobar si ahora distingues sin ayuda algo que resolviste con una pista.

Si has hecho una pausa, dilo:

> No he estudiado en una semana. Hoy tengo 10 minutos.

Koji parte del progreso confirmado y reduce la tarea para ajustarla al tiempo. Los días perdidos no se convierten en horas extra de recuperación obligatoria. También puedes pedir una revisión semanal, corregir un registro, exportar tu nota actual o decir «no guardes esta sesión».

## Tus notas crecen con tu estudio

La guía es el fermento inicial; tu estudio aporta la materia. Las explicaciones útiles que se repiten pueden convertirse en páginas de conocimiento enlazadas, separadas de las evidencias de lo que sabes responder. No tienes que organizar carpetas ni mantener otro cuaderno por tu cuenta.

Tus archivos de estudio permanecen en `local/`, excluido de Git por defecto. Conserva esta carpeta al actualizar Koji: sustituye los archivos de la guía compartida, no tus registros de aprendizaje. El almacenamiento local no significa que la IA procese sin conexión. Koji trabaja durante tus conversaciones, sin recordatorios en segundo plano ni sincronización automática entre copias.

Las explicaciones y notas siguen tus preferencias de idioma, con ejemplos en japonés y lecturas de kanji. La guía está escrita en inglés. Las traducciones del README están hechas por IA y no han recibido una revisión independiente de hablantes nativos; la versión inglesa es la referencia.

## Idiomas del README

- [English](../README.md)
- [한국어](README.ko.md)
- [日本語](README.ja.md)
- [Español](README.es.md)
- [Français](README.fr.md)
- [Deutsch](README.de.md)
- [简体中文](README.zh-CN.md)
- [繁體中文](README.zh-TW.md)
- [Português (Brasil)](README.pt-BR.md)
- [Italiano](README.it.md)
- [Русский](README.ru.md)
- [Українська](README.uk.md)
- [Polski](README.pl.md)
- [Nederlands](README.nl.md)
- [Svenska](README.sv.md)
- [Dansk](README.da.md)
- [Norsk (bokmål)](README.no.md)
- [Suomi](README.fi.md)
- [Čeština](README.cs.md)
- [Türkçe](README.tr.md)
- [Bahasa Indonesia](README.id.md)
- [Tiếng Việt](README.vi.md)
- [ไทย](README.th.md)
- [हिन्दी](README.hi.md)
- [বাংলা](README.bn.md)
- [العربية](README.ar.md)
- [فارسی](README.fa.md)
- [עברית](README.he.md)
- [Bahasa Melayu](README.ms.md)
- [Filipino](README.tl.md)
