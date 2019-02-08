Te la hago corta:
  Bot que vota por la candidata de Valle Fértil para reina del sol en la FNS19

# Considerando:

- Que el martes 5 de febrero del 2019 se habilitó la votación para elegir la reina de la fiesta nacional del sol, en San Juan;
- Que la votación se hace a través de los diarios digitales de la provincia;
- Que ninguno de los medios incorporó un captcha para evitar spameo a la encuesta;
- Que, a simple vista, la única medida implementada para evitar más de un voto por persona es la instalación de una cookie en el browser del cliente;
- Que, como toda medida de seguridad del lado del cliente, la implementación de una cookie falla catastróficamente;

# El Comité Provincial Contra la Pelotudez Informática de las Autoridades Sanjuaninas (CPCPIS) Resuelve:

- Art1: Implementar un Bot para votar en las encuestas de cada diario digital.
- Art2: Elegir a la candidata de Valle Fértil para cada voto emitido por este Bot, sin alguna razón en especial. 
- Art3: Dejar en funcionamiento el Bot durante tanto tiempo como sea posible.
- Art4: Llevar un conteo de todos los votos emitidos por este Bot y compararlo con el resultado final en el día de la 
"coronación".
- Art5: Denunciar por el medio que se crea conveniente, si alguno de los medios digitales que permite ver los resultados de la 
votación, vulneró el conteo de votos. Estos medios son Diario El Zonda y DameNoticias (directamente) y Diario La Provincia (indirectamente).
- Art6: Continuar creando este tipo de programas en tanto las autoridades sanjuaninas permitan, de forma empecinada, implementar este tipo de "soluciones" para la votación de la reina del sol.

# Modo de uso:
Votar en todos los diarios:
```
$> python überBot.py all
```

Votar en Diario de Cuyo: 
```
$> python überBot.py DDC
```

Para votar en los otros diarios: 
```
Argumentos: DDC, DH, DM, DN, ZONDA, S8, DLP
```

# Predicciones:
Al día 7 de febrero del 2019, mis predicciones para ganadora de la votación electrónica son:

1. Valle Fértil
2. Chimbas
-
1. Chimbas
2. Valle Fértil

Por si no lo saben, a menos que todo el pueblo chimbero esté votando todo el día todos los días por su candidata, alguien en chimbas también implementó un bot de votación.

# Curiosidades:
- Al día 7 de febrero del 2019, el sitio web del Diario La ventana, http://diariolaventana.com, tiene implementada la votación de forma tal que cada voto emitido no tiene correspondencia con ninguna de las candidatas.
En el código HTML de la encuesta, cada candidata debería tener un Id asociado con el cuál enviarle la petición de voto al servidor y así sumar +1 a la opción correspondiente a dicho Id. En la actualidad, en la encuesta de dicho diario, todas las candidatas tienen el mismo Id: "VOTAR". En definitiva, no importa en qué opción haga click el usuario; al Diario La Ventana lo único que le llega es un mensaje que dice "VOTAR".

El código:
```
<input name="voto" type="submit" value="VOTAR" title="VOTAR" />
```
debería ser, por ejemplo:
```
<input name="voto" type="submit" value="18" title="VOTAR" />
```

- ...

# Nota final:

La ganadora de la votación a través de los diarios suma 2 votos la noche de la "coronación". Esta cantidad no es suficiente como para marcar una diferencia en los números finales, pero este Bot es un perfecto experimento para ver si, marcando tendencia a través de los medios digitales, se puede influenciar a los jurados en la noche de la votación.

Veremos.

Llega a ganar la de Valle Fértil y me voy a la mierda.

jgilhutton.
