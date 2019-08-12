# Try-it

https://api-tv.tk/api/tnt

> Please note that free Heroku is a shitty hosting plateform for an api

# Routes

```
/api/tnt
/api/generaliste
/api/canal-tps
/api/cinema
/api/sport
/api/information
/api/belgique-suisse
/api/jeunesse
/api/musique
/api/documentaire
/api/serie
```

# Response template

```
[
  {
    "chaine1": {
      "logo": "https://example.com/logo.png",
      "heure": "21H05",
      "titre": "Whiskey Cavalier",
      "resume": "Frankie, Susan et Will sont rejoints par la nouvelle amie de ce dernier ...",
      "lien": "https://www.programme.tv/c37492889-whiskey-cavalier/espagne-trains-et-automobiles-152644522/",
      "subtitle": "Espagne, trains et automobiles",
      "long-title": "Whiskey Cavalier - Espagne, trains et automobiles",
      "type": "Série",
      "infos": [
        "Saison : 1 - Episode : 7/13",
        "Durée : 50 min"
      ],
      "long-resume": "Frankie, Susan et Will sont rejoints par la nouvelle amie de ce dernier alors qu'ils se rendent en Espagne pour récupérer du plutonium tombé entre de mauvaises mains. Dans le même temps, Standish tente d'améliorer ses techniques de séduction."
    },
    "chaine2": { ... }
  },
  {
    "chaine1": { ... },
    "chaine2": { ... }
  },
  {
    "chaine1": { ... },
    "chaine2": { ... }
  }
]
```

# Important notes

- Response always return an array containing 3 `key-value` objects => `[today, tomorrow, in 2 days]`
- Parameter `infos`, not always contains the same data
