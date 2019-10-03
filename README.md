## Text mining 2019 - Clustering
## Introduccion
Se utilizaron algunas oraciones de un corpus de la lengua española para realizar un análisis del mismo utilizando clustering. 

## Desarrollo del pipeline

### Preprocesamiento
Como parte del preprocesamiento se decidió no cambiar la escencia del texto quitando _stopwords_ o borrando carecteres probablemente inutiles para el modelo. Esto se debe a que para el procesamiento del texto se utilizó el pipeline de __spacy__ y la idea era darle a __spacy__ la mayor cantidad de informacion posible de cada documento, por mas que existia la posibilidad de que al haber 'ruido' el analisis se complejizara o perdiera calidad.

### Armado de diccionario de features
Se analizo cada oracion con __spacy__ y se tuvieron en cuenta los siguientes puntos:
    1) Oraciones de tamaño mayor a 7 palabras
    2) Part of speech tag de cada palabra
    3) En cada caso se utilizo una ventana de 2 palabras a izquierda y derecha de cada token junto tambien con sus respectivos _POS_ tags
    
### Vectorizacion
Para realizar la vectorizacion, se utilizo `DictVectorizer` junto con `TruncatedSVD` para la reduccion de dimensionalidad.

### Clustering
Como algoritmo de clustering se utilizo `KMeans` luego de una etapa de prueba-error en comparacion con el algoritmo de clustering jerarquico `AgglomerativeClustering`.
Los resultados con `KMeans` parecian ser mas interesantes, pero el otro algoritmo no se quedaba atrás.



### Resultados - clusters
A continuacion presentamos algunos clusters interesantes de analizar:
-  Para k = 40:
    - Preposiciones:
    
            ['De', 'Para', 'Según', 'con', 'de', 'del', 'durante', 'en', 'entre', 'hasta', 'para', 'por', 'según']
    - Numeros y posiciones:
    
            ['Estos', 'cada', 'cinco', 'como', 'cuatro', 'el', 'esta', 'ex', 'gran', 'la', 'las', 'los', 'mejor', 'mismo', 'más', 'ocho', 'otros', 'primer', 'primera', 'primeros', 'sea', 'segunda', 'siguiente', 'su', 'sus', 'tercera', 'tiene', 'tres', 'un', 'una', 'unos', 'última', 'últimas']

    - Verbo ser y tener:
    
            ['Casi', 'En', 'Era', 'Es', 'Fue', 'No', 'Se', 'También', 'Tiene', 'Tras', 'Tuvo', 'a', 'al', 'como', 'con', 'cuando', 'diecisiete', 'donde', 'era', 'eran', 'es', 'estaba', 'está', 'están', 'fue', 'había', 'lo', 'para', 'per', 'que', 'se', 'siempre', 'siendo', 'sobre', 'tenía', 'tiene']

-  Para k = 80:
    - Paises o ciudades:
    
            ['Beni', 'Congo', 'Cooperstown', 'Estado', 'Europa', 'Gas', 'Inglaterra', 'Kronstadt', 'Macorís', 'María', 'Mauá', 'Mayo', 'Milán', 'Monatte', 'Monnate', 'Pacífico', 'París', 'Patterson', 'Rusia', 'SFIC', 'Sousa', 'Trotsky', 'Zimmerwald', 'África', 'Étudiants']
    - Nacionalidades y politica:
    
            ['anarquistas', 'azufre', 'comunista', 'decayó', 'departamentales', 'esenciales', 'extranjeros', 'franceses', 'francés', 'inglesa', 'internacionalista', 'obrero', 'ovalada', 'parisinos', 'revolucionario', 'sagrada', 'sindical', 'sindicalista', 'suizo', 'très', 'verdadero', 'véase', 'y']

    - Pronombres:
    
            ['Al', 'Del', 'El', 'En', 'Esta', 'La', 'Los', 'Por', 'Su', 'Sus', 'esta', 'su', 'un', 'una']

-  Para k = 120:
    - Paises o ciudades:
    
            ['América', 'Bélgica', 'Censo', 'Clubes', 'Dakota', 'Francia', 'Inglaterra', 'Lyon', 'Montrouge', 'Moscú', 'Oro', 'Otsego', 'París', 'Pennington', 'Prado', 'Rosmer', 'Río', 'Servicio', 'Suiza', 'Tiziano', 'Trotsky', 'Tríptico']
    - Nombres propios:
    
            ['Adrien', 'Alfred', 'Amanitaceae', 'Armamento', 'Atlético', 'Béla', 'Cherry', 'Christian', 'Comédie', 'David', 'Dique', 'Embarcadero', 'Estados', 'Evenkiysky', 'Geografía', 'Grigori', 'Ing', 'Internacional', 'José', 'L', 'Laurens', 'Mary', 'Milford', 'Montagne', 'Morris', 'Nacional', 'Otego', 'Pierre', 'Real', 'Samuel', 'Tungus', 'Vaca', 'Vergeat', 'Victor']

    - Posiciones:
    
            ['ex', 'extensa', 'futuros', 'gran', 'inmensa', 'mejor', 'minerales', 'ocho', 'pequeño', 'pequeños', 'primer', 'primera', 'primeros', 'principal', 'segunda', 'siguiente', 'soldadura', 'tres', 'últimas']


### Conclusión
En conclusión, este proyecto permite notar que existen innumerables combinaciones de procesamiento-vectorizacion-modelado lo que lleva a que queden pendientes varios intentos.
El resultado final no fue el esperado, podria haber sido mucho mejor.
Como mejora a futuro, me gustaria cambiar la forma de armado del diccionario de features, incluyendo para cada palabra un unico diccionario de features, ya que, en el caso actual, se toma a cada palabra en analisis dentro de la oracion donde pertenece y no en cuanto al corpus entero, esto trae problemas como tener palabras iguales en distintos clusters.


