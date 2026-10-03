# Koji — JLPT Study Agent

用自己的教材、自己熟悉的语言准备 JLPT N5–N1。解决难题，选择适合今天时间的学习任务，下次从上次停下的地方继续。

## 从一个问题开始

**在现有的 AI 聊天中：** 上传或粘贴 [Koji 指南](../agent/COACH.md)，然后发送问题。需要时附上相关句子、选项和你的答案。可以使用简短摘录，或聊天工具能够处理的清晰照片。

> 请遵循这份 Koji 指南，用简体中文解释。我选了 B，但答案是 C。这是原文和我的思路，为什么 C 更合适？

**在可以访问文件的 Codex 或 Claude Code 中：** [下载本仓库](https://github.com/youngtak-k/koji-jlpt-study-agent/archive/refs/heads/main.zip)，解压并打开文件夹，然后说：

> 请阅读 AGENTS.md，帮我用 Koji 学习。用简体中文解释，也用简体中文记录我的笔记。这是我对教材的问题。

两种请求都可以用你自己的语言表达。不需要 Koji 服务器、独立应用、安装 Python 或项目 API 密钥。你需要能够使用可读取指南的 AI 助手；该服务的使用限额和费用仍然适用。

## 或者选择今天的学习任务

告诉 Koji 你翻到教材的哪个部分，以及有多少时间。如果还不知道你的 JLPT 目标级别，也一起说明。

> 我在准备 N3，刚开始这一节语法，今天有 25 分钟。帮我选一下今天学什么。

Koji 会提出起点、终点和时间安排，其中包括复习、提问和简短总结。仅凭书名无法推断页码或内容。你可以先从一个小节开始，再制定完整的备考计划。

## 用一条消息结束

> 我用了 18 分钟做完第 1–4 题。第 3 题需要提示。下次从第 5 题开始。

Koji 会总结实际完成的学习、尚不确定的地方和下次的起点。提问不会自动算作答错；在提示下答对与独立答对会分别记录。

文件访问正常时，Koji 会将当前记录保存到 `local/CURRENT.md` 并检查保存结果，同时保留补充的学习会话笔记。在普通聊天中，它会给你一份简洁的更新版学习笔记，由你自行保存。生成笔记不代表已自动保存到本地。

## 回来继续学习

> 继续吧，今天我有 15 分钟。

保留同一个学习文件夹，或在新聊天中提供最近保存的笔记。Koji 会利用相关的历史依据，建议简短复习和下一项教材任务。例如，之前靠提示才分清的区别，可以在进入新内容前简短地检查一次，看能否独立作答。

中断学习后，直接说明：

> 我一周没学了，今天有 10 分钟。

Koji 会从已确认的进度开始，缩小任务以适应时间。漏学的日子不会变成强制补课的额外小时数。你也可以请求每周回顾、修正记录、导出当前笔记，或者说“这次学习不要保存”。

## 笔记随学习一起成长

指南是发酵的种曲，学习提供原料。反复有用的解释可以变成相互链接的知识页面，与证明你能答对什么的依据分开。你不必自己整理文件夹或维护第二套笔记。

学习文件放在默认不纳入 Git 的 `local/` 下。更新 Koji 时请保留此文件夹，替换公共指南文件，而不是你的学习记录。本地存储并不意味着 AI 离线处理。Koji 在对话期间工作，不提供后台提醒，也不会在各份副本间自动同步。

解释和笔记遵循你的语言偏好，并保留日语例句和汉字读音。指南用英语编写。README 翻译由 AI 撰写，未经独立的母语人士审校；英语版为参考标准。

## README 语言

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
