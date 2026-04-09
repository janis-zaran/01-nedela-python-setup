# Projekta plāns — Izdevumu izsekotājs

## A. Programmas apraksts

Izdevumu izsekotājs ir Python komandrindas lietojums, kas ļauj lietotājam saglabāt savus ikdienas izdevumus JSON failā. Programma ļauj pievienot, apskatīt, filtrēt, dzēst un analizēt izdevumus, kā arī eksportēt tos CSV formātā.

Šī programma ir domāta personīgo finanšu uzskaitei, lai lietotājs varētu redzēt, kur un cik daudz naudas tiek iztērēts.

## B. Datu struktūra

Viens izdevuma ieraksts izskatās šādi:

```json
{
  "date": "2025-02-15",
  "amount": 12.50,
  "category": "Ēdiens",
  "description": "Pusdienas kafejnīcā"
}