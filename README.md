# My.Assistant

**Warning:** This project is a Proof of Concept. I will modify it when I complete it.

## Hardware setup
- Raspberry 4
- Keyestudio 5V ReSpeaker 2 Mic Pi HAT V1.0
- Board PAM8403 (Amplifier)
- 2x Speaker 52mm 4Ω 3W
- Powerbank 20000mah (2x USB, 1 USB-c, 1 mini usb)

## Software setup
- [Seed Voicecard](https://github.com/HinTak/seeed-voicecard) used as driver for *Keyestudio 5V 2 Mic Pi HAT V1.0* since official version is outdated
- [Vosk](https://github.com/alphacep/vosk-api) tested with python and worked fine, but I want to improve it by compiling the C code to improve performance.
- [Piper](https://github.com/rhasspy/piper) actually I didn't test yet, but when I try, I will give a feedback.


## Useful commands
- `aplay -l` # get all output devices
- `amixer -c 3 sset 'Headphone' 60%` # set volume of headset (Keyestudio 5V ReSpeaker output). It will only work if Keyestudio 5V ReSpeaker is card 3
- `amixer -c 3 sset 'Speaker' 60%` # set volume of speaker (Keyestudio 5V ReSpeaker output). It will only work if Keyestudio 5V ReSpeaker is card 3