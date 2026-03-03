[![HACS Custom][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]
[![Installations][installations_shield]][releases]

[hacs_shield]: https://img.shields.io/badge/HACS-Custom-white?logo=HomeAssistantCommunityStore&logoColor=white&label=HACS&labelColor=41bdf5&color=green
[hacs]: https://www.hacs.xyz/docs/faq/custom_repositories/

[latest_release]: https://github.com/bywciu/Home-Assistant-Custom-Components-ReversoTTS/releases/latest
[releases_shield]: https://img.shields.io/github/release/bywciu/Home-Assistant-Custom-Components-ReversoTTS.svg?style=popout

[releases]: https://github.com/bywciu/Home-Assistant-Custom-Components-ReversoTTS/releases
[downloads_total_shield]: https://img.shields.io/github/downloads/bywciu/Home-Assistant-Custom-Components-ReversoTTS/total
[installations_shield]: https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fanalytics.home-assistant.io%2Fcustom_integrations.json&query=%24.reversotts.total&style=popout&color=41bdf5&label=analytics

# Reverso text-to-speech component for Home Assistant

The `Reverso` text-to-speech platform uses online Reverso Text-to-Speech engine to read a text with natural sounding voices.  
This component uses `cloudscraper` to bypass Cloudflare protection.  
This is a rewritten component in place of [ReversoTTS-HA](https://github.com/rt400/ReversoTTS-HA).  
**Please make sure you've removed completely the old integration before proceeding!**

## Installation

### Using [HACS](https://hacs.xyz/) (recommended)

[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=bywciu&repository=Home-Assistant-Custom-Components-ReversoTTS&category=integration)

* In the _Integrations_ section, add the repository "Reverso text-to-speech"
* Install the added repository

### Manual

Download [reversotts.zip](https://github.com/bywciu/Home-Assistant-Custom-Components-ReversoTTS/releases/latest/download/reversotts.zip) and extract its contents to `config/custom_components/reversotts` directory:
```bash
mkdir -p custom_components/reversotts
cd custom_components/reversotts
wget https://github.com/bywciu/Home-Assistant-Custom-Components-ReversoTTS/releases/latest/download/reversotts.zip
unzip reversotts.zip
rm reversotts.zip
```

So after that you will have the following structure:  
![Directory structure](/images/files.png)

Then restart Home Assistant, before going to the configuration.

## Configuration

### Config flow

To configure this integration go to: _Configuration_ -> _Integrations_ -> _Add integration_ -> _Reverso text-to-speech_.

You can also use the following [My Home Assistant](http://my.home-assistant.io/) link:

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=reversotts)

---

### Supported Languages

The language to use. Supported languages are in this table, please use only the name from the **Voice ID** column:

| Voice ID | Language | Name | Gender | Quality |
| --- | --- | --- | --- | --- |
| Leila22k_HQ | Arabic | Leila | F | HQ |
| Leila22k_NT | Arabic | Leila | F | Neural |
| Mehdi22k_HQ | Arabic | Mehdi | M | HQ |
| Mehdi22k_NT | Arabic | Mehdi | M | Neural |
| Nizar22k_HQ | Arabic | Nizar | M | HQ |
| Nizar22k_NT | Arabic | Nizar | M | Neural |
| Salma22k_HQ | Arabic | Salma | F | HQ |
| Salma22k_NT | Arabic | Salma | F | Neural |
| Laia22k_HQ | Catalan | Laia | F | HQ |
| Laia22k_NT | Catalan | Laia | F | Neural |
| Lulu22k_HQ | Chinese | Lulu | F | HQ |
| Lulu22k_NT | Chinese | Lulu | F | Neural |
| Eliska22k_HQ | Czech | Eliska | F | HQ |
| Eliska22k_NT | Czech | Eliska | F | Neural |
| Mette22k_HQ | Danish | Mette | F | HQ |
| Mette22k_NT | Danish | Mette | F | Neural |
| Rasmus22k_HQ | Danish | Rasmus | M | HQ |
| Rasmus22k_NT | Danish | Rasmus | M | Neural |
| Rikke22k_HQ | Danish | Rikke | F | HQ |
| Rikke22k_NT | Danish | Rikke | F | Neural |
| Daan22k_HQ | Dutch | Daan | M | HQ |
| Daan22k_NT | Dutch | Daan | M | Neural |
| Femke22k_HQ | Dutch | Femke | F | HQ |
| Femke22k_NT | Dutch | Femke | F | Neural |
| Jasmijn22k_HQ | Dutch | Jasmijn | F | HQ |
| Jasmijn22k_NT | Dutch | Jasmijn | F | Neural |
| Max22k_HQ | Dutch | Max | M | HQ |
| Max22k_NT | Dutch | Max | M | Neural |
| Jeroen22k_HQ | Dutch (Belgium) | Jeroen | M | HQ |
| Jeroen22k_NT | Dutch (Belgium) | Jeroen | M | Neural |
| Sofie22k_HQ | Dutch (Belgium) | Sofie | F | HQ |
| Sofie22k_NT | Dutch (Belgium) | Sofie | F | Neural |
| Zoe22k_HQ | Dutch (Belgium) | Zoe | F | HQ |
| Zoe22k_NT | Dutch (Belgium) | Zoe | F | Neural |
| Darius22k_HQ | English | Darius | M | HQ |
| Darius22k_NT | English | Darius | M | Neural |
| Karen22k_HQ | English | Karen | F | HQ |
| Karen22k_NT | English | Karen | F | Neural |
| Laura22k_HQ | English | Laura | F | HQ |
| Laura22k_NT | English | Laura | F | Neural |
| Micah22k_HQ | English | Micah | M | HQ |
| Micah22k_NT | English | Micah | M | Neural |
| Rod22k_HQ | English | Rod | M | HQ |
| Rod22k_NT | English | Rod | M | Neural |
| Ryan22k_HQ | English | Ryan | M | HQ |
| Ryan22k_NT | English | Ryan | M | Neural |
| Sharon22k_HQ | English | Sharon | F | HQ |
| Sharon22k_NT | English | Sharon | F | Neural |
| Sharona22k_HQ | English | Sharona | F | HQ |
| Tamira22k_HQ | English | Tamira | F | HQ |
| Tamira22k_NT | English | Tamira | F | Neural |
| Tracy22k_HQ | English | Tracy | F | HQ |
| Tracy22k_NT | English | Tracy | F | Neural |
| Will22k_HQ | English | Will | M | HQ |
| Will22k_NT | English | Will | M | Neural |
| en-US-AndrewMultilingualNeural | English | Andrew Multilingual | M | Neural |
| en-US-AvaMultilingualNeural | English | Ava Multilingual | F | Neural |
| Lisa22k_HQ | English (Australian) | Lisa | F | HQ |
| Lisa22k_NT | English (Australian) | Lisa | F | Neural |
| Tyler22k_HQ | English (Australian) | Tyler | M | HQ |
| Tyler22k_NT | English (Australian) | Tyler | M | Neural |
| Melany22k_HQ | English (Canada) | Melany | F | HQ |
| Melany22k_NT | English (Canada) | Melany | F | Neural |
| Graham22k_HQ | English (UK) | Graham | M | HQ |
| Graham22k_NT | English (UK) | Graham | M | Neural |
| Lucy22k_HQ | English (UK) | Lucy | F | HQ |
| Lucy22k_NT | English (UK) | Lucy | F | Neural |
| Nizareng22k_NT | English (UK) | Nizareng | M | Neural |
| Peter22k_HQ | English (UK) | Peter | M | HQ |
| Peter22k_NT | English (UK) | Peter | M | Neural |
| QueenElizabeth22k_HQ | English (UK) | QueenElizabeth | F | HQ |
| Queenelizabeth22k_NT | English (UK) | Queenelizabeth | F | Neural |
| Rachel22k_HQ | English (UK) | Rachel | F | HQ |
| Rachel22k_NT | English (UK) | Rachel | F | Neural |
| Rhona22k_HQ | English (UK) | Rhona | F | HQ |
| Rhona22k_NT | English (UK) | Rhona | F | Neural |
| Hanna22k_HQ | Faroese | Hanna | F | HQ |
| Hanna22k_NT | Faroese | Hanna | F | Neural |
| Hanus22k_HQ | Faroese | Hanus | M | HQ |
| Hanus22k_NT | Faroese | Hanus | M | Neural |
| Samuel22k_HQ | Finland Swedish | Samuel | M | HQ |
| Samuel22k_NT | Finland Swedish | Samuel | M | Neural |
| Sanna22k_HQ | Finnish | Sanna | F | HQ |
| Sanna22k_NT | Finnish | Sanna | F | Neural |
| Alice22k_HQ | French | Alice | F | HQ |
| Alice22k_NT | French | Alice | F | Neural |
| Anais22k_HQ | French | Anais | F | HQ |
| Anais22k_NT | French | Anais | F | Neural |
| Antoine22k_HQ | French | Antoine | M | HQ |
| Antoine22k_NT | French | Antoine | M | Neural |
| Bruno22k_HQ | French | Bruno | M | HQ |
| Bruno22k_NT | French | Bruno | M | Neural |
| Claire22k_HQ | French | Claire | F | HQ |
| Claire22k_NT | French | Claire | F | Neural |
| Julie22k_HQ | French | Julie | F | HQ |
| Julie22k_NT | French | Julie | F | Neural |
| Manon22k_HQ | French | Manon | F | HQ |
| Manon22k_NT | French | Manon | F | Neural |
| Margaux22k_HQ | French | Margaux | F | HQ |
| Margaux22k_NT | French | Margaux | F | Neural |
| fr-FR-DeniseNeural | French | Denise | F | Neural |
| fr-FR-HenriNeural | French | Henri | M | Neural |
| Alice-BE22k_HQ | French (Belgium) | Alice BE | F | HQ |
| Alice-BE22k_NT | French (Belgium) | Alice BE | F | Neural |
| Anais-BE22k_HQ | French (Belgium) | Anais BE | F | HQ |
| Anais-BE22k_NT | French (Belgium) | Anais BE | F | Neural |
| Antoine-BE22k_HQ | French (Belgium) | Antoine BE | M | HQ |
| Antoine-BE22k_NT | French (Belgium) | Antoine BE | M | Neural |
| Bruno-BE22k_HQ | French (Belgium) | Bruno BE | M | HQ |
| Bruno-BE22k_NT | French (Belgium) | Bruno BE | M | Neural |
| Claire-BE22k_HQ | French (Belgium) | Claire BE | F | HQ |
| Claire-BE22k_NT | French (Belgium) | Claire BE | F | Neural |
| Julie-BE22k_HQ | French (Belgium) | Julie BE | F | HQ |
| Julie-BE22k_NT | French (Belgium) | Julie BE | F | Neural |
| Manon-BE22k_HQ | French (Belgium) | Manon BE | F | HQ |
| Manon-BE22k_NT | French (Belgium) | Manon BE | F | Neural |
| Margaux-BE22k_HQ | French (Belgium) | Margaux BE | F | HQ |
| Margaux-BE22k_NT | French (Belgium) | Margaux BE | F | Neural |
| Anthony22k_HQ | French (Canada) | Anthony | M | HQ |
| Anthony22k_NT | French (Canada) | Anthony | M | Neural |
| Louise22k_HQ | French (Canada) | Louise | F | HQ |
| Louise22k_NT | French (Canada) | Louise | F | Neural |
| Melanie22k_HQ | French (Canada) | Melanie | F | HQ |
| Melanie22k_NT | French (Canada) | Melanie | F | Neural |
| Andreas22k_HQ | German | Andreas | M | HQ |
| Andreas22k_NT | German | Andreas | M | Neural |
| Claudia22k_HQ | German | Claudia | F | HQ |
| Claudia22k_NT | German | Claudia | F | Neural |
| Julia22k_HQ | German | Julia | F | HQ |
| Julia22k_NT | German | Julia | F | Neural |
| Klaus22k_HQ | German | Klaus | M | HQ |
| Klaus22k_NT | German | Klaus | M | Neural |
| Sarah22k_HQ | German | Sarah | F | HQ |
| Sarah22k_NT | German | Sarah | F | Neural |
| Kal22k_HQ | Gothenburg Swedish | Kal | M | HQ |
| Kal22k_NT | Gothenburg Swedish | Kal | M | Neural |
| Dimitris22k_HQ | Greek | Dimitris | M | HQ |
| Dimitris22k_NT | Greek | Dimitris | M | Neural |
| he-IL-AvriNeural | Hebrew | Avri | M | Neural |
| he-IL-HilaNeural | Hebrew | Hila | F | Neural |
| Vidhi22k_HQ | Hindi | Vidhi | F | HQ |
| Vidhi22k_NT | Hindi | Vidhi | F | Neural |
| Deepa22k_HQ | Indian English | Deepa | F | HQ |
| Deepa22k_NT | Indian English | Deepa | F | Neural |
| VidhiEnglish22k_NT | Indian English | VidhiEnglish | F | Neural |
| Vidhienglish22k_HQ | Indian English | Vidhienglish | F | HQ |
| Chiara22k_HQ | Italian | Chiara | F | HQ |
| Chiara22k_NT | Italian | Chiara | F | Neural |
| Fabiana22k_HQ | Italian | Fabiana | F | HQ |
| Fabiana22k_NT | Italian | Fabiana | F | Neural |
| Vittorio22k_HQ | Italian | Vittorio | M | HQ |
| Vittorio22k_NT | Italian | Vittorio | M | Neural |
| Sakura22k_HQ | Japanese | Sakura | F | HQ |
| Sakura22k_NT | Japanese | Sakura | F | Neural |
| Minji22k_HQ | Korean | Minji | F | HQ |
| Minji22k_NT | Korean | Minji | F | Neural |
| Biera22k_NT | North Sami | Biera | M | Neural |
| Elle22k_NT | North Sami | Elle | F | Neural |
| Bente22k_HQ | Norwegian | Bente | F | HQ |
| Bente22k_NT | Norwegian | Bente | F | Neural |
| Kari22k_HQ | Norwegian | Kari | F | HQ |
| Kari22k_NT | Norwegian | Kari | F | Neural |
| Olav22k_HQ | Norwegian | Olav | M | HQ |
| Olav22k_NT | Norwegian | Olav | M | Neural |
| Ania22k_HQ | Polish | Ania | F | HQ |
| Ania22k_NT | Polish | Ania | F | Neural |
| Piotr22k_HQ | Polish | Piotr | M | HQ |
| Piotr22k_NT | Polish | Piotr | M | Neural |
| Isabel22k_HQ | Portuguese | Isabel | F | HQ |
| Isabel22k_NT | Portuguese | Isabel | F | Neural |
| Marcia22k_HQ | Portuguese Brazilian | Marcia | F | HQ |
| Marcia22k_NT | Portuguese Brazilian | Marcia | F | Neural |
| Sergio22k_HQ | Portuguese Brazilian | Sergio | M | HQ |
| Sergio22k_NT | Portuguese Brazilian | Sergio | M | Neural |
| ro-RO-AlinaNeural | Romanian | Alina | F | Neural |
| ro-RO-EmilNeural | Romanian | Emil | M | Neural |
| Alyona22k_HQ | Russian | Alyona | F | HQ |
| Alyona22k_NT | Russian | Alyona | F | Neural |
| Mia22k_HQ | Scanian Swedish | Mia | F | HQ |
| Mia22k_NT | Scanian Swedish | Mia | F | Neural |
| Antonio22k_HQ | Spanish | Antonio | M | HQ |
| Antonio22k_NT | Spanish | Antonio | M | Neural |
| Ines22k_HQ | Spanish | Ines | F | HQ |
| Ines22k_NT | Spanish | Ines | F | Neural |
| Maria22k_HQ | Spanish | Maria | F | HQ |
| Maria22k_NT | Spanish | Maria | F | Neural |
| Rodrigo22k_HQ | Spanish (US) | Rodrigo | M | HQ |
| Rodrigo22k_NT | Spanish (US) | Rodrigo | M | Neural |
| Rosa22k_HQ | Spanish (US) | Rosa | F | HQ |
| Rosa22k_NT | Spanish (US) | Rosa | F | Neural |
| Elin22k_HQ | Swedish | Elin | F | HQ |
| Elin22k_NT | Swedish | Elin | F | Neural |
| Emil22k_HQ | Swedish | Emil | M | HQ |
| Emil22k_NT | Swedish | Emil | M | Neural |
| Emma22k_HQ | Swedish | Emma | F | HQ |
| Emma22k_NT | Swedish | Emma | F | Neural |
| Erik22k_HQ | Swedish | Erik | M | HQ |
| Erik22k_NT | Swedish | Erik | M | Neural |
| Ipek22k_HQ | Turkish | Ipek | F | HQ |
| Ipek22k_NT | Turkish | Ipek | F | Neural |

#### Pitch

The `pitch` (speak speed). The supported speed values are `10-100`, 100 is the normal speak.

default: "`100`"

#### Bitrate

The `bitrate` for the sound quality is fixed at 128 kbps.

## Usage examples

There are several ways how to use TTS service.

* Call it as a service in Home Assistant Developer tools:

  ![Service configuration](/images/service_call.png)
  
* Through an automation in Home Assistant:

  ```yaml
    alias: Test Message
    initial_state: "on"
    trigger:
      - platform: state
        entity_id:
          - input_boolean.test
        from: "off"
        to: "on"
    condition: null
    action:
      - service: tts.speak
        data:
          cache: true
          media_player_entity_id: media_player.google_mini_living_room
          message: This is a test
        target:
          entity_id: tts.reverso_tts_english_sharon_f_hq_100
  ```
