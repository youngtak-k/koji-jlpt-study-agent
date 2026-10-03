# Koji — JLPT Study Agent

用自己的教材、自己熟悉的語言準備 JLPT N5–N1。解決難題，選擇適合今天時間的學習任務，下次從上次停下的地方繼續。

## 從一個問題開始

**在現有的 AI 聊天中：** 上傳或貼上 [Koji 指南](../agent/COACH.md)，接著傳送問題。需要時附上相關句子、選項和你的答案。可以使用簡短摘錄，或聊天工具能夠處理的清晰照片。

> 請遵循這份 Koji 指南，用繁體中文解釋。我選了 B，但答案是 C。這是原文和我的思路，為什麼 C 更合適？

**在可以存取檔案的 Codex 或 Claude Code 中：** [下載此儲存庫](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip)，解壓縮並開啟資料夾，然後說：

> 請閱讀 AGENTS.md，幫我用 Koji 學習。用繁體中文解釋，也用繁體中文記錄我的筆記。這是我對教材的問題。

兩種請求都可以用你自己的語言表達。不需要 Koji 伺服器、獨立應用程式、安裝 Python 或專案 API 金鑰。你需要能夠使用可讀取指南的 AI 助理；該服務的使用額度與費用仍然適用。

## 或者選擇今天的學習任務

告訴 Koji 你翻到教材的哪個部分，以及有多少時間。如果還不知道你的 JLPT 目標級別，也一起說明。

> 我在準備 N3，剛開始這一節文法，今天有 25 分鐘。幫我選一下今天學什麼。

Koji 會提出起點、終點和時間安排，其中包括複習、提問和簡短總結。僅憑書名無法推斷頁碼或內容。你可以先從一個小節開始，再制定完整的備考計畫。

## 用一則訊息結束

> 我用了 18 分鐘做完第 1–4 題。第 3 題需要提示。下次從第 5 題開始。

Koji 會總結實際完成的學習、尚不確定的地方和下次的起點。提問不會自動算作答錯；在提示下答對與獨立答對會分別記錄。

檔案存取正常時，Koji 會將目前記錄儲存至 `local/CURRENT.md` 並檢查儲存結果，同時保留補充的學習工作階段筆記。在一般聊天中，它會給你一份精簡的更新版學習筆記，由你自行儲存。產生筆記不代表已自動儲存到本機。

## 回來繼續學習

> 繼續吧，今天我有 15 分鐘。

保留同一個學習資料夾，或在新聊天中提供最近儲存的筆記。Koji 會利用相關的歷史依據，建議簡短複習和下一項教材任務。例如，之前靠提示才分清的差異，可以在進入新內容前簡短確認一次，看能否獨立作答。

中斷學習後，直接說明：

> 我一週沒學了，今天有 10 分鐘。

Koji 會從已確認的進度開始，縮小任務以配合時間。漏學的日子不會變成強制補課的額外時數。你也可以請求每週回顧、修正記錄、匯出目前筆記，或者說「這次學習不要儲存」。

## 筆記隨學習一起成長

指南是發酵的種麴，學習提供原料。反覆有用的解釋可以變成相互連結的知識頁面，與證明你能答對什麼的依據分開。你不必自己整理資料夾或維護第二套筆記。

學習檔案放在預設不納入 Git 的 `local/` 下。更新 Koji 時請保留此資料夾，替換共用指南檔案，而不是你的學習記錄。本機儲存並不代表 AI 離線處理。Koji 在對話期間運作，不提供背景提醒，也不會在各份副本間自動同步。

解釋和筆記遵循你的語言偏好，並保留日語例句和漢字讀音。指南以英語撰寫。README 翻譯由 AI 撰寫，未經獨立的母語人士審校；英語版為參考標準。

## README 語言

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
