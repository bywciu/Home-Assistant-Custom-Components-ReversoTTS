[![HACS Default][hacs_shield]][hacs]
[![GitHub Latest Release][releases_shield]][latest_release]
[![GitHub All Releases][downloads_total_shield]][releases]
[![Installations][installations_shield]][releases]

[hacs_shield]: https://img.shields.io/static/v1.svg?label=HACS&message=Default&style=popout&color=green&labelColor=41bdf5&logo=HomeAssistantCommunityStore&logoColor=white
[hacs]: https://hacs.xyz/docs/default_repositories

[latest_release]: https://github.com/bywciu/Home-Assistant-Custom-Components-ReversoTTS/releases/latest
[releases_shield]: https://img.shields.io/github/release/bywciu/Home-Assistant-Custom-Components-ReversoTTS.svg?style=popout

[releases]: https://github.com/bywciu/Home-Assistant-Custom-Components-ReversoTTS/releases
[downloads_total_shield]: https://img.shields.io/github/downloads/bywciu/Home-Assistant-Custom-Components-ReversoTTS/total
[installations_shield]: https://img.shields.io/badge/dynamic/json?url=https%3A%2F%2Fanalytics.home-assistant.io%2Fcustom_integrations.json&query=%24.reversotts.total&style=popout&color=41bdf5&label=analytics

# Reverso text-to-speech component for Home Assistant

The `Reverso` text-to-speech platform uses online Reverso Text-to-Speech engine to read a text with a natural sounding voices.  
This repo uses [pyttsreverso](https://github.com/rt400/pyttsreverso) library to call the Reverso API.

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

The language to use. Supported languages are in this table, please use only the name from the **Label** column:

| Label | LangCode | Voice | Gender | Language |
| ------------- | ------------- | ------------- | ------------- | ------------- |
| Arabic - Leila | Leila-Arabic | Leila22k | Female | Arabic |
| Arabic - Mehdi | Mehdi-Arabic | Mehdi22k | Male | Arabic |
| Arabic - Nizar | Nizar-Arabic | Nizar22k | Male | Arabic |
| Arabic - Salma | Salma-Arabic | Salma22k | Female | Arabic |
| Catalan - Laia | Laia-Catalan | Laia22k | Female | Catalan |
| Chinese (Mandarin) - Lulu | Lulu-Mandarin-Chinese | Lulu22k | Female | Mandarin Chinese |
| Czech - Eliska | Eliska-Czech | Eliska22k | Female | Czech |
| Danish - Mette | Mette-Danish | Mette22k | Female | Danish |
| Danish - Rasmus | Rasmus-Danish | Rasmus22k | Male | Danish |
| Dutch - Daan | Daan-Dutch | Daan22k | Male | Dutch |
| Dutch - Femke | Femke-Dutch | Femke22k | Female | Dutch |
| Dutch - Jasmijn | Jasmijn-Dutch | Jasmijn22k | Female | Dutch |
| Dutch - Max | Max-Dutch | Max22k | Male | Dutch |
| Dutch (BE) - Jeroen | Jeroen-Belgian-Dutch | Jeroen22k | Male | Belgian Dutch |
| Dutch (BE) - Sofie | Sofie-Belgian-Dutch | Sofie22k | Female | Belgian Dutch |
| Dutch (BE) - Zoe | Zoe-Belgian-Dutch | Zoe22k | Female | Belgian Dutch |
| English (AU) - Lisa | Lisa-Australian-English | Lisa22k | Female | Australian English |
| English (AU) - Tyler | Tyler-Australian-English | Tyler22k | Male | Australian English |
| English (GB) - Graham | Graham-British | Graham22k | Male | British English |
| English (GB) - Lucy | Lucy-British | Lucy22k | Female | British English |
| English (GB) - Peter | Peter-British | Peter22k | Male | British English |
| English (GB) - Queen Elisabeth | QueenElizabeth-British | QueenElizabeth22k | Female | British English |
| English (GB) - Rachel | Rachel-British | Rachel22k | Female | British |
| English (IN) - Deepa | Deepa-Indian-English | Deepa22k | Female | Indian English |
| English (US) - Heather | Heather-US-English | Heather22k | Female | American English |
| English (US) - Karen | Karen-US-English | Karen22k | Female | American English |
| English (US) - Kenny | Kenny-US-English | Kenny22k | Male | American English |
| English (US) - Laura | Laura-US-English | Laura22k | Female | American English |
| English (US) - Micah | Micah-US-English | Micah22k | Male | American English |
| English (US) - Nelly | Nelly-US-English | Nelly22k | Female | American English |
| English (US) - Rod | Rod-US-English | Rod22k | Male | American English |
| English (US) - Ryan | Ryan-US-English | Ryan22k | Male | American English |
| English (US) - Saul | Saul-US-English | Saul22k | Male | American English |
| English (US) - Sharon | Sharon-US-English | Sharon22k | Female | American English |
| English (US) - Tracy | Tracy-US-English | Tracy22k | Female | American English |
| English (US) - Will| Will-US-English | Will22k | Male | American English |
| Finnish - Sanna | Sanna-Finnish | Sanna22k | Female | Finnish |
| French - Alice | Alice-French | Alice22k | Female | French |
| French - Anais | Anais-French | Anais22k | Female | French |
| French - Antoine | Antoine-French | Antoine22k | Male | French |
| French - Bruno | Bruno-French | Bruno22k | Male | French |
| French - Claire | Claire-French | Claire22k | Female | French |
| French - Julie | Julie-French | Julie22k | Female | French |
| French - Manon | Manon-French | Manon22k | Female | French |
| French - Margaux | Margaux-French | Margaux22k | Female | French |
| French (BE) - Alice | Alice-BE-Belgian-French | Alice-BE22k | Female | Belgian French |
| French (BE) - Anais | Anais-BE-Belgian-French | Anais-BE22k | Female | Belgian French |
| French (BE) - Antoine | Antoine-BE-Belgian-French | Antoine-BE22k | Male | Belgian French |
| French (BE) - Bruno | Bruno-BE-Belgian-French | Bruno-BE22k | Male | Belgian French |
| French (BE) - Claire | Claire-BE-Belgian-French | Claire-BE22k | Female | Belgian French |
| French (BE) - Julie | Julie-BE-Belgian-French | Julie-BE22k | Female | Belgian French |
| French (BE) - Justine | Justine-Belgian-French | Justine22k | Female | Belgian French |
| French (BE) - Manon | Manon-BE-Belgian-French | Manon-BE22k | Female | Belgian French |
| French (BE) - Margaux | Margaux-BE-Belgian-French | Margaux-BE22k | Female | Belgian French |
| French (CA) - Louise | Louise-Canadian-French | Louise22k | Female | Canadian French |
| German - Andreas | Andreas-German | Andreas22k | Male | German |
| German - Claudia | Claudia-German | Claudia22k | Female | German |
| German - Julia | Julia-German | Julia22k | Female | German |
| German - Klaus | Klaus-German | Klaus22k | Male | German |
| German - Sarah | Sarah-German | Sarah22k | Female | German |
| Greek - Dimitris | Dimitris-Greek | Dimitris22k | Male | Greek |
| Hebrew - Asaf | he-IL-Asaf-Hebrew | he-IL-Asaf | Male | Hebrew |
| Italian - Chiara| Chiara-Italian | Chiara22k | Female | Italian |
| Italian - Fabiana | Fabiana-Italian | Fabiana22k | Female | Italian |
| Italian - Vittorio | Vittorio-Italian | Vittorio22k | Male | Italian |
| Japanese - Sakura | Sakura-Japanese | Sakura22k | Female | Japanese |
| Korean - Minji | Minji-Korean | Minji22k | Female | Korean |
| Norwegian - Bente | Bente-Norwegian | Bente22k | Female | Norwegian |
| Norwegian - Kari | Kari-Norwegian | Kari22k | Female | Norwegian |
| Norwegian - Olav | Olav-Norwegian | Olav22k | Male | Norwegian |
| Portuguese - Celia | Celia-Portuguese | Celia22k | Female | Portuguese |
| Portuguese (BR) - Marcia | Marcia-Brazilian | Marcia22k | Female | Brazilian Portuguese |
| Polish - Ania | Ania-Polish | Ania22k | Female | Polish |
| Polish - Monika | Monika-Polish | Monika22k | Female | Polish |
| Romanian - Andrei | ro-RO-Andrei-Romanian | ro-RO-Andrei | Male | Romanian |
| Russian - Alyona | Alyona-Russian | Alyona22k | Female | Russian |
| Spanish - Antonio | Antonio-Spanish | Antonio22k | Male | Spanish |
| Spanish - Ines | Ines-Spanish | Ines22k | Female | Spanish |
| Spanish - Maria | Maria-Spanish | Maria22k | Female | Spanish |
| Spanish (US) - Rodrigo | Rodrigo-US-Spanish | Rodrigo22k | Male | US Spanish |
| Spanish (US) - Rosa | Rosa-US-Spanish | Rosa22k | Female | US Spanish |
| Swedish - Elin | Elin-Swedish | Elin22k | Female | Swedish |
| Swedish - Emil | Emil-Swedish | Emil22k | Male | Swedish |
| Swedish - Emma | Emma-Swedish | Emma22k | Female | Swedish |
| Swedish - Erik | Erik-Swedish | Erik22k | Male | Swedish |
| Swedish (FI) - Samuel | Samuel-Finland-Swedish | Samuel22k | Male | Finland Swedish |
| Swedish (Gothenburg) - Kal | Kal-Gothenburg-Swedish | Kal22k | Male | Gothenburg Swedish |
| Swedish (Scanian) - Mia | Mia-Scanian | Mia22k | Female | Scanian Swedish |
| Turkish - Ipek | Ipek-Turkish | Ipek22k | Female | Turkish |

#### Pitch

The `pitch` (speak speed). The supported speed values are `10-100`, 100 is the normal speak.

default: "`100`"

#### Bitrate

The `bitrate` for the sound quality. The supported bitrate values are `22k, 96k, 128k, 192k, 320k`.

default: "`128k`"

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
          media_player_entity_id: media_player.google_mini_salon
          message: This is a test
        target:
          entity_id: tts.reverso_tts_polish_ania_100_320k
  ```
