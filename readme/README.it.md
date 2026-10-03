# Koji — JLPT Study Agent

Prepara il JLPT N5–N1 con il tuo libro, nella tua lingua. Risolvi un dubbio difficile, scegli attività adatte al tempo di oggi e riprendi da dove avevi lasciato.

## Inizia con una domanda

**In una chat AI che usi già:** carica o incolla la [guida Koji](../agent/COACH.md), poi invia la domanda. Includi la frase, le opzioni e la tua risposta quando servono. Usa un breve estratto o una foto leggibile che la chat possa elaborare.

> Segui questa guida Koji. Spiega in italiano. Ho scelto B, ma nelle soluzioni c’è C. Ecco il brano e il mio ragionamento. Perché C è più adatta?

**In Codex o Claude Code con accesso ai file:** [scarica questo repository](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip), estrailo e apri la cartella. Chiedi:

> Leggi AGENTS.md e aiutami a studiare con Koji. Spiega in italiano e scrivi i miei appunti in italiano. Ecco la mia domanda sul libro.

Puoi formulare entrambe le richieste nella tua lingua. Non servono un server Koji, un’app separata, l’installazione di Python o una chiave API del progetto. Devi poter accedere a un assistente AI capace di leggere la guida; restano validi i suoi limiti e costi.

## Oppure scegli il lavoro di oggi

Indica a Koji quale sezione del libro hai aperto e quanto tempo hai. Aggiungi il livello JLPT che vuoi raggiungere, se non è già noto.

> Sto preparando l’N3. Sono all’inizio di questa sezione di grammatica e ho 25 minuti. Aiutami a scegliere cosa studiare oggi.

Koji propone un punto di partenza, un punto di arrivo e un budget di tempo che comprende ripasso, domande e una breve conclusione. Il titolo del libro non basta a dedurne pagine o contenuti. Puoi iniziare da una sezione prima di pianificare l’intera preparazione all’esame.

## Concludi con un messaggio

> Ho finito le domande 1–4 in 18 minuti. Per la 3 mi è servito un indizio. La prossima è la 5.

Koji riassume ciò che hai fatto davvero, i punti ancora incerti e dove riprendere. Fare una domanda non conta automaticamente come errore; una risposta con un indizio rimane distinta da una risposta autonoma.

Se l’accesso ai file funziona, Koji salva e verifica il tuo stato attuale in `local/CURRENT.md`, insieme a note di sessione di supporto. In una chat normale fornisce una nota di studio breve e aggiornata, che devi salvare tu. Generare una nota non equivale a salvarla automaticamente in locale.

## Torna e continua

> Continuiamo. Oggi ho 15 minuti.

Mantieni la stessa cartella di studio oppure fornisci l’ultima nota salvata nella nuova chat. Koji usa le evidenze precedenti pertinenti per suggerire un breve ripasso e il prossimo compito sul libro. Per esempio, prima di proseguire può verificare brevemente se ora distingui senza aiuto qualcosa che avevi risolto con un indizio.

Dopo una pausa, dillo:

> Non ho studiato per una settimana. Oggi ho 10 minuti.

Koji parte dai progressi confermati e riduce il compito per adattarlo al tempo. I giorni saltati non diventano ore extra di recupero obbligatorio. Puoi anche chiedere un riepilogo settimanale, correggere un dato, esportare la nota attuale o dire «non salvare questa sessione».

## I tuoi appunti crescono con lo studio

La guida è il fermento iniziale; il tuo studio fornisce il materiale. Le spiegazioni utili che ricorrono possono diventare pagine di conoscenza collegate, separate dalle prove di ciò a cui sai rispondere. Non devi organizzare cartelle o mantenere da solo un secondo quaderno.

I file di studio restano in `local/`, escluso da Git per impostazione predefinita. Conserva questa cartella quando aggiorni Koji: sostituisci i file della guida condivisa, non i tuoi dati di apprendimento. Il salvataggio locale non implica che l’AI elabori i dati offline. Koji lavora durante le conversazioni, senza promemoria in background né sincronizzazione automatica fra copie.

Spiegazioni e appunti seguono le tue preferenze linguistiche, con esempi giapponesi e letture dei kanji. La guida è scritta in inglese. Le traduzioni del README sono generate da AI e non hanno ricevuto una revisione indipendente da madrelingua; l’edizione inglese è il riferimento.

## Lingue del README

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
