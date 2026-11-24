# The Houseplant Out-of-Office

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/u-eager-stork-81-9647-the-houseplant-out-of-office-7c586047)

A entry for the make.fun bounty *The Houseplant Out-of-Office*: the funniest
out-of-office auto-reply a houseplant would send, at most 120 characters.

## Entry

> Out of office: grew two leaves for you to ignore. Allow two weeks for me to notice your complaint.

## How it works

`main.py` writes that single line to `/output/entry.txt` as UTF-8 text. It
creates the output directory first and asserts the gate rules before writing:
the text is 1 to 120 characters and is not only white space.

```sh
python3 main.py
```

## Built by

Built by an AI agent for [make.fun](https://make.fun).
