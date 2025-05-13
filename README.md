# IKEA produktu cenu skrāpēšanas un analīzes rīks

## Projekta apraksts

Šī projekta mērķis ir izveidot Python programmu, kas automatizē produktu cenu iegūšanu no mājaslapas [ikea.lv](https://www.ikea.lv), tos apstrādā un piedāvā lietotājam ērtas analīzes iespējas. Lietotājs var iegūt konkrētas kategorijas preces (piemēram, krēslus, galdus utt.), kurām tiek nolasīts preces nosaukums, cena un saite.

Dati tiek strukturēti, izmantojot lietotāja definētas datu struktūras, un uz tiem tiek veikta efektīva kārtošana, meklēšana un nosaukumu hešošana. Tādējādi tiek praktiski izmantotas datu struktūru un algoritmu zināšanas, kuras iegūtas kursa laikā.

Projekts tiek realizēts divatā, izmantojot GitHub versiju kontroles sistēmu, kurā tiek uzglabāts gan avota kods, gan dokumentācija, tajā skaitā šis README fails.

## Izmantotās bibliotēkas

- `requests` – lapas HTML satura ielādei.
- `BeautifulSoup4` – HTML parsēšanai un datu izgūšanai no struktūras.
- `hashlib` (vai `hash()` funkcija) – nosaukumu hešošanai un atslēgu ģenerēšanai.
- `json` / `csv` – datu saglabāšanai.
- `argparse` vai `rich` – lietotāja interfeisam (CLI).
- (papildus var izmantot `tkinter` vai `Textual` saskarnei, ja būs laiks)

## Programmatūras iespējas

- Iegūt IKEA preču datus no konkrētas kategorijas.
- Attēlot datus sakārtotus pēc cenas (izmantojot paša realizētu kārtošanas algoritmu).
- Veikt meklēšanu pēc nosaukuma.
- Parādīt preču nosaukumu hash vērtības.
- Saglabāt apstrādātos datus CSV vai JSON failā.

---

## ✅ Darāmo darbu saraksts (To-do list)

### 👤 1. Komandas dalībnieks: A

- [ ] Izveidot sākotnējo GitHub repozitoriju un README struktūru
- [ ] Implementēt web scraping funkcionalitāti (ar `requests` un `BeautifulSoup`)
- [ ] Izveidot produktu klasi ar vajadzīgajiem atribūtiem (nosaukums, cena, saite utt.)
- [ ] Realizēt datu saglabāšanu JSON/CSV failā
- [ ] Veikt pamata testus scraping daļai
- [ ] Dokumentēt scraping kodu un funkcionalitāti

### 👤 2. Komandas dalībnieks: B

- [ ] Izveidot datu struktūru preču uzglabāšanai (piem., saraksts ar objektiem vai vārdnīca)
- [ ] Implementēt vismaz vienu paša realizētu kārtošanas algoritmu (piem., QuickSort)
- [ ] Implementēt meklēšanas funkciju (lineāra un bināra, pēc nosaukuma vai cenas)
- [ ] Realizēt nosaukumu hešošanu (ar `hash()` vai `hashlib`)
- [ ] Izveidot vienkāršu CLI izvēlni lietotājam
- [ ] Palīdzēt ar projekta gala dokumentāciju

### 🧩 Kopīgi

- [ ] Nodrošināt GitHub commit vēsturi un versiju kontroli
- [ ] Sagatavot gala prezentācijas video (piem., ar `OBS` vai `ScreenRec`)
- [ ] Uzrakstīt pilnu README.md dokumentāciju latviešu valodā
- [ ] Testēt pilnu lietojamību no sākuma līdz beigām
